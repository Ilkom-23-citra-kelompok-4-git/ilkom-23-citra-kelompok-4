import os
import cv2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Konfigurasi folder
UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/processed'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

def edge_detection(image_path):
    # Baca gambar
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # Terapkan Canny Edge Detection
    edges = cv2.Canny(img, 50, 150)
    # Simpan hasilnya di folder processed
    output_filename = 'output.png'
    output_path = os.path.join(app.config['PROCESSED_FOLDER'], output_filename)
    cv2.imwrite(output_path, edges)
    return output_filename  # Kembalikan nama file saja

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == "":
            return redirect(request.url)
        if file:
            # Simpan file upload di folder uploads
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            # Proses gambar dan simpan di folder processed
            processed_filename = edge_detection(filepath)
            return render_template("index.html", 
                               uploaded_image=f"uploads/{file.filename}", 
                               output_image=f"processed/{processed_filename}")
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)