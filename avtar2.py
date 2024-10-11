import cv2

# Apply cartoon effect on the image
def cartoonify_image(img):
    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur to the grayscale image
    gray = cv2.medianBlur(gray, 1)  # Increased kernel size for better blurring
    
    # Use adaptive thresholding to create an edge mask
    edges = cv2.adaptiveThreshold(
        gray, 255, 
        cv2.ADAPTIVE_THRESH_MEAN_C, 
        cv2.THRESH_BINARY, 
        9,  # Size of the pixel neighborhood
        8   # Constant subtracted from the mean
    )
    
    # Apply bilateral filter to the original image
    color = cv2.bilateralFilter(img, d=1, sigmaColor=300, sigmaSpace=300)  # d=9 gives better smoothing
    
    # Combine the color image with edges to create a cartoon effect
    cartoon = cv2.bitwise_and(color, color, mask=edges)
    
    return cartoon

# Load the image
image = cv2.imread("baikunthaimg.jpg")

# Apply cartoon effect
cartoon_image = cartoonify_image(image)

# Save the output
cv2.imwrite("cartoon_avatar.jpg", cartoon_image)
