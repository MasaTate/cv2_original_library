import cv2
import warnings


class cv2_video:
    def __init__(self, path):
        self.cap = cv2.VideoCapture(path)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.total_frame = self.cap.get(cv2.CAP_PROP_FRAME_COUNT)
        self.height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        self.width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH)

        if type(self.fps) == float and self.fps > 0 and type(self.total_frame) == float:
            self.duration = int(self.total_frame / self.fps)
        else:
            warnings.warn("can't define video duration")

    def set_second(self, sec):
        assert type(self.fps) == float
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, self.fps * sec)

    def read_sec_frame(self, sec):
        self.set_second(sec)
        ret, frame = self.cap.read()

        if ret == False:
            raise ValueError("can't read frame")

        return frame
