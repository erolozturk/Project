#!/usr/bin/env python
import rospy
from ackermann_msgs.msg import AckermannDriveStamped
from sensor_msgs.msg import Joy

hiz=0.0
aci=0.0
def hareket(data):
	global hiz,aci
	data2=data
	hiz=data2.axes[1]*255
    
	aci=data2.axes[3]*30
	print aci,hiz

def abone():
    global hiz,aci
    pub = rospy.Publisher('Ackermann', AckermannDriveStamped, queue_size=10)
	
    rospy.init_node('ackerman_yayin_node', anonymous=True)
    rospy.Subscriber('joy',Joy, hareket)
    rate = rospy.Rate(10)  

    while not rospy.is_shutdown():
        msg=AckermannDriveStamped()	 
        msg.drive.speed=hiz 
        msg.drive.steering_angle=aci  
        pub.publish(msg)
        rate.sleep()
    	
    	 

if __name__ == '__main__':
    try:
        abone()
    except rospy.ROSInterruptException:
        pass



 













