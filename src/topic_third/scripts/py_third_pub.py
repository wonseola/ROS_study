#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32MultiArray

if __name__=="__main__":
    rospy.init_node("py_third_pub")
    pub = rospy.Publisher("multi_array", Int32MultiArray, queue_size=100)
    
    loop_rate = rospy.Rate(1)
    msg = Int32MultiArray()
    msg.data.append(0)
    
    while not rospy.is_shutdown():
        pub.publish(msg)
        msg.data.append(0)
        loop_rate.sleep()