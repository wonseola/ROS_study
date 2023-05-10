#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from yh_difference.srv import YhDifference, YhDifferenceResponse

def aaa(req):
    if req.a > req.b:
        result = req.a - req.b
    else:
        result = req.b - req.a
    rospy.loginfo(f"a = {req.a} , b = {req.b} \t result = {result}")
    return YhDifferenceResponse(result)

if __name__ == "__main__":
    rospy.init_node("yh_dif_server")
    my_server = rospy.Service("yh_difference_service", YhDifference, aaa)
    rospy.loginfo("Service server ready.")
    rospy.spin()