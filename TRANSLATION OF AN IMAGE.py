import cv2
import numpy as np

def translate_image(image, tx, ty):
    rows, cols = image.shape[:2]
    M = np.float32([[1, 0, tx], [0, 1, ty]])
    translated_image = cv2.warpAffine(image, M, (cols, rows))
    return translated_image

image = cv2.imread(r"C:/Users/91949/Pictures/IMG_0053 (1).JPG")
translated_image = translate_image(image, 50, 100)

cv2.imshow('Translated Image', translated_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
