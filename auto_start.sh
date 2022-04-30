#!usr/bin/env bash
export ROS_MASTER_URI=http://ubuntu-Aurora-R7:11311
export ROS_HOSTNAME=driver-raspi

source ~/ros_catkin_ws/devel_isolated/setup.bash
source ~/catkin_ws/devel/setup.bash

roslaunch jazzy_driver jazzy_driver_ros.launch
aplay /home/pi/catkin_ws/src/jazzy_driver/sound/heart_beat.wav
