#include "ros/ros.h"
#include "service_tutorial/AddTwoInts.h"

bool add(service_tutorial::AddTwoInts::Request& req, service_tutorial::AddTwoInts::Response& res){
    res.result = req.a + req.b;
    ROS_INFO("request : a = %d , b = %d", req.a, req.b);
    ROS_INFO("response : result = %d", res.result);
    return true;
}

int main(int argc, char** argv){
    ros::init(argc, argv, "my_server");
    ros::NodeHandle nh;
    ros::ServiceServer my_server = nh.advertiseService("add_two_ints",add);
    ROS_INFO("Service server ready.");
    ros::spin();


    return 0;
}
