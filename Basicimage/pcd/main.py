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