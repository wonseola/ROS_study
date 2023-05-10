#include "ros/ros.h"
#include "std_msgs/Int32MultiArray.h"

void msgCallback(const std_msgs::Int32MultiArray::ConstPtr& msg){
    std::vector<int32_t> v = msg -> data;
    for(int i = 0; i < v.size(); i++){
        std::cout << v[i] << " ";
    }
    std::cout << std::endl;
}

int main(int argc, char** argv){
    ros::init(argc, argv, "third_sub");
    ros::NodeHandle nh;
    ros::Subscriber sub = nh.subscribe("multi_array", 100, msgCallback);
    ros::spin();

    return 0;
}
