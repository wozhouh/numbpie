#coding:utf-8  
# -*- coding: utf-8 -*-  
# @Time    : 2019/1/24
# @Author  : yangguofeng   
# @Software: Pycharm

from PIL import Image
import os

from src.gans import Modifier
from src.features import AkiwiFeatureGenerator, ResnetFeatureGenerator
from src.search import Search, CombinedSearch

from src.pipeline import FashionGANApp

import warnings
warnings.filterwarnings('ignore')

# Load Search Models
folder_gens = {'akiwi_50': AkiwiFeatureGenerator(50), 
               'resnet': ResnetFeatureGenerator()}

dress_imgs = './data/images/fashion/dresses/'
model_imgs = './data/images/fashion_models/dresses_clustered/'

dress_feats = './data/features/fashion/dresses/'
model_feats = './data/features/fashion_models/dresses/'

dress_search = {}
for dir_name, gen in folder_gens.items():
    dress_search[dir_name] = Search(dress_imgs, os.path.join(dress_feats, dir_name), gen)

model_search = {}
for dir_name, gen in folder_gens.items():
    model_search[dir_name] = Search(model_imgs, os.path.join(model_feats, dir_name), gen)

# combined search
dress_resnet50 = CombinedSearch([dress_search['akiwi_50'], dress_search['resnet']], factors=[2, 1])
model_resnet50 = CombinedSearch([model_search['akiwi_50'], model_search['resnet']], factors=[2, 1])

# FashionGAN Search

modifier = Modifier('./data/models/')
app = FashionGANApp(modifier, dress_resnet50, model_resnet50)

test_img = Image.open('./data/images/fashion/dresses/9815337.jpg')

app.start(test_img)