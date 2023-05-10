#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import Int64

if __name__ == "__main__":
    rospy.init_node("my_test_pub")
    pub = rospy.Publisher("a", Int64,queue_size=10)
    loop_rate = rospy.Rate(5)
    msg=Int64()
    msg.data=0
    while not rospy.is_shutdown():
        pub.publish(msg)
        loop_rate.sleep()
        msg.data+=1
        if(msg.data==16): msg.data=0