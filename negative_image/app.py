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

# Function to create a negative image using OpenCV
def make_negative(image_path, save_path):
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
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
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            # Save uploaded file first
            file.save(input_path)

            # ✅ Convert to RGB and overwrite to ensure canvas compatibility
            try:
                img = Image.open(input_path).convert('RGB')
                img.save(input_path, format='PNG')
            except Exception as e:
                print("Error converting image:", e)

            # Create negative image
            output_filename = f"negative_{filename}"
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            make_negative(input_path, output_path)

            # Pass URLs to template (static file paths)
            return render_template('negative.html',
                                   original=url_for('static', filename=f'negative/{filename}'),
                                   result=url_for('static', filename=f'negative/{output_filename}'))

    return render_template('negative.html', original=None, result=None)

if __name__ == '__main__':
    app.run(debug=True)
