# Installation on Raspberry Pi

## Install ROS Melodic
Follow the [tutorial](http://wiki.ros.org/ROSberryPi/Installing%20ROS%20Melodic%20on%20the%20Raspberry%20Pi) to install ROS melodic (into ros_catkin_ws).
1. setup ROS repositories
```
$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'

$ sudo apt-key adv --keyserver hkp://ubuntu-keyservers.com:80 --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654

$ sudo apt-get update
$ sudo apt-get upgrade
```
2. install bootstrap dependencies
```
$ sudo apt install -y python-rosdep python-rosinstall-generator python-wstool python-rosinstall build-essential cmake
```
3. initializing rosdep
```
$ sudo rosdep init
$ rosdep update
```

4. Install ros melodic
4.1 create a caktin workspace
```
$ mkdir -p ~/ros_catkin_ws
$ cd ~/ros_catkin_ws
```
4.2 download ros_comm
```
$ rosinstall_generator ros_comm --rosdistro melodic --deps --wet-only --tar > melodic-ros_comm-wet.rosinstall
$ wstool init src melodic-ros_comm-wet.rosinstall

```
this will add all of the catkin or wet packages into the ~/ros_catkin_ws/src directory, in terms of using geometry_message, we need to update the [common_msgs](https://github.com/ros/common_msgs.git)
4.3 resolve dependencies
```
$ cd ~/ros_catkin_ws
$ rosdep install -y --from-paths src --ignore-src --rosdistro melodic -r --os=debian:buster
```  
4.4 build the catkin workspace
```
$ sudo ./src/catkin/bin/catkin_make_isolated --install -DCMAKE_BUILD_TYPE=Release --install-space /opt/ros/melodic

$ echo "source /opt/ros/melodic/setup.bash" >> ~/.bashrc
```

## Install pigpio driver
Follow the [tutorial](https://github.com/pololu/dual-g2-high-power-motor-driver-rpi) to install pigpio driver
```
sudo apt install python-pigpio
sudo systemctl start pigpiod
```
auto start the service when boot
```
sudo systemctl enable pigpoid
```
