from flask import Flask, Response
import cv2

app = Flask(__name__)
video = cv2.VideoCapture(0)


@app.route('/')
def index():
    return "Default Message"

def gen(video):
    while True:
        # to get next frame or image in video
        success, image = video.read()
        # returns two values if image is loaded then success is true
        ret, jpeg = cv2.imencode('.jpg', image)
        # save frame as JPG file
        frame = jpeg.tobytes()
        # Converting image into bytes
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/video_feed')
def video_feed():
    global video
    return Response(gen(video),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=2204, threaded=True)
    app.run(debug=True)