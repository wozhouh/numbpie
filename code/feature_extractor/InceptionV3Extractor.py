import tensorflow as tf
from feature_extractor.FeatureExtractor import *


class InceptionV3Config:

    BACKBONE = "InceptionV3"
    DIM_FEATURE = 2048
    NEED_EXTRA_NORM = True
    INPUT_NODE = 'DecodeJpeg:0'
    OUTPUT_NODE = 'pool_3/_reshape:0'


class InceptionV3Extractor(Extractor):

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
        return feature
