from PIL import Image
import numpy as np
import torch
from torch.autograd import Variable
from torchvision import transforms
from ResNet50_helper.net import f_model, c_model, p_model
from ResNet50_helper.utils import *
from FeatureExtractor import *


class ResNet50Config:
    BACKBONE = "ResNet50"
    DIM_FEATURE = 512+30
    USE_TWO_FEATURES = True
    NEED_EXTRA_NORM = False
    TRANSFORM = transforms.Compose([
        transforms.Resize((224, 224), interpolation=3),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])


class ResNet50Extractor(Extractor):

    def __init__(self, config, weights_path):
        super(ResNet50Extractor, self).__init__(config=config)
        main_model = f_model(model_path=weights_path).cuda()
        color_model = c_model().cuda()
        pooling_model = p_model().cuda()
        self.extractor = FeatureExtractor(main_model, color_model, pooling_model)

    def img_preprocess(self, img):
        img_pil = Image.fromarray(img)
        img_t = self.config.TRANSFORM(img_pil)
        img_batch = torch.stack([img_t], 0, out=None)
        data = Variable(img_batch).cuda()
        return data

    def forward(self, data):
        deep_feat, color_feat = self.extractor(data)
        feat = np.concatenate((deep_feat[0], color_feat[0]), axis=0)
        return feat
