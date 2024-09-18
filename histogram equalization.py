import cv2

image = cv2.imread(r"C:/Users/91949/Pictures/IMG_0053 (1).JPG", cv2.IMREAD_GRAYSCALE)
equalized_image = cv2.equalizeHist(image)

cv2.imshow('Original Image', image)
cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
