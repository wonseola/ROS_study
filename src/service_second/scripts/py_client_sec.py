#!/usr/bin/python
#!-*- cording: utf-8 -*-

import rospy
from service_tutorial.srv import AddTwoInts, AddTwoIntsRequest
import sys

if __name__=="__main__":
    rospy.init_node("py_clientsec")
    if len(sys.argv)!=3:
        rospy.loginfo("int32")
        sys.exit(1)
        
    client = rospy.ServiceProxy("mul_two_ints", AddTwoInts)
    
    req = AddTwoIntsRequest()
    req.a = int(sys.argv[1])
    req.b = int(sys.argv[2])
    
    try:
        res=client(req)
        rospy.loginfo(f"a : {req.a} , b : {req.b} \t result : {res.result}")
    except rospy.ServiceException as e:
        rospy.logerr(f"Failed : {e}")