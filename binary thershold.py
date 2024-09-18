import cv2

image = cv2.imread(r"C:/Users/91949/Pictures/IMG_0053 (1).JPG", cv2.IMREAD_GRAYSCALE)

# Apply global binary thresholding
ret, binary_threshold = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

cv2.imshow('Original Image', image)
cv2.imshow('Binary Thresholding', binary_threshold)

cv2.waitKey(0)
cv2.destroyAllWindows()
