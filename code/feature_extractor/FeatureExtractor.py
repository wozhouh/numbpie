import numpy as np
from abc import abstractmethod


class Config:
    BACKBONE = ""
    DIM_FEATURE = None
    NEED_EXTRA_NORM = False


class Extractor:

    def __init__(self, config):
        self.config = config

    def img_preprocess(self, img):
        return np.array(img)

    def norm_features(self, features):
        features_l2norm = np.sqrt(np.sum(features**2, axis=1).reshape(-1, 1))
        return features / features_l2norm

    # PIL image of RGB format
    def extract_features(self, img):
        data = self.img_preprocess(img)
        features = self.forward(data)
        if self.config.NEED_EXTRA_NORM:
            features = self.norm_features(features)
        return features  # [1, DIM]

    @abstractmethod
    def forward(self, img):
        pass
