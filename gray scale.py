import cv2
image = cv2.imread(r'C:/Users/91949/Pictures/IMG_0053 (1).JPG')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image', image)
cv2.imshow('Gray-Scale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
