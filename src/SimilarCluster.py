import os
import numpy as np


class SimilarCluster:

    def __init__(self, imgs_q, imgs_g, features_q, features_g, top_k=100):
        self.imgs_q = imgs_q
        self.imgs_g = imgs_g
        self.top_k = top_k
        if isinstance(features_q, str):
            self.features_q = np.load(features_q)
        else:
            self.features_q = features_q
        if isinstance(features_g, str):
            self.features_g = np.load(features_g)
        else:
            self.features_g = features_g
        assert (len(imgs_q) == self.features_q.shape[0])
        assert (len(imgs_g) == self.features_g.shape[0])
        self.sim = self.features_q.dot(self.features_g.T)
        self.num_queries = self.features_q.shape[0]
        self.num_gallery = self.features_g.shape[0]
        self.top_idx = np.array([np.argsort(self.sim[k])[-top_k:] for k in range(self.num_queries)])

    def visualize(self, cluster_dir, num_display=None):
        for k in range(self.num_queries):
            if num_display is not None and k >= num_display:
                break
            q_name = os.path.basename(self.imgs_q[k])
            dst_dir = os.path.join(cluster_dir, q_name)
            if not os.path.exists(dst_dir):
                os.makedirs(dst_dir)
            open(os.path.join(dst_dir, q_name), 'wb').write(open(self.imgs_q[k], 'rb').read())
            # choose top-k to display
            for i in range(self.top_k):
                img_idx = self.top_idx[k, -i - 1]
                img_src_path = self.imgs_g[img_idx]
                img_dst_path = os.path.join(dst_dir, str(i).zfill(4) + '_' + os.path.basename(img_src_path) + '_' + str(
                    self.sim[k, img_idx]))
                open(img_dst_path, 'wb').write(open(img_src_path, 'rb').read())
