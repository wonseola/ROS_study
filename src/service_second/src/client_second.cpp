#include "ros/ros.h"
#include "service_tutorial/AddTwoInts.h"
#include <cstdlib>

int main(int argc, char** argv){
    ros::init(argc, argv, "client_second");
    
    if(argc!=3){
        ROS_INFO("command : rosrum service_second client_second arg1 arg2");
        ROS_INFO("arg1, arg2 = int32");
        return 1;
    }
    ros::NodeHandle nh;
    ros::ServiceClient client = nh.serviceClient<service_tutorial::AddTwoInts>("mul_two_ints");
    service_tutorial::AddTwoInts srv;
    srv.request.a = atoi(argv[1]);
    srv.request.b = atoi(argv[2]);

    if(client.call(srv)){
        ROS_INFO("request : a = %d, b = %d",srv.request.a, srv.request.b);
        ROS_INFO("response : result = %d",srv.response.result);
    }
    else{
        ROS_ERROR("Failed to call service");
        return 1;
    }
    return 0;
}