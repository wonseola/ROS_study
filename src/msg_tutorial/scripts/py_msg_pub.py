#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from msg_tutorial.msg import MyMsg

if __name__ =="__main__":
    rospy.init_node("py_msg_pub")
    pub = rospy.Publisher("aa", MyMsg, queue_size=50)
    loop_rate = rospy.Rate(20)
    msg = MyMsg()
    msg.data=0
    
    while not rospy.is_shutdown():
        msg.stamp = rospy.Time.now()
        rospy.loginfo("send msg : %d, %d", msg.stamp.secs, msg.stamp.nsecs)
        rospy.loginfo("send msg : %d", msg.data)
        pub.publish(msg)
        msg.data += 1
        loop_rate.sleep()
        
