import time
import matplotlib.image as mpimg
from fashion_gan.fashion_gan_wrapper import *
from ssd_detector.ssd_detector import *
from similarity_searcher.SimilaritySearcher import *
from feature_extractor.InceptionV3Extractor import *


class Config:
    SSD_MODEL_PATH = '/home/doggie/camp/deploy/model/ssd_person_detector.pb'
    EXTRACTOR_MODEL_PATH = '/home/doggie/camp/deploy/model/InceptionV3_ft.pb'
    GALLERY_DIR = '/home/doggie/camp/dataset/test'
    FEATURES_PATH = '/home/doggie/camp/deploy/features/features_test.npy'
    DST_DIR = '/home/doggie/camp/deploy/little_test/ans'
    SIM_DIR = '/home/doggie/camp/deploy/web/sim'


class Searcher:

    def __init__(self, config):

        self.config = config
        # self.fashion_gan_wrapper = FashionGANWrapper()
        self.ssd = SSD_model(config.SSD_MODEL_PATH)
        self.extractor = InceptionV3Extractor(InceptionV3Config(), config.EXTRACTOR_MODEL_PATH)
        self.s_searcher = SimilaritySearcher(config.GALLERY_DIR, config.FEATURES_PATH, config.DST_DIR, config.SIM_DIR)


if __name__ == '__main__':

    """
    test
    """

    # img_path = '/home/doggie/camp/deploy/little_test/query/20'
    QUERY_DIR = '/home/doggie/camp/deploy/little_test/query_0'
    searcher = Searcher(Config())

    for k, i in enumerate(os.listdir(QUERY_DIR)):
        img_path = os.path.join(QUERY_DIR, i)

        # SSD
        # img_ssd_output = searcher.ssd.detect(img_path)  # np.array of 'RGB' format
        # print(img_ssd_output.shape)
        # ssd_dst_path = os.path.join("/home/doggie/camp/deploy/little_test/ssd", i+'.jpg')
        # mpimg.imsave(ssd_dst_path, img_ssd_output)
        img_ssd_output = mpimg.imread(img_path)  # skip

        # GAN
        # ATTR = ['fit', 'loose', 'stripes', 'remove']
        # img_gan_input = Image.fromarray(img_ssd_output)
        # img_gan_output = searcher.fashion_gan_wrapper.generate(img_gan_input, ATTR)  # PIL image
        # print(img_gan_output)
        # gan_dst_path = os.path.join("/home/doggie/camp/deploy/little_test/gan", i+'.jpg')
        # img_gan_output.save(gan_dst_path)
        img_gan_output = Image.fromarray(img_ssd_output)  # skip

        # Extractor
        feature_q = searcher.extractor.extract_features(img_gan_output)  # [1, DIM]
        print(feature_q)
        print(feature_q.shape)

        # Search
        img_idx = searcher.s_searcher.find_similar_idx(feature_q, top_k=20, clip_th=0.70)
        searcher.s_searcher.copy_img2dir(img_idx)

    """
    run
    """

