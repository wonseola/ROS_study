#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from yh_dual.msg import MyMsg

if __name__ =="__main__":
    rospy.init_node("yu_dual_pub")
    pub = rospy.Publisher("yu_dual_topic", MyMsg, queue_size=50)
    loop_rate = rospy.Rate(8)
    msg = MyMsg()
    msg.data=0
    
    while not rospy.is_shutdown():
        msg.stamp = rospy.Time.now()
        pub.publish(msg)
        msg.data += 1
        loop_rate.sleep()