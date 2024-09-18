import cv2
import numpy as np
import matplotlib.pyplot as plt
img = cv2.imread(r'C:/Users/91949/Pictures/IMG_0053 (1).JPG', 0)
prewitt_x = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
prewitt_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)
edge_x = cv2.filter2D(img, cv2.CV_32F, prewitt_x)
edge_y = cv2.filter2D(img, cv2.CV_32F, prewitt_y)
prewitt = cv2.magnitude(edge_x, edge_y)
plt.imshow(prewitt, cmap='gray')
plt.show()
