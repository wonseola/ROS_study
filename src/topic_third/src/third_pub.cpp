#include "ros/ros.h"
#include "std_msgs/Int32MultiArray.h"

int main(int argc, char** argv){
    ros::init(argc, argv, "third_pub");
    ros::NodeHandle nh;
    ros::Publisher pub = nh.advertise<std_msgs::Int32MultiArray>("multi_array",100);
    ros::Rate loop_rate(1);
    std_msgs::Int32MultiArray msg;
    msg.data.push_back(0);
    while(ros::ok()){
        pub.publish(msg);
        loop_rate.sleep();
        msg.data.push_back(0);
    }
    return 0;
}
