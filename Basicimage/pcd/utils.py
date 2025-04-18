import cv2

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
