# Odbicie poziome
# a. Wczytaj obraz i wykonaj odbicie lustrzane w poziomie.
# b. Wyświetl wynik.

import cv2

image = cv2.imread("image.jpg")
cv2.imshow("Original", image)

flipped = cv2.flip(image, 1)
cv2.imshow("Flipped Horizontally", flipped)
cv2.waitKey(0)