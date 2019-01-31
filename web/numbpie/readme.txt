上传图片后
  if checked labels: #用gan
    (select features & 提交)
    "true" > static/gan/checked.txt
    选中的feature > static/gan/feature.txt
    选中的texture > static/gan/texture.txt
    选中的action > static/gan/action.txt
    ---------------------------------------
    model返回  3张 gan info images (1.jpg, 2.jpg, 3.jpg) > static/gan_info_img
              5张 rec images (rec1.jpg, rec2.jpg, rec3.jpg, rec4.jpg, rec5.jpg) > static/rec_images
              5个 rec accuracy (1.txt, 2.txt, 3.txt, 4.txt, 5.txt) > static/rec_accuracy
    ---------------------------------------
    前端显示

  else:  #不用gan
    (直接提交)
    "false" > static/gan/checked.txt
    剩下三个gan/*.txt不会更新不过你们看到false就知道不用gan了
    ---------------------------------------
    model返回  5张 rec images (rec1.jpg, rec2.jpg, rec3.jpg, rec4.jpg, rec5.jpg) > static/rec_images
              5个 rec accuracy (1.txt, 2.txt, 3.txt, 4.txt, 5.txt) > static/rec_accuracy
    ---------------------------------------
    前端显示
