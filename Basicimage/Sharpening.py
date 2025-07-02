import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os
from datetime import datetime

def convolve2d_custom(image, kernel, padding_mode='edge'):
    """
    Melakukan konvolusi 2D pada satu channel citra
    """
    kernel_height, kernel_width = kernel.shape
    pad_h, pad_w = kernel_height // 2, kernel_width // 2
    padded_img = np.pad(image, ((pad_h, pad_h), (pad_w, pad_w)), mode=padding_mode)
    output = np.zeros_like(image)

    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            region = padded_img[y:y+kernel_height, x:x+kernel_width]
            output[y, x] = np.sum(region * kernel)
    return output

def get_kernel(kernel_type='default'):
    if kernel_type == 'aggressive':
        return np.array([
            [-1, -1, -1],
            [-1,  9, -1],
            [-1, -1, -1]
        ], dtype=np.float32)
    elif kernel_type == 'edge_enhance':
        return np.array([
            [1,  -2,  1],
            [-2,  5, -2],
            [1,  -2,  1]
        ], dtype=np.float32)
    else:
        return np.array([
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ], dtype=np.float32)

def apply_sharpening_filter_numpy(image_path, output_dir, kernel_type='default'):
    # Load and convert image
    img = Image.open(image_path).convert('RGB')
    img_array = np.array(img, dtype=np.float32)
    
    kernel = get_kernel(kernel_type)

    if len(img_array.shape) == 2:
        sharpened = convolve2d_custom(img_array, kernel)
    else:
        sharpened = np.zeros_like(img_array)
        for c in range(3):
            sharpened[..., c] = convolve2d_custom(img_array[..., c], kernel)

    sharpened = np.clip(sharpened, 0, 255).astype(np.uint8)
    output_img = Image.fromarray(sharpened)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_filename = f'sharpened_{kernel_type}_{timestamp}.jpg'
    output_path = os.path.join(output_dir, output_filename)
    output_img.save(output_path)

    print(f"Sharpened image saved as {output_path}")

    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(img)
    plt.title("Original Image")
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(output_img)
    plt.title(f"Sharpened Image ({kernel_type})")
    plt.axis('off')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    input_image_path = 'image/bangunan.jpg'
    output_dir = '.'
    apply_sharpening_filter_numpy(input_image_path, output_dir, kernel_type='default')
