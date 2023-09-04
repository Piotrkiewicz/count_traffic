import typing

import cv2
import numpy as np


def get_next_frame(file_path) -> np.ndarray:
    video_stream = cv2.VideoCapture(file_path)

    while video_stream.isOpened():
        # grab the current frame
        ret, frame = video_stream.read()

        # check to see if we have reached the end of the stream
        if frame is None:
            break

        yield frame

    video_stream.release()
