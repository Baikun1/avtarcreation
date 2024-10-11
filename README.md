# Cartoonify Image and Create Avatar Using Python

This Python script uses the OpenCV and NumPy libraries to convert an image into a cartoon-style avatar while retaining the original facial features and colors. It also utilizes the PIL (Pillow) library for image handling. 

## Prerequisites

Before running the script, ensure that you have the following libraries installed:

- OpenCV
- NumPy
- Pillow

You can install these libraries using pip if you haven't already:

```python
pip install opencv-python numpy pillow
```
## Code Explanation
Importing Libraries
```python
import cv2
import numpy as np
from PIL import Image
```
- cv2: This is the OpenCV library used for image processing.
- numpy: This library is used for numerical operations and array handling.
- Image from PIL: This module is used for image handling and displaying images.

## Defining the Cartoonification Function
```python

def cartoonify_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 8)
    color = cv2.bilateralFilter(img, d=5, sigmaColor=50, sigmaSpace=50)
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cartoon = cv2.bitwise_and(color, edges_colored)
    cartoon = cv2.addWeighted(cartoon, 0.8, img, 0.2, 0)
    return cartoon
```
## Convert Image to Grayscale:
```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY): Converts the input image from BGR to grayscale.
Apply Median Blur:

gray = cv2.medianBlur(gray, 5): Smoothens the grayscale image to reduce noise.
```
### Edge Detection:
- edges = cv2.adaptiveThreshold(...):Applies adaptive thresholding to detect edges in the image, which are crucial for the cartoon effect.
Bilateral Filter:

- color = cv2.bilateralFilter(...): Applies a bilateral filter to the original image to smooth out the colors while preserving edges.
Convert Edges to 3-Channel:

- edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR): Converts the single-channel edge image back to a 3-channel image for blending.
Combine Images:

- cartoon = cv2.bitwise_and(color, edges_colored): Combines the filtered color image with the edge mask.
Final Blending:

- cartoon = cv2.addWeighted(...): Blends the cartoon image with the original image to maintain some original features and colors.
## Creating the Avatar Function
```python

def create_avatar(input_image_path, output_image_path):
    img = cv2.imread(input_image_path)
    if img is None:
        print("Error: Could not read the image.")
        return
    
    avatar = cartoonify_image(img)
    cv2.imwrite(output_image_path, avatar)
    print(f"Avatar saved as {output_image_path}")
```
## Read the Input Image:

- img = cv2.imread(input_image_path): Loads the input image from the specified path.
Check if the Image is Loaded:

- If the image cannot be loaded, an error message is printed, and the function returns.
Generate Cartoon Avatar:

- Calls the cartoonify_image function to process the image.
Save the Output Image:

- cv2.imwrite(output_image_path, avatar): Saves the generated avatar to the specified output path.
Main Execution
python
Copy code
input_image_path = 'input_img.jpg' 
output_image_path = 'avatar_image.jpg'  
create_avatar(input_image_path, output_image_path)
Specify the input image path (input_image_path) and output image path (output_image_path) where the generated avatar will be saved.
Call the create_avatar function to process the image and save the output.
How to Use This Code
Prepare Your Environment:

- Ensure you have Python installed on your system along with the required libraries.
Place Your Image:

- Place the image you want to convert into a cartoon avatar in the same directory as your script, or provide the full path to the image.
Run the Script:

Execute the script in your Python environment (e.g., command line, terminal, or an IDE).
Make sure to replace input_img.jpg with the filename of your image.
Check the Output:

After execution, you should find the generated avatar saved as avatar_image.jpg in the same directory (or the specified path).
Example
If you have an image named my_photo.jpg, you would modify the paths like this:

```python

input_image_path = 'my_photo.jpg' 
output_image_path = 'my_avatar.jpg'  
create_avatar(input_image_path, output_image_path)
After running the script, check for my_avatar.jpg in the directory.

```
### Notes
- Ensure that the input image has a valid path.
- You can customize the names of the input and output files as needed.
- Feel free to experiment with the parameters in the `cartoonify_image` function to achieve d