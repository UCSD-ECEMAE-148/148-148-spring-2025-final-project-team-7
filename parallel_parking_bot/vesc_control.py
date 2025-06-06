# function to control vesc for parallel parking
import time

def set_throttle(vesc, speed):
    vesc.set_duty_cycle(speed)

def set_steering(vesc, angle):
    vesc.set_servo(angle)

def stop_car(vesc):
    set_throttle(vesc, 0.0)
