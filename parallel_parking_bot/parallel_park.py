# main script for parallel parking bot
import time
from pyvesc.VESC import VESC
from spot_detection import wait_for_blue_spot
from align_to_spot import align_to_side_of_spot
from forward_parking import forward_parallel_park
from reverse_parking import reverse_parallel_park
from vesc_control import stop_car

def main():
    # Connect to VESC (adjust ttyUSB index if needed)
    vesc = VESC(serial_port="/dev/ttyACM0")

    print("Starting approach: driving forward until blue spot detected...")
    ##wait_for_blue_spot()
    stop_car(vesc)

    align_to_side_of_spot(vesc)

    print("Press 'f' for forward park, 'r' for reverse park:")
    key = input().lower()

    if key == 'f':
        forward_parallel_park(vesc)
    elif key == 'r':
        reverse_parallel_park(vesc)
    else:
        print("Invalid input. Aborting.")
        stop_car(vesc)

if __name__ == "__main__":
    main()



