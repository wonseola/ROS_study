# ROS_study
<br><br>
<details>
<summary><h3>05.02</h3></summary>

#### 리눅스 설치, ros 설치
[ROS](http://wiki.ros.org/noetic/Installation/Ubuntu) <br>
[Ubuntu 20.04.6](https://releases.ubuntu.com/focal/)
</details>

<details open>
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
    
    ```
      cd ~/catkin_ws/src 
      catkin_init_workspace 
    ```
    
    
  </details>
  

catkin_create_pkg topic_tutorial roscpp rospy std_msgs <br>
패키지 생성 <br><br>

(파일 생성위치)<br>
catkin_ws/src/"패키지"/src
<br><br>
roscore <br>
마스터 on
<br><br>
rosrun "패키지이름" "node이름"
<br><br>

</details>



