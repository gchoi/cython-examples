"""
Example 3: Image Processor: Sharpen Filter (Standard Python)
"""

from PIL import Image
import numpy as np
from scipy.signal import convolve2d
import time
import matplotlib.pyplot as plt


def sharpen_image_python(image: Image.Image):
    # Convert the image to RGB
    image_pil = image.convert('RGB')

    # Define a sharpening kernel
    kernel = np.array(
        [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0]
        ]
    )

    # Convert image to a numpy array
    image_array = np.array(image_pil)

    # Prepare an empty array for the sharpened image
    sharpened_array = np.zeros_like(image_array)

    # Apply the convolution kernel to each channel (assuming RGB image)
    for i in range(3):
        channel = image_array[:, :, i]
        # Perform convolution
        convolved_channel = convolve2d(channel, kernel, mode='same', boundary='wrap')

        # Clip values to be in the range [0, 255]
        convolved_channel = np.clip(convolved_channel, 0, 255)

        # Store back in the sharpened array
        sharpened_array[:, :, i] = convolved_channel.astype(np.uint8)

    # Debugging: Check output values
    print("Sharpened array values: Min =", sharpened_array.min(), "Max =", sharpened_array.max())

    # Convert array back to image
    sharpened_image = Image.fromarray(sharpened_array)
    return sharpened_image


if __name__ == "__main__":
    image_path = './test-images/background.jpg'
    image = Image.open(image_path)

    # Time the sharpening with Python
    start_time = time.time()
    sharpened_image = sharpen_image_python(image=image)
    python_time = time.time() - start_time

    if sharpened_image:
        # Display the original and sharpened images using Matplotlib
        fig, axs = plt.subplots(1, 2, figsize=(15, 7))

        # Original image
        axs[0].imshow(image)
        axs[0].set_title("Original Image")
        axs[0].axis('off')

        # Sharpened image
        axs[1].imshow(sharpened_image)
        axs[1].set_title("Sharpened Image")
        axs[1].axis('off')

        # Show both of the images side by side
        plt.show()
    else:
        print("Failed to generate sharpened image.")

    # Print the time taken for Python processing
    print(f"Image Processing for the image with resolution: {image.size}")
    print(f"Processing time with Python: {python_time:.5f} (sec)")
