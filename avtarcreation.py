import cv2
import numpy as np
from PIL import Image

def cartoonify_image(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray, 5)
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 8)
    color = cv2.bilateralFilter(img, d=5, sigmaColor=50, sigmaSpace=50)
    edges_colored = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    cartoon = cv2.bitwise_and(color, edges_colored)
    cartoon = cv2.addWeighted(cartoon, 0.8, img, 0.2, 0)
    return cartoon

def create_avatar(input_image_path, output_image_path):
    img = cv2.imread(input_image_path)
    if img is None:
        print("Error: Could not read the image.")
        return
    
    avatar = cartoonify_image(img)
    cv2.imwrite(output_image_path, avatar)
    print(f"Avatar saved as {output_image_path}")

input_image_path = 'baikunthaimg.jpg' 
output_image_path = 'avatar_image.jpg'  
create_avatar(input_image_path, output_image_path)
