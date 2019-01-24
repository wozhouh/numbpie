#coding:utf-8  
# -*- coding: utf-8 -*-  
# @Time    : 2019/1/24
# @Author  : yangguofeng   
# @Software: Pycharm

import os
import glob
import numpy as np
import sys
sys.path.append('..')

from src import features, search

# Load Data

# path with all image files
data_path = '../data/images/fashion_models/dresses_clustered/*.jpg'
# path to save features - subfolders for each feature name will be created
feature_root = '../data/features/fashion_models/dresses/'

# read data
filelist = glob.glob(data_path)
filelist = sorted(filelist)
print('num images: ', len(filelist))

# Akiwi Features

feature_path = os.path.join(feature_root, 'akiwi_114')
feature_gen = search.AkiwiFeatureGenerator(114)

features.download_feature_vectors(filelist, feature_path, feature_gen)

# Split 114 features into 64 and 50

feat_path64 = os.path.join(feature_root, 'akiwi_64')
if not os.path.exists(feat_path64):
    os.makedirs(feat_path64)
    
feat_path50 = os.path.join(feature_root, 'akiwi_50')
if not os.path.exists(feat_path50):
    os.makedirs(feat_path50)

feats114 = glob.glob(os.path.join(feature_path,'*.npy'))
for idx, file in enumerate(feats114):
    if idx % 1000 == 0:
        print(idx)
    
    fv = np.load(file)
    
    feat64 = fv[:64]
    np.save(os.path.join(feat_path64, os.path.basename(file)), feat64)
    
    feat50 = fv[64:]
    np.save(os.path.join(feat_path50, os.path.basename(file)), feat50)

# Original ResNet152 Features

feature_path = os.path.join(feature_root, 'resnet')
feature_gen = search.ResnetFeatureGenerator()

features.download_feature_vectors(filelist, feature_path, feature_gen)

# Retrained ResNet152 Features
feature_path = os.path.join(feature_root, 'resnet_retrained')
feature_gen = search.ResnetFeatureGenerator('../data/models/resnet152_retrained.pth')
features.download_feature_vectors(filelist, feature_path, feature_gen)
