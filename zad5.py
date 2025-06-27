# Automatyczne skalowanie na podstawie szerokości
# a. Zmień szerokość obrazu na 500 pikseli, zachowując proporcje.
import cv2 

image = cv2.imread("image_small.jpg")
cv2.imshow("Original", image)
r = 500.0 / image.shape[1]
dim = (500, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imshow("Resized", resized)
cv2.waitKey(0)