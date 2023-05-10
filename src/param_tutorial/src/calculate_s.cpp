#include "ros/ros.h"
#include "param_tutorial/Calculate.h"

#define PLUS 1
#define MINUS 2
#define MUL 3
#define DIV 4

int my_operator = PLUS;
bool calculation(param_tutorial::Calculate::Request& req, param_tutorial::Calculate::Response& res){
    switch(my_operator){
        case PLUS:
            res.result = req.a + req.b;
            break;
        case MINUS:
            res.result = req.a - req.b;
            break;
        case MUL:
            res.result = req.a * req.b;
            break;
        case DIV:
            if(req.b==0){res.result=0;}
            else{res.result = req.a / req.b;}
            break;
        default:
            res.result = req.a + req.b;
            break;
    }
    ROS_INFO("a : %d , b : %d \t result : %d", req.a, req.b, res.result);
    return true;
}

int main(int argc, char** argv){
    ros::init(argc, argv, "calculate_s");
    ros::NodeHandle nh;

    //파라미터 서버에 있는 변수값 설정
    nh.setParam("calculation_method", PLUS); // 파라미터 값 초기 설정
    ros::Rate loop_rate(10);
    ros::ServiceServer server = nh.advertiseService("calculate", calculation);
    ROS_INFO("Calculate server ready");
    
    while(ros::ok()){
        nh.getParam("calculation_method", my_operator); // 파라미터 값 읽기
        ros::spinOnce();
        loop_rate.sleep();
    }

    return 0;
}