from DataSet import *
from InceptionV3Extractor import *
from ResNet50Extractor import *
from SimilarCluster import *
from SimilarClusterV2 import *


"""
convert the gallery
"""

G_DIR = '/home/doggie/camp/dataset/test'
MODEL_PATH = '/home/doggie/camp/deploy/model/InceptionV3_ft.pb'
NPY_PATH = '/home/doggie/camp/deploy/features/features_test.npy'

g_set = DataSet(G_DIR)
icp_v3_config = InceptionV3Config()
icp_v3_extractor = InceptionV3Extractor(icp_v3_config, MODEL_PATH)

imgs = g_set.get_img_path_list()
features = icp_v3_extractor.extract_features(imgs, save_features=True, features_path=NPY_PATH)


"""
convert the queries
"""

# Q_DIR = '/home/doggie/camp/dataset/query/bg-ssd'
# MODEL_PATH = '/home/doggie/camp/numbpie/models/InceptionV3.pb'
# NPY_PATH = '/home/doggie/camp/features/ssd/features_q.npy'
#
# q_set = DataSet(Q_DIR)
# icp_v3_config = InceptionV3Config()
# icp_v3_extractor = InceptionV3Extractor(icp_v3_config, MODEL_PATH)
#
# imgs = q_set.get_img_path_list()
# features = icp_v3_extractor.extract_features(imgs, save_features=True, features_path=NPY_PATH)


"""
similar clusters
"""

# Q_FEATURES = '/home/doggie/camp/features/ssd/features_q.npy'
# G_FEATURES = '/home/doggie/camp/deploy/features_g.npy'
# Q_DIR = '/home/doggie/camp/dataset/query/bg-ssd'
# G_DIR = '/home/doggie/camp/dataset/validation'
# JSON_PATH = '/home/doggie/camp/dataset/json/fashion_all/validation.json'
# CLUSTER_DIR = '/home/doggie/camp/cluster/ssd'
#
# q_set = DataSet(Q_DIR)
# g_set = DataSet(G_DIR)
# q_imgs = q_set.get_img_path_list()
# g_imgs = g_set.get_img_path_list()
# sc = SimilarCluster(q_imgs, g_imgs, Q_FEATURES, G_FEATURES, JSON_PATH)
# sc.visualize(CLUSTER_DIR, num_display=100)

# sc.search(CLUSTER_DIR)


"""
ResNet-50
"""

# G_DIR = '/home/doggie/camp/dataset/test'
# WEIGHTS_PATH = '/home/doggie/camp/src/models/model_10_final.pth.tar'
# NPY_PATH = '/home/doggie/camp/features/res-50/features_g.npy'
#
# g_set = DataSet(G_DIR)
# res_50_config = ResNet50Config()
# res_50_extractor = ResNet50Extractor(res_50_config, WEIGHTS_PATH)
#
# imgs = g_set.get_img_path_list()
# features = res_50_extractor.extract_features(imgs, save_features=True, features_path=NPY_PATH)


# Q_DIR = '/home/doggie/camp/dataset/query/bg'
# WEIGHTS_PATH = '/home/doggie/camp/src/models/model_10_final.pth.tar'
# NPY_PATH = '/home/doggie/camp/features/res-50/features_q3.npy'
#
# q_set = DataSet(Q_DIR)
# res_50_config = ResNet50Config()
# res_50_extractor = ResNet50Extractor(res_50_config, WEIGHTS_PATH)
#
# imgs = q_set.get_img_path_list()
# features = res_50_extractor.extract_features(imgs, save_features=True, features_path=NPY_PATH)



"""
similar clusters V2
"""

# Q_FEATURES = '/home/doggie/camp/features/res-50/features_q1.npy'
# G_FEATURES = '/home/doggie/camp/features/res-50/features_g.npy'
# Q_DIR = '/home/doggie/camp/dataset/query/pure'
# G_DIR = '/home/doggie/camp/dataset/test'
# CLUSTER_DIR = '/home/doggie/camp/cluster/res-50/pure'
#
# q_set = DataSet(Q_DIR)
# g_set = DataSet(G_DIR)
# q_imgs = q_set.get_img_path_list()
# g_imgs = g_set.get_img_path_list()
# sc = SimilarClusterV2(q_imgs, g_imgs, Q_FEATURES, G_FEATURES)
# sc.visualize(CLUSTER_DIR, num_display=100)
