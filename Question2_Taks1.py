from PIL import Image
import numpy as np

# https://github.com/rupin01-uni/Syd124Python2nd.git
# Load the original image
original_image_path = 'D:\Software_now_project\Chapter_1.jpeg'
original_image = Image.open(original_image_path)

# pip install Pillow
import time
from PIL import Image

# Open the original image
original_image_path = "D:\Software_now_project\Chapter_1.jpeg"
original_image = Image.open(original_image_path)

# Get the size of the image
width, height = original_image.size

# Get the current time and generate a number
current_time = int(time.time())
generated_number = (current_time % 100) + 50

# Iterate through each pixel and modify the values
for y in range(height):
    for x in range(width):
        # Get the original pixel values
        r, g, b = original_image.getpixel((x, y))

        # Add the generated number to each channel
        r += generated_number
        g += generated_number
        b += generated_number

        # Update the pixel values in the original image
        original_image.putpixel((x, y), (r, g, b))

# Save the modified image
output_image_path = "D:\Software_now_project\Chapter1_output.jpg"
original_image.save(output_image_path)

# Calculate the sum of red pixel values in the modified image
red_sum = sum(pixel[0] for pixel in original_image.getdata())

# Print the sum of red pixel values
print("Sum of red pixel values:", red_sum)
print(generated_number)
