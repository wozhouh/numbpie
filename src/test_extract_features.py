import DataSet
import FeatureExtractor
import SimilarCluster


"""
convert the gallery
"""

# VAL_DIR = '/home/doggie/camp/dataset/validation'
# MODEL_PATH = '/home/doggie/camp/src/models/InceptionV3/classify_image_graph_def.pb'
# NPY_PATH = '/home/doggie/camp/src/temp/features_val.npy'
#
# val_set = DataSet.DataSet(VAL_DIR)
# icp_v3_config = FeatureExtractor.InceptionV3Config()
# icp_v3_extractor = FeatureExtractor.InceptionV3Extractor(icp_v3_config, MODEL_PATH)
#
# imgs = val_set.get_img_path_list()
# features = icp_v3_extractor.extract_features(imgs, save_features=True, features_path=NPY_PATH)


"""
convert the queries
"""

# Q_DIR = '/home/doggie/camp/dataset/self'
# MODEL_PATH = '/home/doggie/camp/src/models/InceptionV3/classify_image_graph_def.pb'
# NPY_PATH = '/home/doggie/camp/src/temp/features_q.npy'
#
# q_set = DataSet.DataSet(Q_DIR)
# icp_v3_config = FeatureExtractor.InceptionV3Config()
# icp_v3_extractor = FeatureExtractor.InceptionV3Extractor(icp_v3_config, MODEL_PATH)
#
# imgs = q_set.get_img_path_list()
# features = icp_v3_extractor.extract_features(imgs, save_features=True, features_path=NPY_PATH)


"""
similar clusters
"""

# Q_FEATURES = '/home/doggie/camp/src/temp/features_q.npy'
Q_FEATURES = '/home/doggie/camp/src/temp/features_val.npy'
G_FEATURES = '/home/doggie/camp/src/temp/features_val.npy'
# Q_DIR = '/home/doggie/camp/dataset/self'
Q_DIR = '/home/doggie/camp/dataset/validation'
G_DIR = '/home/doggie/camp/dataset/validation'
# CLUSTER_DIR = '/home/doggie/camp/retrieval/test_features/cluster/self'
CLUSTER_DIR = '/home/doggie/camp/retrieval/test_features/cluster/val'

q_set = DataSet.DataSet(Q_DIR)
g_set = DataSet.DataSet(G_DIR)
q_imgs = q_set.get_img_path_list()
g_imgs = g_set.get_img_path_list()
sc = SimilarCluster.SimilarCluster(q_imgs, g_imgs, Q_FEATURES, G_FEATURES)
sc.visualize(CLUSTER_DIR, num_display=100)
