#include "ros/ros.h"
#include "msg_tutorial/MyMsg.h" //mymsg message header file. 빌드시 생성

int main(int argc, char** argv){
    ros::init(argc, argv, "msg_publisher");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<msg_tutorial::MyMsg>("aaaa",10);
    ros::Rate loop_rate(10);
    msg_tutorial::MyMsg msg;
    msg.data = 0;
    while(ros::ok()){
        msg.stamp = ros::Time::now();
        ROS_INFO("send msg :%d , %d", msg.stamp.sec, msg.stamp.nsec);
        ROS_INFO("send msg : %d", msg.data);
        pub.publish(msg);
        msg.data++;
        loop_rate.sleep();
    }
    return 0;
}