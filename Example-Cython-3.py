"""
Example 3: Image Processor: Sharpen Filter (Cython)
"""

from cython_mods.image_processor import sharpen_image_cython
from PIL import Image
import numpy as np
import time as py_time
import matplotlib.pyplot as plt


if __name__ == "__main__":
    # Load the input image
    image_path = './test-images/background.jpg'
    image = Image.open(image_path).convert('RGB')

    # Convert the image to a numPy array
    image_array = np.array(image)

    # Time the sharpening with Cython
    start_time = py_time.time()
    sharpened_array = sharpen_image_cython(image_array=image_array)
    cython_time = py_time.time() - start_time

    # Convert back to an image for displaying
    sharpened_image = Image.fromarray(sharpened_array)

    # Display the original and sharpened image
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.imshow(image)
    plt.title("Original Image")

    plt.subplot(1, 2, 2)
    plt.imshow(sharpened_image)
    plt.title("Sharpened Image")
    plt.show()

    # Print the time taken for Cython processing
    print(f"Image Processing for the image with resolution: {image.size}")
    print(f"Processing time with Cython: {cython_time:.5f} (sec)")
