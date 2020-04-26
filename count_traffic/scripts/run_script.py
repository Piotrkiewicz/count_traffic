import os
import time
import pathlib
import functools

import cv2

import count_traffic.opencv_approch.video_capture.file as vf
import count_traffic.opencv_approch.tracker as tr


def play_back_video(path):
    for image in vf.get_next_frame(str(path)):
        cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
            break
        time.sleep(1/15.)


def main():
    video_file = pathlib.Path('../data/output.avi')
    gen = functools.partial(vf.get_next_frame, str(video_file))
    tr.track_using_optical_flow(gen)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print(" --- Took %.3f seconds --- " % (time.time() - start_time))
