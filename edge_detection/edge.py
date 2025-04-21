import os
import cv2
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Konfigurasi folder
UPLOAD_FOLDER = 'static/uploads'
PROCESSED_FOLDER = 'static/history'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROCESSED_FOLDER'] = PROCESSED_FOLDER

def edge_detection(image_path, color_hex):
    img_gray = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img_gray, 30, 100)

    # Konversi warna HEX ke BGR
    color_bgr = tuple(int(color_hex.lstrip('#')[i:i+2], 16) for i in (4, 2, 0))

    # Convert ke BGR
    color_edge = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    color_edge[edges != 0] = color_bgr

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    processed_filename = f"edge_{timestamp}.png"
    processed_path = os.path.join(PROCESSED_FOLDER, processed_filename)
    cv2.imwrite(processed_path, color_edge)

    return os.path.basename(image_path), processed_filename

def get_history_images():
    history_folder = "static/history"
    files = sorted(os.listdir(history_folder), reverse=True)
    print("Found history files:", files)
    return [f"history/{f}" for f in files if f.endswith((".png", ".jpg", ".jpeg"))]

@app.route("/", methods=["GET", "POST"])
def index():
    uploaded_image = None
    output_image = None

    if request.method == "POST":
        if 'file' not in request.files or request.files['file'].filename == "":
            return redirect(request.url)

        file = request.files['file']
        color = request.form.get("color", "#fff")

        if file:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            filename = f"{timestamp}_{file.filename}"
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            original_filename, processed_filename = edge_detection(filepath, color)
            uploaded_image = f"uploads/{original_filename}"
            output_image = f"history/{processed_filename}"

    # Benerin pairing untuk history
    history = []
    originals = os.listdir(UPLOAD_FOLDER)
    processed = os.listdir(PROCESSED_FOLDER)

    for orig_file in originals:
        ts = orig_file.split("_")[0]
        expected_proc = f"edge_{ts}.png"
        if expected_proc in processed:
            history.append({
                "original": f"uploads/{orig_file}",
                "processed": f"history/{expected_proc}"
            })

    return render_template("index.html", 
                           uploaded_image=uploaded_image, 
                           output_image=output_image, 
                           history=history)

if __name__ == "__main__":
    app.run(debug=True)