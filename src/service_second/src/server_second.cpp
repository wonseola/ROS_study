#include "ros/ros.h"
#include "service_tutorial/AddTwoInts.h"

bool mul_two_ints(service_tutorial::AddTwoInts::Request& req, service_tutorial::AddTwoInts::Response& res){
    res.result = req.a * req.b;
    ROS_INFO("request : a = %d, b = %d", req.a, req.b);
    ROS_INFO("response : result = %d", res.result);
    return true;
}
int main(int argc, char** argv){
    ros::init(argc, argv, "server_second");
    ros::NodeHandle nh;
    ros::ServiceServer server = nh.advertiseService("mul_two_ints", mul_two_ints);
    ROS_INFO("Service server ready");
    ros::spin();
    return 0;
}