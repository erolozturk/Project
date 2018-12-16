#!/usr/bin/env python
import numpy as np
import cv2
import math
import rospy

from sensor_msgs.msg import Image
from cv_bridge import CvBridge


if __name__ == '__main__':
	rospy.init_node('pycode', anonymous=True)
	rate = rospy.Rate(20)
	
	cam=cv2.VideoCapture(0)

	while not rospy.is_shutdown():
		ret,frame=cam.read()	
		if ret:   
			image_pub = rospy.Publisher("camera_raw",Image,queue_size=10)
			bridge = CvBridge()
			image_pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
			
			cv2.imshow("frame",frame)
			rate.sleep()
	
		if cv2.waitKey(1) & 0xFF ==27:
			break
	rospy.spin()
	cam.release()
	cv2.destroyAllWindows()
