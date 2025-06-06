# function to perform forward parking maneuver, edit values as needed
import time
from control_values import STEER_RIGHT, STEER_STRAIGHT, THROTTLE_FORWARD, PARK_TIME
from vesc_control import set_throttle, set_steering, stop_car

def forward_parallel_park(vesc):
    print("Forward parking...")
    # forward parking procedure

    # 1) GO BACK
    print("Going back...")
    set_steering(vesc, 0.5)  # straight (0.5), right (1.0), left (0.0)
    set_throttle(vesc, -0.05) # power
    time.sleep(1.7)  # adjust for arc length

    # 2) TURN RIGHT
    print("Going back...")
    set_steering(vesc, 1.4)  # straight (0.5), right (1.0), left (0.0)
    set_throttle(vesc, 0.062) # power
    time.sleep(0.74)  # adjust for arc length

    # 2) TURN LEFT
    print("Going back...")
    set_steering(vesc, 0.0)  # straight (0.5), right (1.0), left (0.0)
    set_throttle(vesc, 0.064) # power
    time.sleep(0.58)  # adjust for arc length

    # END WITH WHEELS STRAIGHT
    print("Straightening out...")
    set_steering(vesc, 0.5)
    time.sleep(0.05)  # move straight for a bit

    # Step 3: Stop
    stop_car(vesc) # END OF CODE
    print("Forward Parked!")

