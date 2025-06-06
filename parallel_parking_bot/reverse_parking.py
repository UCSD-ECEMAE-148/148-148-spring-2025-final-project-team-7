# function to reverse park the car, edit the values as needed
import time
from control_values import STEER_LEFT, STEER_STRAIGHT, THROTTLE_REVERSE, PARK_TIME
from vesc_control import set_throttle, set_steering, stop_car

def reverse_parallel_park(vesc):
    # reverse parking procedure

    # 1) GO FORWARD
    print("Going forward...")
    set_steering(vesc, 0.5)  # straight (0.5), right (1.0), left (0.0)
    set_throttle(vesc, 0.05) # power
    time.sleep(2.0)  # adjust for arc length

    # 2) REVERSE LEFT
    print("Going back...")
    set_steering(vesc, 1.4)  # straight (0.5), right (1.0), left (0.0)
    set_throttle(vesc, -0.07) # power
    time.sleep(0.68)  # adjust for arc length

    # 2) REVERSE RIGHT
    print("Going back...")
    set_steering(vesc, 0.0)  # straight (0.5), right (1.0), left (0.0)
    set_throttle(vesc, -0.062) # power
    time.sleep(0.58)  # adjust for arc length

    # END WITH WHEELS STRAIGHT
    print("Straightening out...")
    set_steering(vesc, 0.5)
    time.sleep(0.05)  # move straight for a bit

    # Step 3: Stop
    stop_car(vesc) # END OF CODE
    print("Reverse Parked!")

