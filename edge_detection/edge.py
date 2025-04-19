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

def edge_detection(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    edges = cv2.Canny(img, 50, 150)
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    
    # Original
    original_filename = os.path.basename(image_path)
    
    # Processed
    processed_filename = f"edge_{timestamp}.png"
    processed_path = os.path.join(PROCESSED_FOLDER, processed_filename)
    cv2.imwrite(processed_path, edges)

    return original_filename, processed_filename

def get_history_images():
    history_folder = "static/history"
    files = sorted(os.listdir(history_folder), reverse=True)
    print("Found history files:", files)
    return [f"history/{f}" for f in files if f.endswith((".png", ".jpg", ".jpeg"))]

@app.route("/", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def index():
    uploaded_image = None
    output_image = None

    if request.method == "POST":
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == "":
            return redirect(request.url)

        if file:
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            original_filename, processed_filename = edge_detection(filepath)
            uploaded_image = f"uploads/{original_filename}"
            output_image = f"history/{processed_filename}"

    history = []
    originals = os.listdir(UPLOAD_FOLDER)
    processed = os.listdir(PROCESSED_FOLDER)

    for proc_file in processed:
        if proc_file.startswith("edge_"):
            base_name = proc_file.replace("edge_", "")
            if base_name in originals:
                history.append({
                    "original": f"uploads/{base_name}",
                    "processed": f"history/{proc_file}"
                })


    return render_template("index.html", original=base_name, processed=proc_file, history=history)

if __name__ == "__main__":
    app.run(debug=True)