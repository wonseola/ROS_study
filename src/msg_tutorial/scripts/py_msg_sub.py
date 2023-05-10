#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from msg_tutorial.msg import MyMsg

def msgCallback(msg):
    rospy.loginfo("receive msg : %d , %d", msg.stamp.secs, msg.stamp.nsecs)
    rospy.loginfo("receive msg : %d",msg.data)
    
if __name__ == "__main__":
    rospy.init_node("py_msg_sub")
    rospy.Subscriber("aa", MyMsg, msgCallback, queue_size=10)
    rospy.spin()