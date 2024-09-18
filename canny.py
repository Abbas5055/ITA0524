import cv2, matplotlib.pyplot as plt
img = cv2.imread(r"C:/Users/91949/Pictures/IMG_0053 (1).JPG", 0)
canny = cv2.Canny(img, 100, 200)
plt.imshow(canny, cmap='gray')
plt.show()
