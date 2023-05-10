#include "ros/ros.h"
#include "std_msgs/String.h"
//콜백함수
void msgCallback(const std_msgs::String::ConstPtr& msg){
	ROS_INFO("msg : %s",msg->data.c_str());
}

int main(int argc, char** argv){
	ros::init (argc, argv, "my_subscriber");//노드이름 초기화
	ros::NodeHandle nh;//핸들
	
	//서브스크라이버 선언
	//패키지(std_msgs)의 메세지(String)를 이용한 서브스크라이버(sub) 선언
	//토픽(my_topic) subsctiber큐 사이즈(100)
	//콜백함수(msgCallback)
	
	ros::Subscriber sub = nh.subscribe("my_topic",100,msgCallback);
	
	//콜백 함수 호출 함수. 메세지 수신 대기
	//수신 되면 콜백함수 호출
	ros::spin();
	
	return 0;
}
