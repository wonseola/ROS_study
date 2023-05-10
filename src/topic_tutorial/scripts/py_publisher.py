#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

def talker():
	rospy.init_node("py_publisher") #노드 초기화
	pub = rospy.Publisher("my_topic", String, queue_size=100) #퍼블리셔 생성 
	#패키지(std_msgs) 메세지(String) 퍼블리셔(pub)
	#토픽(my_topic) 퍼블리셔큐 사이즈(100) 
	loop_rate = rospy.Rate(10)
	msg = String()
	msg.data = "Hi"
	
	while not rospy.is_shutdown():
		pub.publish(msg)
		loop_rate.sleep()
	
if __name__ == "__main__":
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
