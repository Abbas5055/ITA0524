import cv2

image = cv2.imread(r'C:/Users/91949/Pictures/IMG_0053 (1).JPG')
rotated_image = cv2.rotate(image, cv2.ROTATE_180)

cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
