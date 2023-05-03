#include "ros/ros.h" //ros
#include "std_msgs/String.h" //string message 

int main(int argc, char** argv){
	ros::init(argc, argv, "my_publisher"); //노드 이름 초기화
	ros::NodeHandle nh; // ros와 통신을 위한 핸들 선언
	
	//퍼블리셔 선언
	//패키지(std_msgs)의 메시지파일(String)을 이용한 퍼ㅡㄹ리셔(pub)를 만든다
	//토픽은(my_topic), 퍼블리셔큐(queue)사이즈는 (100)
	ros::Publisher pub = nh.advertise<std_msgs::String>("my_topic",100);
	
	ros::Rate loop_rate(10); //10Hz 루프 
	
	std_msgs::String msg;
	msg.data="Hello"; // msg 에 Hello 넣음
	
	while(ros::ok()){
		pub.publish(msg);
		loop_rate.sleep();	
	}
	return 0;
}
