#!usr/bin/env bash

export ROS_MASTER_URI=http://192.168.1.19:11311
export ROS_IP=192.168.1.19

source ~/ros_catkin_ws/devel/setup.bash
roslaunch jazzy_driver jazzy_driver_ros.launch

aplay ./sound/heart_beat.wav
