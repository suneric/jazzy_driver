"""
Raspberry Pi dual motor driver using Cytron MDDS30

Wiring:
--------------------------------------------------
MDDS30                  RPi
IN1                     gpio 5
IN2                     gpio 6
AIN1                    gpio 12
AIN2                    gpio 13
--------------------------------------------------

linzhank, 2022-03-25
"""
import RPi.GPIO as GPIO
_pin_M1DIR = 5
_pin_M2DIR = 6
_pin_M1PWM = 12  # hardware pwm 0: 12 or 18
_pin_M2PWM = 13  # hardware pwm 1: 13 or 19
MAX_SPEED = 100.0


class Motor(object):

    def __init__(self, pwm_pin, dir_pin):
        GPIO.setup(pwm_pin, GPIO.OUT)
        self.pwm_signal = GPIO.PWM(pwm_pin, 10000)  # frequency=10000Hz
        GPIO.setup(dir_pin, GPIO.OUT)
        self.pwm_pin = pwm_pin
        self.dir_pin = dir_pin

    def setSpeed(self, speed):
        if speed < 0:
            speed = -speed
            GPIO.output(self.dir_pin, GPIO.HIGH)
        else:
            GPIO.output(self.dir_pin, GPIO.LOW)
        if speed > MAX_SPEED:
            speed = MAX_SPEED
        self.pwm_signal.start(speed)

    def enable(self):
        pass

    def disable(self):
        self.pwm_signal.start(0)

    def getFault(self):
        pass


class Motors(object):

    def __init__(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        self.motor1 = Motor(_pin_M1PWM, _pin_M1DIR)
        self.motor2 = Motor(_pin_M2PWM, _pin_M2DIR)

    def setSpeeds(self, m1_speed, m2_speed):
        self.motor1.setSpeed(m1_speed)
        self.motor2.setSpeed(m2_speed)

    def enable(self):
        self.motor1.enable()
        self.motor2.enable()

    def disable(self):
        self.motor1.disable()
        self.motor2.disable()

    def getFaults(self):
        pass

    def forceStop(self):
        self.disable()


motors = Motors()
