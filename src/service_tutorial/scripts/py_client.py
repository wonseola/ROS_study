#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from service_tutorial.srv import AddTwoInts
import sys

if __name__=="__main__":
    rospy.init_node("py_client")
    
    if len(sys.argv)!=3:
        rospy.loginfo("rosrun service_tutorial py_client.py a b")
        rospy.loginfo("a, b = int32")
        sys.exit(1)
    
    rospy.wait_for_service("add_two_ints")
    try:
        my_client = rospy.ServiceProxy("add_two_ints", AddTwoInts)
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        response = my_client(a, b)
    except rospy.ServiceException as e:
        rospy.logerr("Service call failed : %s",e)
    else:
        rospy.loginfo("reequest : a = %d , b = %d", a, b)
        rospy.loginfo("response : result = %d ",response.result)
            