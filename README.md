# ROS_study
<br><br>
<details>
<summary><h3>05.02</h3></summary>

#### 리눅스 설치, ros 설치
[ROS](http://wiki.ros.org/noetic/Installation/Ubuntu) <br>
[Ubuntu 20.04.6](https://releases.ubuntu.com/focal/)
</details>

<details>
<summary><h3>05.03</h3></summary>

|리눅스 명령어|?|
|---|---|
|touch "파일명"|파일생성|
|gedit "파일명"|gedit 으로 열기|
|cat "파일명"|내용 출력|
|cp "기존파일" "새파일명"|복사|
|mkdir "폴더명" |폴더생성|
|mv "파일명" "폴더명"|파일을 폴더로 옮김|
|mv "파일명" "새 파일명"|파일 이름 변경|
|rm "파일명"|삭제|
|rmdir "폴더명|디렉토리 삭제|

<br><br>

|ROS용어|?|
|---|---|
|Node|실행 가능 프로세서|
|Package|하나 이상 노드,노드실행 정보 묶음|
|Message|노드간 데이터|
|Master|노드간 통신 관리|

<br><br>

#### 통신
Topic (관련 자료만 통신) <br>
Publisher (보내기)<br>
Subscriber (받기) <br><br>

service client (요청)<br>
sevice server (응답)<br>
action client ,server<br>

<br><br>
#### catkin
  
  <details>
    <summary> catkin </summary>
워크스페이스 <br>
    
   ```
      mkdir ~/catkin_ws/src
   ```
    
src 에 CMakeLists
    

      cd ~/catkin_ws/src 
      catkin_init_workspace 
      catkin_make

 setup.bash 를 bashrc에 추가함..(창 열릴때마다 실행되게 ~)
      
      gedit ~/.bashrc
      source ~/catkin_ws/devel/setup.bash
    
  </details>
  
패키지 생성 <br>
    ```
      catkin_create_pkg topic_tutorial roscpp rospy std_msgs 
    ```

파일 생성... 위치  <br>
    ```
      catkin_ws/src/"패키지"/src 
    ```

      
빌드  <br>
    ```
      cd ~/catkin_ws && catkin_make 
    ```

      

    
<details>
  <summary>CMakeLists 수정 </summary>
  
  ```
    add_executable(my_publisher src/my_publisher.cpp)
    add_executable(my_subscriber src/my_subscriber.cpp)
    add_dependencies(my_publisher ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
    add_dependencies(my_subscriber ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})
    target_link_libraries(my_publisher   ${catkin_LIBRARIES} )
    target_link_libraries(my_subscriber   ${catkin_LIBRARIES} )
  ```

</details>

<br>
    
    
마스터 on<br>
    ```
      roscore 
    ```

실행<br>
    ```
      rosrun "패키지이름" "node이름"
     ```
     
<br><br>


    


</details>

<details>
<summary><h3>05.08</h3></summary>

http://wiki.ros.org/msg

rosnode list // 켜져있는 노드 확인 <br>
rosnode info "노드이름" // 노드 정보  <br>
rostopic list //토픽 확인 <br>
rostopic info "토픽이름" // 토픽 정보 <br>
rostopic echo "토픽이름" // sub 출력 <br>
rostopic pub "토픽이름" // pub 출력 <br>

</details>

<details>
<summary><h3>05.09</h3></summary>
   <br>
rosparam list <br>
rosparam get "파라미터 이름" <br>
rosparam set "파라미터 이름" "변경값" <br>

  
</details>


<details>
<summary><h3>05.10</h3></summary>
   <br>

rosrun turtlesim turtoesim_node <br>

  
</details>
