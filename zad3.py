# Odbicie względem obu osi
# a. Odbij obraz zarówno poziomo, jak i pionowo (czyli względem obu osi).

import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

flipped = cv2.flip(image, -1)
cv2.imshow("Flipped Horizontally & Vertically", flipped)
cv2.waitKey(0)