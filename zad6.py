# Automatyczne skalowanie na podstawie wysokości
# a. Zmień wysokość obrazu na 400 pikseli, zachowując proporcje.
# b. Wyświetl wynik.

import cv2 
import imutils 

image = cv2.imread("image_small.jpg")
cv2.imshow("Original", image)
r = 400.0 / image.shape[0]
dim = (int(image.shape[1] * r), 400)
resized = imutils.resize(image, dim, inter=cv2.INTER_AREA)
cv2.imshow("Resized", resized)
cv2.waitKey(0)
