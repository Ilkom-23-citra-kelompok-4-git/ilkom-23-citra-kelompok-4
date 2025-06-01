import numpy as np
from PIL import Image

def apply_sharpening_filter_numpy(image_path, output_path):
    # Load the image
    img = Image.open(image_path).convert('L')
    img_array = np.array(img, dtype=np.float32)

    # Define the sharpening filter kernel
    sharpening_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    # Get the dimensions of the image
    height, width = img_array.shape

    # Create an output array with the same dimensions
    output_array = np.zeros_like(img_array)

    # Apply the filter
    for y in range(1, height - 1):
        for x in range(1, width - 1):
            # Extract the neighborhood around the current pixel
            neighborhood = img_array[y-1:y+2, x-1:x+2]
            # Apply the kernel and sum the results
            output_array[y, x] = np.sum(neighborhood * sharpening_kernel)

    # Clip the values to the valid range (0-255)
    output_array = np.clip(output_array, 0, 255)

    # Convert the output array back to an image
    output_img = Image.fromarray(output_array.astype(np.uint8))

    # Save the output image
    output_img.save(output_path)

    print(f"Sharpened image saved as {output_path}")

# Example usage
input_image_path = 'image/image1.jpg'  # Replace with your input image path
output_image_path = 'sharpened_image_numpy.jpg'  # Replace with your desired output path
apply_sharpening_filter_numpy(input_image_path, output_image_path)