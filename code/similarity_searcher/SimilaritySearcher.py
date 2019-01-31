import os
import numpy as np


class SimilaritySearcher:

    def __init__(self, img_dir, features_path, dst_dir, sim_dir, num_display=5):

        self.img_dir = img_dir
        self.dst_path = dst_dir
        self.sim_dir = sim_dir
        self.num_display = num_display
        assert os.path.exists(features_path)
        self.features_g = np.load(features_path)
        self.features_path = features_path
        self.img_list = os.listdir(img_dir)
        self.img_path_list = [os.path.join(img_dir, i) for i in os.listdir(img_dir)]

    def get_img_list(self):
        return self.img_list

    def get_img_path_list(self):
        return self.img_path_list

    def find_similar_idx(self, feature_q, top_k=20, clip_th=0.78):
        assert (len(feature_q.shape) == 2)
        assert feature_q.shape[0] == 1
        sim = feature_q.dot(self.features_g.T)
        top_idx = np.argsort(sim[0])[-top_k:]
        top_idx_clip = [top_idx[i] for i in range(top_k) if sim[0, top_idx[i]] >= clip_th or len(top_idx) < 5]  # select by similarity threshold
        sim_list = [sim[0, j] for j in top_idx_clip]
        self.save_sim(sim_list)
        return top_idx_clip[: self.num_display]

    def copy_img2dir(self, idx):
        for j in os.listdir(self.dst_path):
            img_del_path = os.path.join(self.dst_path, j)
            os.remove(img_del_path)
        for k, i in enumerate(idx[::-1]):
            img_path = self.img_path_list[i]
            dst_path = os.path.join(self.dst_path, 'rec' + str(k+1)+'.jpg')
            open(dst_path, 'wb').write(open(img_path, 'rb').read())

    def save_sim(self, sim_list):
        sim_print_list = sim_list[: self.num_display]
        for k, i in enumerate(sim_print_list[::-1]):
            txt_path = os.path.join(self.sim_dir, str(k+1)+'.txt')
            print(txt_path)
            f_w = open(txt_path, 'w')
            f_w.write(str(i))
            f_w.close()
