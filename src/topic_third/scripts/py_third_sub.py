#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int32MultiArray

def msgCallback(msg):
    print(msg.data)
    
if __name__ =="__main__":
    rospy.init_node("py_third_sub")
    rospy.Subscriber("multi_array", Int32MultiArray, msgCallback, queue_size=100)
    rospy.spin()
    