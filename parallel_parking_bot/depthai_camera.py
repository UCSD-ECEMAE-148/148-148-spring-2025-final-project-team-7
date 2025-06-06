# function for handing DepthAI front camera and USB camera rear camera
import cv2
import depthai as dai

# Existing functions for DepthAI front camera
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

def get_front_camera():
    pipeline = create_pipeline()
    device = dai.Device(pipeline)
    video = device.getOutputQueue(name="video", maxSize=4, blocking=False)
    return device, video  # caller must keep 'device' alive

def get_usb_camera(camera_index=0):
    cap = cv2.VideoCapture(camera_index)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    if not cap.isOpened():
        raise RuntimeError("Unable to open USB camera")

    return cap
