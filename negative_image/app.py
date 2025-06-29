from flask import Flask, render_template, request, redirect, url_for
import cv2
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = 'negative_image/static/negative'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Ensure folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def make_negative(image_path, save_path):
    img = cv2.imread(image_path)
    if img is None:
        return None
    negative = 255 - img
    cv2.imwrite(save_path, negative)
    return save_path

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            filename = secure_filename(file.filename)
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(input_path)

            output_filename = f"negative_{filename}"
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            make_negative(input_path, output_path)

            return render_template('negative.html',
                                   original=url_for('static', filename=f'negative/{filename}'),
                                   result=url_for('static', filename=f'negative/{output_filename}'))

    return render_template('negative.html')

if __name__ == '__main__':
    app.run(debug=True)
