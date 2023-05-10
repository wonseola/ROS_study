#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from yh_dual.msg import MyMsg

def cBack(msg):
    print(msg.stamp.secs)
    #print(msg.stamp.nsecs)

if __name__ == "__main__":
    rospy.init_node("yu_dual_time")
    rospy.Subscriber("yu_dual_topic", MyMsg, cBack, queue_size=10)
    rospy.spin()