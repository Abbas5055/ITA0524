import cv2
import numpy as np

image = cv2.imread(r"C:/Users/91949/Pictures/IMG_0053 (1).JPG", cv2.IMREAD_GRAYSCALE)

# Define a kernel (structuring element)
kernel = np.ones((15, 15), np.uint8)

# Apply the Top Hat transformation (original image - opening)
top_hat = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)

cv2.imshow('Original Image', image)
cv2.imshow('Top Hat Transformation', top_hat)

cv2.waitKey(0)
cv2.destroyAllWindows()
