# function to test the hsv values and see hsv mask in effect
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

def detect_blue_spot(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_blue = np.array([53, 26, 76])
    upper_blue = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    detected = False

    for c in contours:
        approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
        area = cv2.contourArea(c)
        if len(approx) == 4 and area > 500:
            cv2.drawContours(frame, [approx], 0, (0, 255, 0), 3)
            detected = True

    return frame, detected


def main():
    pipeline = create_pipeline()
    device = dai.Device(pipeline)
    video = device.getOutputQueue(name="video", maxSize=4, blocking=False)

    print("Starting video stream from OAK-D Lite... Press 'q' to quit.")

    while True:
        in_frame = video.get()
        frame = in_frame.getCvFrame()
        frame, detected = detect_blue_spot(frame)

        if detected:
            cv2.putText(frame, "Blue spot detected!", (10, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        cv2.imshow("OAK-D Camera Feed", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()