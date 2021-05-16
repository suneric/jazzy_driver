# Jazzy Elite ES Motor Driver for ROS

This is a python library for [Jazzy Elite ES](https://www.pridemobility.com/jazzy-power-chairs/jazzy-elite-es/) motor driver using [Pololu Dual G2 High-Power Motor Driver for Rasberry Pi](https://www.pololu.com/product/3754).

## Depedencies
- Hardware
  - Jazzy Elite ES mobile base
  - Pololu Dual G2 High-Power Motor Driver 18v22 for Rasberry Pi
- Software
  - Python 2.7
  - [ROS Melodic on Rasberry Pi](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi)
  - [Pololu dual-g2-high-power-motor-driver-rpi](https://github.com/pololu/dual-g2-high-power-motor-driver-rpi)
    - [pigpio](http://abyz.me.uk/rpi/pigpio/)


## Installation (on raspberry pi)
- install ros [melodic]
- install pigpio
```
sudo apt install python-pigpio
```
- start pigpiod daemon
```
sudo systemctl start pigpiod
```
Optionally, to automatically start the daemon everytime your Rasberry Pi boots, you can run
```
sudo systemctl enable pigpiod
```

## Download this repo to raspberry pi
```
git clone https://github.com/suneric/jazzy_driver.git
```
make two files executable
```
sudo chmod +x ./auto_start.sh
sudo chmod +x ./scripts/jazzy_ros_interface.py
```


## ROS-network
1. set ROS master on raspberry pi
  open ~/.bashrc
    export ROS_MASTER_URI=http://192.168.1.19:11311
    export ROS_IP=192.168.1.19
2. use ROS master on client machile
  open ~/.bashrc
  export ROS_MASTER_URI=http:/192.168.1.19:11311
  export ROS_IP=192.168.1.171


## create boot script for raspberry pi using [systemd](https://magiccvs.byu.edu/wiki/#!computers/systemd.md)
- add a systemd service
  1. cd /etc/systemd/system
  2. create a file named jazzy-service.service
    ```
    sudo touch jazzy-service.service
    sudo vim jazzy-service.service
    ```
    and include the following:
    ```
    [Unit]
    Description="Jazzy ROS start"
    After=network-online.target

    [Service]
    Type=simple
    User=pi
    Group=pi
    ExecStart=/home/ros_catkin_ws/src/jazzy_driver/auto_start.sh

    [Install]
    WantedBy=default.target
    ```
    then save and quit (:qw!)
- Before booting, test the service with
  ```
  sudo systemctl start jazzy-service
  ```
  check if it is running or failed with
  ```
  sudo systemctl status jazzy-service
  ```
- make sure to install the service with
  ```
  sudo systemctl enable jazzy-service
  ```
