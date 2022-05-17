import cv2
from django.shortcuts import render
from django.views.decorators import gzip
from django.http import StreamingHttpResponse

# Create your views here.
@gzip.gzip_page
def home(request):
    return render(request, "home.html")

def getVideo(request):
    try:
        return StreamingHttpResponse(gen(VideoCam()),content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        pass

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        

class VideoCam(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()
        cv2.destroyAllWindows()

    def get_frame(self):
        ret, image = self.video.read()
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()