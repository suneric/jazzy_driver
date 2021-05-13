import rospy
from geometry_msgs.msg import Twist
import time
from dual_g2_hpmd_rpi import motors, MAX_SPEED
import math


class DriverFault(Exception):
    def __init__(self, driver_num):
        self.driver_num = driver_num

def raiseIfFault():
    if motors.motor1.getFault():
        raise DriverFault(1)
    if motors.motor2.getFault():
        raise DriverFault(2)

class JazzyLowLevelControl:
    def __init__(self):
        rospy.loginfo("Setting Up the Node")
        rospy.init_node("Jazzy ROS Interface", anonymous=True)
        self.twist_sub = rospy.Subscriber("/cmd_vel", Twist, self.set_motors_cmd)
        rospy.loginfo("> Subscriber Correctly Initilized")
        rospy.loginfo("Initialization Complete")

    def set_motors_cmd(self,msg):
        s1,s2 = self.motor_linear_speed(msg.linear.x)
        motors.setSpeeds(s1,s2)
        raiseIfFault()
        time.sleep(0.002)
        s1,s2 = self.motor_angular_speed(msg.angular.z)
        motors.setSpeeds(s1,s2)
        raiseIfFault()
        time.sleep(0.002)

    def motor_linear_speed(self,x):
        wheel_d = 0.2286 # m 9 # inch
        N = x*(60/(2*math.pi))/(wheel_d/2)
        print("linear speed", x, "m/s", int(N), "rpm")
        if N > MAX_SPEED:
            N = MAX_SPEED
        if N < -MAX_SPEED:
            N = -MAX_SPEED
        return int(N), int(N)

    def motor_angular_speed(self,z):
        wheel_d = 0.2286 # m
        t_rad = 0.6287 # m
        N = z*t_rad*(60/(2*math.pi))/(wheel_d/2)
        print("angular speed",z, "rad/s", int(N), "rpm")
        if N > MAX_SPEED:
            N = MAX_SPEED
        if N < -MAX_SPEED:
            N = -MAX_SPEED
        return -int(N), int(N)

    def run(self):
        rate = rospy.Rate(10)
        try:
            while not rospy.is_shutdown():
                rate.sleep()
        except rospy.ROSInterruptException:
            motors.forceStop()
            pass

if __name__ == '__main__':
    controller = JazzyLowLevelControl()
    controller.run()
