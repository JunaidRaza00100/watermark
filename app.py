from flask import Flask, request, send_file
from PIL import Image
import cv2
import numpy as np
import io

app = Flask(__name__)

def remove_watermark(image_path):
    # Watermark removal logic (this is a basic placeholder)
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    mask = cv2.inpaint(image, thresh, 3, cv2.INPAINT_TELEA)
    return mask

@app.route('/remove-watermark', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return "No file found", 400

    file = request.files['image']
    image = Image.open(file.stream)
    image_path = 'uploaded_image.jpg'
    image.save(image_path)

    result_image = remove_watermark(image_path)

    is_success, buffer = cv2.imencode(".jpg", result_image)
    io_buf = io.BytesIO(buffer)
    return send_file(io_buf, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True)
