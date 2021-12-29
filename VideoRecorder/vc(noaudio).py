import os
import cv2


class VideoRec:
    def __init__(self, camID: int, fname: str, fps: int, res: str):

        self.camId = camID
        self.cam = cv2.VideoCapture(self.camId, cv2.CAP_DSHOW)

        self.fname = fname
        self.fps = fps
        self.res = res

        self.VIDEO_TYPE = {
            'avi': cv2.VideoWriter_fourcc(*'XVID'),
            'mp4': cv2.VideoWriter_fourcc(*'XVID'),
        }

        self.STD_DIMENSIONS = {
            "480p": (640, 480),
            "720p": (1280, 720),
            "1080p": (1920, 1080),
            "4k": (3840, 2160),
        }

    def _set_res(self, w, h):
        self.cam.set(3, w)
        self.cam.set(4, h)

    def get_dims(self):
        w, h  = self.STD_DIMENSIONS["480p"]

        if self.res in self.STD_DIMENSIONS:
            w, h = self.STD_DIMENSIONS[self.res]

        self._set_res(w, h)

        return (w, h)

    def _get_video_type(self):
        _, ext = os.path.splitext(self.fname)
        return self.VIDEO_TYPE[ext] if ext in self.VIDEO_TYPE else self.VIDEO_TYPE['avi']

    def reacord(self):
        out = cv2.VideoWriter(self.fname, self._get_video_type(), self.fps, self.get_dims())
        while True:
            # capture frame-by-frame
            success, frame = self.cam.read()
            out.write(frame)
            # Display the resulting frame
            cv2.imshow('frame', frame)
            if cv2.waitKey(10) == ord('q'):
                break
        # when everything is done, release the capture
        self.cam.release()
        out.release()
        cv2.destroyAllWindows()

        return None



if __name__ == "__main__":
    vc = VideoRec(0, "output.avi", 25, "480p")
    vc.reacord()