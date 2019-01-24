import numpy as np
from PIL import Image
from abc import abstractmethod


class Config:
    BACKBONE = ""
    DIM_FEATURE = None
    NEED_EXTRA_NORM = False


class Extractor:

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
            data = self.img_preprocess(img)
            features[k, :] = self.forward(data)
            print(k)
        if self.config.NEED_EXTRA_NORM:
            features = self.norm_features(features)
        if save_features:
            np.save(features_path, features)
        return features

    @abstractmethod
    def forward(self, img):
        pass
