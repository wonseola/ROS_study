#include "ros/ros.h"
#include "msg_tutorial/MyMsg.h" //mymsg message header file. 빌드시 생성

void msgCallback(const msg_tutorial::MyMsg::ConstPtr& msg){
    ROS_INFO("receive msg : %d, %d",msg->stamp.sec, msg->stamp.nsec);
    ROS_INFO("receive msg : %d",msg->data);
}
int main(int argc, char** argv){
    ros::init(argc, argv, "msg_subscriber");
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("aaaa", 10, msgCallback);
    ros::spin();
    return 0;

}