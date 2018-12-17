#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import PoseStamped

def talker():
     rospy.init_node('talker', anonymous=True)
     rate = rospy.Rate(10) # 
     while not rospy.is_shutdown():
        pub = rospy.Publisher('/move_base_simple/goal', PoseStamped, queue_size=10)
        msg=PoseStamped()
        msg.header.frame_id="map"
        msg.header.stamp=rospy.Time.now()
        msg.pose.position.x = -4.00430250168
        msg.pose.position.y = -0.984996318817
        msg.pose.orientation.w = -0.0129763088404
        rospy.loginfo(msg)
        pub.publish(msg)
        rate.sleep()
 
#publisherde bunlar sabit
if __name__ == '__main__':
     try:
         talker()
     except rospy.ROSInterruptException:
         pass
