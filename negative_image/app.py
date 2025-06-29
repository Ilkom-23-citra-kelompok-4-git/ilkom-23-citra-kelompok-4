from flask import Flask, render_template, request, url_for
import cv2
import os
from werkzeug.utils import secure_filename
from PIL import Image

app = Flask(__name__)
UPLOAD_FOLDER = 'negative_image/static/negative'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Function to make a negative image
def make_negative(image_path, save_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)  # ✅ ensure color
    if img is None:
        return None
    negative = 255 - img
    cv2.imwrite(save_path, negative)
    return save_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files.get('image')
        if file and file.filename != '':
            # Secure and set paths
            filename = secure_filename(file.filename)
            base_filename = os.path.splitext(filename)[0] + ".jpg"  # force .jpg
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], base_filename)

            # ✅ Convert uploaded image to RGB JPEG
            img = Image.open(file).convert("RGB")
            img.save(input_path, format="JPEG")
            # Debug check
            test_img = Image.open(input_path)
            print("Mode after save:", test_img.mode)


            # ✅ Generate negative
            negative_filename = f"negative_{base_filename}"
            negative_path = os.path.join(app.config['UPLOAD_FOLDER'], negative_filename)
            make_negative(input_path, negative_path)

            # ✅ Send correct paths to template
            original_url = url_for('static', filename=f'negative/{base_filename}')
            negative_url = url_for('static', filename=f'negative/{negative_filename}')

            return render_template('negative.html',
                                   original=original_url,
                                   result=negative_url)

    return render_template('negative.html', original=None, result=None)

if __name__ == '__main__':
    app.run(debug=True)
