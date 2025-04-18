import cv2
import os
from utils import (
    load_image, convert_to_grayscale,
    apply_gaussian_blur, apply_threshold,
    apply_canny
)

INPUT_PATH = 'images/sample.jpg'
OUTPUT_DIR = 'output/'