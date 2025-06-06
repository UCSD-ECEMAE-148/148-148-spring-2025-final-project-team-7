# function for the camera to detect the blue parking spot, edit hsv values as needed
import cv2
import numpy as np
from depthai_camera import get_front_camera, get_usb_camera

def detect_blue_spot(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([53, 26, 76])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
        if len(approx) == 4 and cv2.contourArea(c) > 500:
            return True
    return False

def wait_for_blue_spot():
    device, video = get_front_camera()
    print("Searching for blue spot...")

    while True:
        in_frame = video.get()
        frame = in_frame.getCvFrame()
        if detect_blue_spot(frame):
            print("Blue spot detected!")
            break


