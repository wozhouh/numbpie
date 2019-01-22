import os


class DataSet:
    def __init__(self, img_dir):
        self.img_dir = img_dir
        self.img_list = os.listdir(img_dir)
        self.img_path_list = [os.path.join(img_dir, i) for i in os.listdir(img_dir)]

    def get_img_list(self):
        return self.img_list

    def get_img_path_list(self):
        return self.img_path_list
