# -*- coding: utf-8 -*-

import os

import numpy as np
import matplotlib.image as mpimg
from PIL import Image
import tensorflow as tf
from ssd_detector import np_methods


# configurations of the SSD person detector model
class SSD_Config:
    NAME = 'SSD'
    NET_SHAPE = (300, 300)
    FEAT_SHAPES = [(38, 38), (19, 19), (10, 10), (5, 5), (3, 3), (1, 1)]
    NUM_LEVELS = len(FEAT_SHAPES)
    NUM_CLASSES = 2
    ANCHOR_SIZES = [(21., 45.), (45., 99.), (99., 153.), (153., 207.), (207., 261.), (261., 315.)]
    ANCHOR_RATIOS = [[.5], [.5, 1. / 3], [.5, 1. / 3], [.5, 1. / 3], [.5], [.5]]
    ANCHOR_STEPS = [8, 16, 32, 64, 100, 300]
    ANCHOR_OFFSET = 0.5
    SELECT_THRESHOLD = 0.40
    NMS_THRESHOLD = 0.45
    INPUT_NODE = "Placeholder:0"
    OUTPUT_NODES = ["ssd_300_vgg/block4_box/Reshape:0", "ssd_300_vgg/block7_box/Reshape:0",
                    "ssd_300_vgg/block8_box/Reshape:0", "ssd_300_vgg/block9_box/Reshape:0",
                    "ssd_300_vgg/block10_box/Reshape:0", "ssd_300_vgg/block11_box/Reshape:0",
                    "ssd_300_vgg/softmax/Reshape_1:0", "ssd_300_vgg/softmax_1/Reshape_1:0",
                    "ssd_300_vgg/softmax_2/Reshape_1:0", "ssd_300_vgg/softmax_3/Reshape_1:0",
                    "ssd_300_vgg/softmax_4/Reshape_1:0", "ssd_300_vgg/softmax_5/Reshape_1:0"]

# SSD person detector class
class SSD_model:

    def __init__(self, model_path):
        self.config = SSD_Config()

        # Load the model of the frozen graph
        self.graph_def = tf.GraphDef.FromString(open(model_path, 'rb').read())
        tf.Graph().as_default()
        tf.import_graph_def(self.graph_def, name='')

        # Create a session
        gpu_options = tf.GPUOptions(allow_growth=True)
        sess_config = tf.ConfigProto(log_device_placement=False, gpu_options=gpu_options)
        self.sess = tf.Session(config=sess_config)

        # Anchors
        self.ssd_anchors = np_methods.ssd_anchors_all_layers(self.config.NET_SHAPE, self.config.FEAT_SHAPES,
                                                             self.config.ANCHOR_SIZES, self.config.ANCHOR_RATIOS,
                                                             self.config.ANCHOR_STEPS, self.config.ANCHOR_OFFSET)

    def detect(self, img):
        input_feed_dict = {self.config.INPUT_NODE: img}
        outputs_list = self.sess.run(self.config.OUTPUT_NODES, feed_dict=input_feed_dict)
        rlocalisations = outputs_list[:self.config.NUM_LEVELS]
        rpredictions = outputs_list[self.config.NUM_LEVELS:]
        rbbox_img = [0., 0., 1., 1.]

        # get classes and bboxes from the net outputs
        rclasses, rscores, rbboxes = np_methods.ssd_bboxes_select(
            rpredictions, rlocalisations, self.ssd_anchors,
            select_threshold=self.config.SELECT_THRESHOLD, img_shape=self.config.NET_SHAPE,
            num_classes=self.config.NUM_CLASSES, decode=True)

        rbboxes = np_methods.bboxes_clip(rbbox_img, rbboxes)
        rclasses, rscores, rbboxes = np_methods.bboxes_sort(rclasses, rscores, rbboxes, top_k=300)
        rclasses, rscores, rbboxes = np_methods.bboxes_nms(rclasses, rscores, rbboxes,
                                                           nms_threshold=self.config.NMS_THRESHOLD)
        rbboxes = np_methods.bboxes_resize(rbbox_img, rbboxes)

        print("rbboxes:")
        print(rbboxes)

        return self.crop(img, rbboxes)  # np.array of 'RGB' format

    def crop(self, img, rbboxes):
        if len(rbboxes) == 1:
            # cast the bounding box coordinate into integer
            bbox = np.array(rbboxes[0])
            bbox[0] *= img.shape[0]  # y_min
            bbox[1] *= img.shape[1]  # x_min
            bbox[2] *= img.shape[0]  # y_max
            bbox[3] *= img.shape[1]  # x_max
            bbox = bbox.astype(np.int32)
            return img[bbox[0]:bbox[2], bbox[1]:bbox[3]]
        else:
            return img


if __name__ == '__main__':

    MODEL_PATH = "/home/doggie/lab/DoggieRobot/framework/src/Detector/Python/ssd_person_detector.pb"
    IMG_DIR = "/home/doggie/camp/dataset/query/bg"
    OUTPUT_DIR = "/home/doggie/camp/dataset/query/bg-ssd"

    # init
    ssd = SSD_model(MODEL_PATH)
    for i in os.listdir(IMG_DIR):
        img_path = os.path.join(IMG_DIR, i)
        img = mpimg.imread(img_path)
