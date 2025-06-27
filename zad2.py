# Powiększenie obrazu dwukrotnie
# a. Powiększ obraz 2× zarówno w pionie, jak i w poziomie.
# b. Użyj metody cv2.INTER_LINEAR .

import cv2

image = cv2.imread("image_small.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]

resized = cv2.resize(image, (w*2, h*2), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized", resized)
cv2.waitKey(0)