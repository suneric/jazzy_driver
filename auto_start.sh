#!usr/bin/env bash
aplay /home/pi/ros_catkin_ws/src/jazzy_driver/sound/heart_beat.wav

export ROS_MASTER_URI=http://192.168.1.19:11311
export ROS_IP=192.168.1.19

source ~/ros_catkin_ws/devel_isolated/setup.bash
source ~/catkin_ws/devel/setup.bash
roslaunch jazzy_driver jazzy_ros.launch
