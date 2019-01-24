from PIL import Image
import os

from fashion_gan.src.gans import Modifier
from fashion_gan.src.features import AkiwiFeatureGenerator, ResnetFeatureGenerator
from fashion_gan.src.search import Search, CombinedSearch

from fashion_gan.src.pipeline import FashionGANApp


class FashionGANWrapper:

    def __init__(self):

        folder_gens = {'akiwi_50': AkiwiFeatureGenerator(50),
                       'resnet': ResnetFeatureGenerator()}

        dress_imgs = '/home/doggie/camp/deploy/code/fashion_gan/data/images/fashion/dresses/'
        model_imgs = '/home/doggie/camp/deploy/code/fashion_gan/data/images/fashion_models/dresses_clustered/'

        dress_feats = '/home/doggie/camp/deploy/code/fashion_gan/data/features/fashion/dresses/'
        model_feats = '/home/doggie/camp/deploy/code/fashion_gan/data/features/fashion_models/dresses/'

        dress_search = {}
        for dir_name, gen in folder_gens.items():
            dress_search[dir_name] = Search(dress_imgs,
                                            os.path.join(dress_feats, dir_name),
                                            gen)

        model_search = {}
        for dir_name, gen in folder_gens.items():
            model_search[dir_name] = Search(model_imgs,
                                            os.path.join(model_feats, dir_name),
                                            gen)

        # combined search
        dress_resnet50 = CombinedSearch(
            [dress_search['akiwi_50'], dress_search['resnet']], factors=[2, 1])
        model_resnet50 = CombinedSearch(
            [model_search['akiwi_50'], model_search['resnet']], factors=[2, 1])

        modifier = Modifier('/home/doggie/camp/deploy/code/fashion_gan/data/models/')
        self.app = FashionGANApp(modifier, dress_resnet50, model_resnet50)

    def generate(self, img, attr):

        img_gan_1 = self.app._modifier.modify_shape(img, attr[0], attr[1])
        img_gan_2 = self.app._modifier.modify_pattern(img_gan_1, attr[2], attr[3])
        img_gan_3 = self.app._modifier.product_to_model(img_gan_2)

        return img_gan_3


if __name__ == '__main__':

    IMG_PATH = '/home/doggie/camp/dataset/validation/3'
    ATTR = ['fit', 'normal', 'floral', 'add']
    img = Image.open(IMG_PATH)
    fashion_gan_wrapper = FashionGANWrapper()
    img_gan = fashion_gan_wrapper.generate(img, ATTR)
    img_gan.save('/home/doggie/3.jpg')
