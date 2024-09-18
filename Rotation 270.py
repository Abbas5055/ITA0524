import cv2

image = cv2.imread(r"C:/Users/91949/Pictures/IMG_0053 (1).JPG")
rotated_image = cv2.transpose(image)
rotated_image = cv2.flip(rotated_image, flipCode=0)

cv2.imshow('Rotated Image', rotated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
