# function to align car parallel to spot after detecting it
import time
from control_vals import STEER_LEFT, STEER_STRAIGHT, THROTTLE_FORWARD, ALIGN_TIME
from vesc_control import set_throttle, set_steering, stop_car

def align_to_side_of_spot(vesc):
    print("Aligning to the left side of the spot...")

    # Step 1: Start turning left while moving forward
    print("Turning left and moving forward...")
    set_steering(vesc, 0.175)  # full or partial left
    set_throttle(vesc, 0.05)
    time.sleep(1.2)  # adjust for arc length

    # Step 2: Straighten the car to get parallel to left boundary
    print("Straightening out...")
    set_steering(vesc, 0.85)
    time.sleep(1.5)  # move straight for a bit

    # Step 2: Straighten the car to get parallel to left boundary
    print("Straightening out...")
    set_steering(vesc, 0.5)
    time.sleep(0.05)  # move straight for a bit

    # Step 3: Stop
    stop_car(vesc)
    print("Alignment complete. Ready for forward or reverse parallel park.")

