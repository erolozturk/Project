#!/usr/bin/env python

#roslaunch openni_launch openni.launch
#points 1280*720=921600 elemanli bir listedir

from __future__ import print_function
import sys
import rospy
from sensor_msgs.msg import PointCloud2
from sensor_msgs import point_cloud2 as pc2

class point_test:
   def callback(self, point_cloud):
      points = list(pc2.read_points(point_cloud))
      print (points[461440])

   def __init__(self):
      self.point_cloud_sub = rospy.Subscriber("/zed/point_cloud/cloud_registered",PointCloud2,self.callback,queue_size=2) 
def main(args):
   pt = point_test()
   rospy.init_node('get_point_test', anonymous=True)
   try:
      rospy.spin()
   except KeyboardInterrupt:
      print("Shutting down")

if __name__ == '__main__':
   main(sys.argv)
