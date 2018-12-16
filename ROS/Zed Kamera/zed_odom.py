#!/usr/bin/env python
import numpy as np
import cv2
import math
import rospy
from nav_msgs.msg import Odometry

def zed_callback(data):
	hareket_x = data.pose.pose.position.x
	hareket_y = data.pose.pose.position.y
	hareket_z = data.pose.pose.position.z
	aci_x = data.pose.pose.orientation.x
	aci_y = data.pose.pose.orientation.y
	aci_z = data.pose.pose.orientation.z
	mesafe=math.sqrt(x**2+y**2)
	print "hareket mesafesi" + str(mesafe) + " metre"
	#zed kameranin x ve y eksenlerinde ne kadar hareket ettigini yazdirir

if __name__ == '__main__':
	rospy.init_node('zed_odom', anonymous=True)
	rospy.Subscriber('/zed/odom',Odometry,zed_callback,queue_size=1)
	rospy.spin()

