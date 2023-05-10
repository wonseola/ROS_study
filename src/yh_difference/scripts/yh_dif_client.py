#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from yh_difference.srv import YhDifference
import sys

if __name__=="__main__":
    rospy.init_node("yh_dif_client")
    
    if len(sys.argv)!=3:
        rospy.loginfo("a, b = int32")
        sys.exit(1)
    
    rospy.wait_for_service("yh_difference_service")
    try:
        my_client = rospy.ServiceProxy("yh_difference_service", YhDifference)
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        response = my_client(a, b)
        rospy.loginfo(f"a = {a} , b = {b} \t result = {response.result}")
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed : %s",e)

            