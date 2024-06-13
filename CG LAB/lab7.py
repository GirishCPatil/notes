import cv2
import numpy as np

# Define image path (replace with your image path)
image_path = "atc.jpg"

# Load the image
img = cv2.imread(image_path)

# Check if image loading was successful
if img is None:
    print("Error: Could not load image from", image_path)
    exit()

# Get the image height, width, and number of channels
height, width, _ = img.shape

# Split the image into four quadrants
up_left = img[0:height // 2, 0:width // 2]
up_right = img[0:height // 2, width // 2:width]
down_left = img[height // 2:height, 0:width // 2]
down_right = img[height // 2:height, width // 2:width]

# Create a blank canvas to display the quadrants
canvas = np.zeros((height, width, 3), dtype=np.uint8)

# Place the quadrants on the canvas
canvas[0:height // 2, 0:width // 2] = up_left
canvas[0:height // 2, width // 2:width] = up_right
canvas[height // 2:height, 0:width // 2] = down_left
canvas[height // 2:height, width // 2:width] = down_right

# Display the canvas
cv2.imshow("Image Quadrants", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
