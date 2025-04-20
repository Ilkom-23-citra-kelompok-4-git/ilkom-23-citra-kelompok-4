import cv2
import matplotlib.pyplot as plt
import os

OUTPUT_DIR = 'output/'

def load_image(path):
    return cv2.imread(path)

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def apply_gaussian_blur(image, ksize=(5, 5)):
    return cv2.GaussianBlur(image, ksize, 0)

def apply_threshold(image, thresh=127, maxval=255):
    _, result = cv2.threshold(image, thresh, maxval, cv2.THRESH_BINARY)
    return result

def apply_canny(image, threshold1=100, threshold2=200):
    return cv2.Canny(image, threshold1, threshold2)

def show_image(title, image, cmap='gray'):
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.axis('off')
    plt.show()

def save_image(name, image):
    path = os.path.join(OUTPUT_DIR, name)
    cv2.imwrite(path, image)

def adjust_brightness_contrast(image, alpha=1.5, beta=30):
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

def resize_image(image, scale=0.5):
    width = int(image.shape[1] * scale)
    height = int(image.shape[0] * scale)
    return cv2.resize(image, (width, height))

def rotate_image(image, angle=90):
    height, width = image.shape[:2]
    center = (width // 2, height // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1)
    return cv2.warpAffine(image, matrix, (width, height))
