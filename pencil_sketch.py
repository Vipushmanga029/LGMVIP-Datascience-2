from PIL import Image, ImageOps, ImageFilter
import numpy as np
from PIL import ImageChops

def convert_to_pencil_sketch(image_path):
    # Open the image
    image = Image.open(image_path)
    
    # Convert the image to grayscale
    grayscale_image = image.convert("L")
    
    # Invert the grayscale image
    inverted_image = ImageOps.invert(grayscale_image)
    
    # Apply a Gaussian blur to the inverted image
    blurred_image = inverted_image.filter(ImageFilter.GaussianBlur(111))
    
    # Convert the blurred image to a numpy array
    blurred_array = np.array(blurred_image)
    
    # Invert the blurred array
    inverted_blurred_array = np.invert(blurred_array)
    
    # Convert the inverted blurred array back to an Image object
    inverted_blurred_image = Image.fromarray(inverted_blurred_array)
    
    # Create the pencil sketch by blending the grayscale image with the inverted blurred image
    pencil_sketch = ImageChops.multiply(grayscale_image, inverted_blurred_image)
    
    # Display the original image and the pencil sketch
    image.show()
    pencil_sketch.show()

# Provide the path to your image
image_path = "tiger.jpg"

# Convert the image to a pencil sketch
convert_to_pencil_sketch(image_path)
