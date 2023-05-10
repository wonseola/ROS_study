#!/usr/bin/python
#-*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String

#콜백
def msgCallback(msg):
	rospy.loginfo("msg : %s" ,msg.data)

def listener():
	rospy.init_node("py_subscriber") #노드 이름 초기화
	rospy.Subscriber("my_topic", String, msgCallback, queue_size=100)
	#서브스크라이버 생성
	#패키지(std_msgs) 메세지(String) 서브스크라이버
	#토픽(my_topic) 서브스크라이버 큐사이즈(100)
	#콜백함수(msgCallback)
	
	rospy.spin() #수신 대기

if __name__ == "__main__":
	listener() 
