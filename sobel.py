import cv2
import matplotlib.pyplot as plt
img = cv2.imread('C://Users//91949//Pictures//IMG_0053 (1).JPG', 0)
sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobelx, sobely)
plt.imshow(sobel, cmap='gray')
plt.show()
