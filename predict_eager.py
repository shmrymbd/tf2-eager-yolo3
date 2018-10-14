# -*- coding: utf-8 -*-

import tensorflow as tf
import matplotlib.pyplot as plt
tf.enable_eager_execution()
from yolo.post_proc.decoder import postprocess_ouput
from yolo.post_proc.box import draw_boxes
from yolo.net.yolonet import Yolonet, preprocess_input
from yolo import RACCOON_ANCHORS

WEIGHTS_FNAME = "weights.h5"


if __name__ == '__main__':
    import os
    from yolo import PROJECT_ROOT
    import cv2
    net_size = 288
    image_path = os.path.join(PROJECT_ROOT, "samples", "imgs", "raccoon-1.jpg")
    image_path = os.path.join(PROJECT_ROOT, "samples", "imgs", "raccoon-12.jpg")

    image = cv2.imread(image_path)
    image = image[:,:,::-1]
    image_h, image_w, _ = image.shape
    new_image = preprocess_input(image, net_size)

    # 2. create model
    model = Yolonet(n_classes=1)
    model.load_weights(WEIGHTS_FNAME)

    # 3. predict
    yolos = model.predict(new_image)
    boxes = postprocess_ouput(yolos, RACCOON_ANCHORS, net_size, image_h, image_w)
    
    # 4. draw detected boxes
    image = draw_boxes(image, boxes, labels=["ani"], obj_thresh=0.0)

    # 5. plot    
    plt.imshow(image)
    plt.show()





