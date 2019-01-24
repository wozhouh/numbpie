# -*- coding: utf-8 -*-
# Author: yongyuan.name
import os
import h5py
import numpy as np
import argparse

from extract_cnn_vgg16_keras import VGGNet


'''
 Returns a list of filenames for all jpg images in a directory. 
'''
def get_imlist(path):
     return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')]
    #return [os.path.join(path,f) for f in os.listdir(path)]


'''
 Extract features and index the images
'''
if __name__ == "__main__":

    db = "/Users/yangguofeng/Downloads/flask-keras-cnn-image-retrieval-master/database"
    img_list = get_imlist(db)
    
    print("--------------------------------------------------")
    print("         feature extraction starts")
    print("--------------------------------------------------")
    
    feats = []
    names = []

    model = VGGNet()


    for i, img_path in enumerate(img_list):
        norm_feat = model.extract_feat(img_path)
        img_name = os.path.split(img_path)[1]
        feats.append(norm_feat)
        names.append(img_name)
        print("extracting feature from image No. %d , %d images in total" %((i+1), len(img_list)))

    feats = np.array(feats)
    # print(feats.shape)
    # directory for storing extracted features
    output = "/Users/yangguofeng/Downloads/flask-keras-cnn-image-retrieval-master/vgg_16_Cosine similarity.h5"
    
    print("--------------------------------------------------")
    print("      writing feature extraction results ...")
    print("--------------------------------------------------")


    h5f = h5py.File(output, 'w')
    h5f.create_dataset('dataset_1', data = feats)
    # h5f.create_dataset('dataset_2', data = names)
    h5f.create_dataset('dataset_2', data = np.string_(names))
    h5f.close()

'''
from annoy import AnnoyIndex

f = 512       # dim of the feature
t = AnnoyIndex(f)
# 如1000,代表一共有1000个实例
# FEATURE(i),代表第i个实例的特征

for i, img_path in enumerate(img_list):
        v = model.extract_feat(img_path)
        t.add_item(i, v)
        print("extracting feature from image No. %d , %d images in total" %((i+1), len(img_list)))

t.build(50) # 10 trees
t.save('vgg_nnoy.ann')
'''