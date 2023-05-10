#include "ros/ros.h"
#include "param_tutorial/Calculate.h"
#include "cstdlib"

int main(int argc, char** argv){
    ros::init(argc, argv, "calculate");
    if(argc != 3){
        ROS_INFO("rosrun param_tutorial calculate_c a b");
        ROS_INFO("a , b : int32");
        return 1;
    }
    ros::NodeHandle nh;
    ros::ServiceClient client = nh.serviceClient<param_tutorial::Calculate>("calculate");
    param_tutorial::Calculate srv;
    srv.request.a = atoi(argv[1]);
    srv.request.b = atoi(argv[2]);
    if(client.call(srv)){
        ROS_INFO("a : %d, b : %d \t result : %d", srv.request.a, srv.request.b, srv.response.result);
    }
    else{
        ROS_ERROR("Failed to call service");
        return 1;
    }

    return 0;
}