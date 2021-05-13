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


## Installation
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

## Download
