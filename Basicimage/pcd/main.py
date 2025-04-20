import cv2
import os
from utils import (
    load_image, convert_to_grayscale, apply_gaussian_blur,
    apply_threshold, apply_canny, show_image, save_image,
    adjust_brightness_contrast, resize_image, rotate_image,
    crop_image, flip_image, apply_hist_equalization
)

INPUT_PATH = 'images/sample.jpg'
OUTPUT_DIR = 'output/'
os.makedirs(OUTPUT_DIR, exist_ok=True)

def process_image():
    # Step 1: Load image
    image = load_image(INPUT_PATH)
    save_image('1_original.jpg', image)

    # Step 2: Convert to Grayscale
    gray = convert_to_grayscale(image)
    save_image('2_grayscale.jpg', gray)

    # Step 3: Apply Gaussian Blur
    blurred = apply_gaussian_blur(gray)
    save_image('3_blurred.jpg', blurred)

    # Step 4: Apply Thresholding
    thresholded = apply_threshold(gray)
    save_image('4_threshold.jpg', thresholded)

    # Step 5: Apply Edge Detection
    edges = apply_canny(gray)
    save_image('5_canny.jpg', edges)

    # Step 6: Adjust Brightness and Contrast
    adjusted = adjust_brightness_contrast(image)
    save_image('6_brightness_contrast.jpg', adjusted)

    # Step 7: Resize Image
    resized = resize_image(image)
    save_image('7_resized.jpg', resized)

    # Step 8: Rotate Image
    rotated = rotate_image(image)
    save_image('8_rotated.jpg', rotated)
