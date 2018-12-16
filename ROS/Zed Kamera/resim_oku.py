#!/usr/bin/env python

#roslaunch zed_wrapper zed.launch paketi calistirilmasi gerekir
#/zed/left/image_raw_color      sol kamera renk duzeltilmemis goruntu
#/zed/left/image_rect_color     sol kamera renk duzeltilmis goruntu
#/zed/right/image_raw_color     sag kamera renk duzeltilmemis goruntu
#/zed/right/image_rect_color    sag kamera renk duzeltilmis goruntu
#/zed/depth/depth_registered    derinlik goruntusu

import numpy as np
import cv2
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError


def callback(image_msg):
    global image_np
    bridge = CvBridge()
    try:
        image_np = bridge.imgmsg_to_cv2(image_msg)
    except CvBridgeError as e:
      print(e)

rospy.init_node('image',anonymous=True)
rospy.Subscriber('/zed/left/image_raw_color',Image ,callback)

while not rospy.is_shutdown():
    try:
        cv2.imshow("frame", image_np)
        if cv2.waitKey(25) & 0xFF == 27:
            cv2.destroyAllWindows()
            break
    except:
        pass
