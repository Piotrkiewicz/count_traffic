""" We want to capture video frames, either from the camera or from file. These should be interchangeable so that
we can test and write our code in the same way as we run it."""

import time

from picamera.array import PiRGBArray
from picamera import PiCamera


def get_next_frame(resolution=(640, 480), fps=15):
    # initialize the camera and grab a reference to the raw camera capture
    camera = PiCamera()
    camera.resolution = resolution
    camera.framerate = fps
    rawCapture = PiRGBArray(camera, size=resolution)

    # allow the camera to warmup
    time.sleep(0.1)

    # capture frames from the camera
    for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array

        yield image
        rawCapture.truncate(0)


if __name__ == '__main__':
    import cv2
    for image in get_next_frame():
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        # clear the stream in preparation for the next frame
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
