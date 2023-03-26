# Jazzy Elite ES Motor Driver for ROS

This is a python library for [Jazzy Elite ES](https://www.pridemobility.com/jazzy-power-chairs/jazzy-elite-es/) motor driver using [Pololu Dual G2 High-Power Motor Driver for Rasberry Pi](https://www.pololu.com/product/3754).


## Hardware
- Raspberry pi (OS: buster)
- Jazzy Elite ES mobile base
- Pololu Dual G2 High-Power Motor Driver 18v22 for Rasberry Pi

## Installation
Follow INSTALL_RASPBERRY_PI.md to install ROS melodic and pigpio

## Download this repo
```
cd ~/catkin_ws/src
git clone https://github.com/suneric/jazzy_driver.git
```
make two files executable
```
sudo chmod +x ./auto_start.sh
sudo chmod +x ./scripts/jazzy_ros_interface.py
```

## Setup
- Follow SETUP.md to setup the service

## Use and control on client machine
1. set ROS network on client machine
  open ~/.bashrc
  ```
  export ROS_MASTER_URI=http:/192.168.1.7:11311
  export ROS_HOSTNAME=raspberrypi
  ```
2. check /cmd_vel is available
```
  rostopic list
```
3. control with teleop-twist-keyboard
```
sudo apt install ros-[verion]-teleop-twist-keyboard
```
