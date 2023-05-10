#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int64

def cBack(msg):
	rospy.loginfo("%d" ,msg.data)

if __name__ == "__main__":
	rospy.init_node("my_test_sub")
	rospy.Subscriber("a", Int64, cBack, queue_size=10)
	rospy.spin()