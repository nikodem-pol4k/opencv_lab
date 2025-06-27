# Zmiana rozmiaru i zapis pliku
# a. Powiększ obraz do szerokości 800 pikseli i zapisz wynik do pliku
# resized_output.jpg .

import cv2 

image = cv2.imread("image_small.jpg")
cv2.imshow("Original", image)
r = 800.0 / image.shape[1]
dim = (800, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
cv2.imwrite("resized_output.jpg", resized)
cv2.imshow("Resized", resized)
cv2.waitKey(0)