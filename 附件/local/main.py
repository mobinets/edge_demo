from flask import Flask,request
import os
import detect_picamera
app = Flask(__name__)

@app.route('/detect',methods=['POST'])
def yoloDetect():
    f=request.files['img']
    f.save('image.jpg')
    result=detect_picamera.getDetectResult(imagePath='image.jpg')
    os.remove('image.jpg')
    if result:
        return str(result[0]['class_id'])
    else:
        return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)