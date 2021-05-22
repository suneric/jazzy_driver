# Installation on Raspberry Pi

## Install pigpio driver
Follow the [tutorial](https://github.com/pololu/dual-g2-high-power-motor-driver-rpi) to install pigpio driver
```
sudo apt install python-pigpio
sudo systemctl start pigpiod
sudo systemctl enable pigpoid
```

## Install ROS Melodic
Follow the [tutorial](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi) to install ROS melodic (into ros_catkin_ws).
To resolve ros package dependencies by running rosdep:
```
$ cd ~/ros_catkin_ws
$ rosdep install -y --from-paths src --ignore-src --rosdistro melodic -r --os=debian:buster
```
To build the catkin workspace (invoke catkin_make_isolated)
```
$ sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/melodic
```

## Install Realsense SDK
Follow the [tutorial](https://github.com/IntelRealSense/librealsense/blob/master/doc/installation_raspbian.md) to install realsense SDK. which will require OpenCV to be installed.
If the method of OpenCV installation in the tutorial does not work, build the OpenCV 3.4 by following the [tutorial](https://docs.opencv.org/3.4.14/d7/d9f/tutorial_linux_install.html)

## Install realsense-ros
Download the soruce code into ros_catkin_ws/src by running
```
cd ~/ros_catkin_ws/src
git clone https://github.com/IntelRealSense/realsense-ros.git
```
And build the catkin workspace
```
$ sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/melodic
```
