import cv2

def load_image(path):
    return cv2.imread(path)

def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)