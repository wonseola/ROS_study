#!/usr/bin/python
#!-*- cording: utf-8 -*-

import rospy
from service_tutorial.srv import AddTwoInts, AddTwoIntsResponse

def mul_two_ints(req):
    result = req.a * req.b
    rospy.loginfo(f"a : {req.a} , b : {req.b} \t result : {result}")
    return AddTwoIntsResponse(result)

if __name__ =="__main__":
    rospy.init_node("py_server_sec")
    server = rospy.Service("mul_two_ints", AddTwoInts, mul_two_ints)
    rospy.loginfo("server ready")
    rospy.spin()