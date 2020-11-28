import time
import traitlets
from traitlets.config.configurable import SingletonConfigurable
from Adafruit_MotorHAT import Adafruit_MotorHAT
from .motor import Motor
#TB_7

class Robot(SingletonConfigurable):
    
    left_motor = traitlets.Instance(Motor)
    left_motor2 = traitlets.Instance(Motor)
    right_motor = traitlets.Instance(Motor)
    right_motor2 = traitlets.Instance(Motor)

    # config
    i2c_bus = traitlets.Integer(default_value=1).tag(config=True)
    left_motor_channel = traitlets.Integer(default_value=1).tag(config=True)
    left_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    
    left_motor_channel2 = traitlets.Integer(default_value=3).tag(config=True)
    left_motor_alpha2 = traitlets.Float(default_value=1.0).tag(config=True)
    
    right_motor_channel = traitlets.Integer(default_value=2).tag(config=True)
    right_motor_alpha = traitlets.Float(default_value=1.0).tag(config=True)
    
    right_motor_channel2 = traitlets.Integer(default_value=4).tag(config=True)
    right_motor_alpha2 = traitlets.Float(default_value=1.0).tag(config=True)
    
    def __init__(self, *args, **kwargs):
        super(Robot, self).__init__(*args, **kwargs)
        self.motor_driver = Adafruit_MotorHAT(i2c_bus=self.i2c_bus)
        self.left_motor = Motor(self.motor_driver, channel=self.left_motor_channel, alpha=self.left_motor_alpha)
        self.left_motor2 = Motor(self.motor_driver, channel=self.left_motor_channel2, alpha=self.left_motor_alpha2)
        self.right_motor = Motor(self.motor_driver, channel=self.right_motor_channel, alpha=self.right_motor_alpha)
        self.right_motor2 = Motor(self.motor_driver, channel=self.right_motor_channel2, alpha=self.right_motor_alpha2)
        
    def set_motors(self, left_speed, right_speed):
        self.left_motor.value = left_speed
        self.right_motor.value = right_speed
        
    def forward(self, speed=1.0, duration=None):
        self.left_motor.value = speed
        self.right_motor.value = speed
        
    def backward(self, speed=1.0):
        self.left_motor.value = -speed
        self.right_motor.value = -speed

    def left(self, speed=1.0):
        self.left_motor.value = -speed
        self.right_motor.value = speed

    def right(self, speed=1.0):
        self.left_motor.value = speed
        self.right_motor.value = -speed

    def stop(self):
        self.left_motor.value = 0
        self.right_motor.value = 0       
        
    def forward2(self, speed2=1.0):
        self.left_motor2.value = speed2
        self.right_motor2.value = speed2
        
    def left2(self, speed2=1.0):
        self.left_motor2.value = -speed2
        self.right_motor2.value = speed2 
        
    def right2(self, speed2=1.0):
        self.left_motor2.value = speed2
        self.right_motor2.value = -speed2
        
    def stop2(self):
        self.left_motor2.value = 0
        self.right_motor2.value = 0
        
    def backward2(self, speed2=1.0):
        self.left_motor2.value = -speed2
        self.right_motor2.value = -speed2
        
    def set_motors2(self, left_speed2, right_speed2):
        self.left_motor2.value = left_speed2
        self.right_motor2.value = right_speed2
