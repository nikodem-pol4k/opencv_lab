# Zmiana rozmiaru na konkretną wartość
# a. Zmień rozmiar obrazu na dokładnie 200×300 pikseli.
# b. Użyj cv2.resize().

import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]

resized = cv2.resize(image, (200, 300), interpolation=cv2.INTER_LINEAR)
cv2.imshow("Resized", resized)
cv2.waitKey(0)