import numpy as np
from PIL import Image
from abc import abstractmethod
import tensorflow as tf


class Config:
    BACKBONE = ""
    DIM_FEATURE = None
    NEED_EXTRA_NORM = False


class InceptionV3Config:
    BACKBONE = "InceptionV3"
    DIM_FEATURE = 2048
    NEED_EXTRA_NORM = True
    INPUT_NODE = 'DecodeJpeg:0'
    OUTPUT_NODE = 'pool_3/_reshape:0'


class FeatureExtractor:

    def __init__(self, config):
        self.config = config

    def img_read(self, img_path):
        img = Image.open(img_path).convert('RGB')
        return np.asarray(img)

    def img_preprocess(self, img):
        return img

    def norm_features(self, features):
        features_l2norm = np.sqrt(np.sum(features**2, axis=1).reshape(-1, 1))
        return features / features_l2norm

    def extract_features(self, img_path_list, save_features=False, features_path=""):
        img_num = len(img_path_list)
        features = np.zeros((img_num, self.config.DIM_FEATURE), dtype=np.float32)
        for k, img_path in enumerate(img_path_list):
            img = self.img_read(img_path)
            img = self.img_preprocess(img)
            features[k, :] = self.forward(img)
        if self.config.NEED_EXTRA_NORM:
            features = self.norm_features(features)
        if save_features:
            np.save(features_path, features)
        return features

    @abstractmethod
    def forward(self, img):
        pass


class InceptionV3Extractor(FeatureExtractor):
    def __init__(self, config, model_path):
        super(InceptionV3Extractor, self).__init__(config=config)
        graph_def = tf.GraphDef.FromString(open(model_path, 'rb').read())
        tf.Graph().as_default()
        tf.import_graph_def(graph_def, name='')
        gpu_options = tf.GPUOptions(allow_growth=True)
        sess_config = tf.ConfigProto(log_device_placement=False, gpu_options=gpu_options)
        self.sess = tf.Session(config=sess_config)

    def forward(self, img):
        feature = self.sess.run(self.config.OUTPUT_NODE, feed_dict={self.config.INPUT_NODE: img})
        return feature[0]
