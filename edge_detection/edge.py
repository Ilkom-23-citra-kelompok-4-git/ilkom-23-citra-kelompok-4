import os
import cv2
import numpy as np
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
UPLOAD_FOLDER = 'static'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def edge_detection(image_path):
    # Baca gambar
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Terapkan Canny Edge Detection
    edges = cv2.Canny(img, 50, 150)
    # Simpan hasilnya
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.png')
    cv2.imwrite(output_path, edges)
    return output_path

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == "":
            return redirect(request.url)
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            processed_image = edge_detection(filepath)
            return render_template("index.html", uploaded_image=file.filename, output_image="output.png")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)