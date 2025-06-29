import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

def apply_sharpening_filter_numpy(image_path, output_path):
    # Load the image
    img = Image.open(image_path)
    img_array = np.array(img, dtype=np.float32)
    # Penjelasan: Muat citra dari file dan konversi ke array NumPy dengan tipe data float32.
    # Ini akan bekerja baik untuk citra grayscale maupun RGB.

    # Define the sharpening filter kernel
    sharpening_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])
    # Penjelasan: Definisikan kernel pengasah. Kernel ini digunakan untuk mengonvolusi dengan citra.
    # Kernel ini mengurangi piksel sekitar dan meningkatkan piksel pusat.

    # Get the dimensions of the image
    if len(img_array.shape) == 2:
        height, width = img_array.shape
        channels = 1
    else:
        height, width, channels = img_array.shape
    # Penjelasan: Dapatkan dimensi citra. Jika citra adalah grayscale, hanya memiliki dua dimensi (tinggi dan lebar).
    # Jika citra adalah RGB, memiliki tiga dimensi (tinggi, lebar, dan saluran warna).

    # Create an output array with the same dimensions
    output_array = np.zeros_like(img_array)
    # Penjelasan: Buat array keluaran dengan dimensi yang sama dengan citra asli.

    # Apply the filter to each color channel or single channel
    if channels == 1:
        for y in range(1, height - 1):
            for x in range(1, width - 1):
                # Extract the neighborhood around the current pixel
                neighborhood = img_array[y-1:y+2, x-1:x+2]
                # Apply the kernel and sum the results
                output_array[y, x] = np.sum(neighborhood * sharpening_kernel)
    else:
        for c in range(channels):
            for y in range(1, height - 1):
                for x in range(1, width - 1):
                    # Extract the neighborhood around the current pixel
                    neighborhood = img_array[y-1:y+2, x-1:x+2, c]
                    # Apply the kernel and sum the results
                    output_array[y, x, c] = np.sum(neighborhood * sharpening_kernel)

    # Clip the values to the valid range (0-255)
    output_array = np.clip(output_array, 0, 255)
    # Penjelasan: Batasi nilai piksel ke rentang yang valid (0-255).
    # Ini memastikan bahwa nilai piksel tidak melebihi batas yang diizinkan.

    # Convert the output array back to an image
    output_img = Image.fromarray(output_array.astype(np.uint8))
    # Penjelasan: Konversi array keluaran kembali ke objek citra.
    # Gunakan tipe data uint8 karena citra hanya dapat memiliki nilai piksel dari 0 hingga 255.

    # Save the output image
    output_img.save(output_path)

    print(f"Sharpened image saved as {output_path}")

    # Display the original and sharpened images
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.title("Original Image")
    plt.imshow(img, cmap='gray')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.title("Sharpened Image")
    plt.imshow(output_img, cmap='gray')
    plt.axis('off')

    plt.show()
# Example usage
input_image_path = 'image/bangunan.jpg'  # Replace with your input image path
output_image_path = 'sharpened_image_numpy.jpg'  # Replace with your desired output path
apply_sharpening_filter_numpy(input_image_path, output_image_path)
