# Setup

## ROS-network
1. [set a static IP on raspberry pi](https://linuxhint.com/raspberry_pi_static_ip_setup/)
  - edit the configuration file /etc/dhcpcd.conf
  ```
  sudo vim /etc/dhcpcd.conf
  ```
  go to the end of the file and add following lines
  ```
  interface eth0 [or wlan0]
  static ip_address=192.168.1.19/24
  static routers=192.168.1.1
  static domain_name_servers=192.168.1.1 1.1.1.1 8.8.8.8
  ```
  - reboot
  - check your ip address
  ```
  ip addr show eth0 [or wlan0]
  ```

2. set ROS master on raspberry pi
  open ~/.bashrc
  ```
  export ROS_MASTER_URI=http://ubuntu-Aurora-R7:11311
  export ROS_HOSTNAME=driver-raspi
  ```
3. add hostname to /etc/hosts
```
127.0.1.1 driver-raspi
192.168.1.7 ubuntu-Aurora-R7
```

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
    Wants=network-online.target
    After=network.target network-online.target

    [Service]
    Type=simple
    User=pi
    Group=pi
    ExecStart=/home/pi/catkin_ws/src/jazzy_driver/auto_start.sh

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
