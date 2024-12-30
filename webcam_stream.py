import logging
from flask import Flask, Response
import cv2

logger = logging.getLogger(__name__)
logging.basicConfig(filename='webcam_logging.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s')

app = Flask(__name__)
HOST = "0.0.0.0"
PORT = 5000

logger.info('Webcam streamer started')

# Initialize webcam 
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()
        if not success:
            logger.error('Problem capturing frame')
            break
        else:
            # Encode the frame in JPEG format
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()

            # Yield the frame in byte format for streaming
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    # Return video stream as a response
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def index():
    return "<img src='/video_feed' />"

app.run(host=HOST, port=PORT, debug=True)
