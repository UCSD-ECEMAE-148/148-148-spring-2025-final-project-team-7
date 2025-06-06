# function to configure HSV mask for detecting the parking spot

import cv2
import numpy as np
import depthai as dai

def create_pipeline():
    pipeline = dai.Pipeline()
    cam_rgb = pipeline.create(dai.node.ColorCamera)
    cam_rgb.setBoardSocket(dai.CameraBoardSocket.RGB)
    cam_rgb.setResolution(dai.ColorCameraProperties.SensorResolution.THE_1080_P)
    cam_rgb.setInterleaved(False)
    cam_rgb.setPreviewSize(640, 480)

    xout = pipeline.create(dai.node.XLinkOut)
    xout.setStreamName("video")
    cam_rgb.preview.link(xout.input)

    return pipeline

def nothing(x): pass

def create_hsv_trackbar():
    cv2.namedWindow("Trackbars")
    cv2.createTrackbar("L - H", "Trackbars", 100, 179, nothing)
    cv2.createTrackbar("L - S", "Trackbars", 150, 255, nothing)
    cv2.createTrackbar("L - V", "Trackbars", 50, 255, nothing)
    cv2.createTrackbar("U - H", "Trackbars", 140, 179, nothing)
    cv2.createTrackbar("U - S", "Trackbars", 255, 255, nothing)
    cv2.createTrackbar("U - V", "Trackbars", 255, 255, nothing)

def get_hsv_bounds():
    lh = cv2.getTrackbarPos("L - H", "Trackbars")
    ls = cv2.getTrackbarPos("L - S", "Trackbars")
    lv = cv2.getTrackbarPos("L - V", "Trackbars")
    uh = cv2.getTrackbarPos("U - H", "Trackbars")
    us = cv2.getTrackbarPos("U - S", "Trackbars")
    uv = cv2.getTrackbarPos("U - V", "Trackbars")
    return np.array([lh, ls, lv]), np.array([uh, us, uv])

def detect_blue_rectangle(frame, lower_blue, upper_blue):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detected = False

    for c in contours:
        approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
        area = cv2.contourArea(c)
        if len(approx) == 4 and area > 300:  # Lowered for debugging
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)
            detected = True

    return frame, mask, detected

def main():
    pipeline = create_pipeline()
    device = dai.Device(pipeline)
    video = device.getOutputQueue(name="video", maxSize=4, blocking=False)

    create_hsv_trackbar()

    print("Adjust HSV sliders to detect blue spot. Press 'q' to quit.")

    while True:
        in_frame = video.get()
        frame = in_frame.getCvFrame()

        lower_blue, upper_blue = get_hsv_bounds()
        processed_frame, mask, detected = detect_blue_rectangle(frame, lower_blue, upper_blue)

        if detected:
            cv2.putText(processed_frame, "Blue Rectangle Detected!", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("OAK-D Camera Feed", processed_frame)
        cv2.imshow("Mask", mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
