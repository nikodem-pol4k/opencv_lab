import cv2
# Kolorowanie fragmentu obrazu
# a. Podziel obraz na 4 równe części (ćwiartki).
# b. Wypełnij lewą górną ćwiartkę kolorem niebieskim (255, 0, 0) .
# c. Wyświetl obraz po zmianach.

image = cv2.imread('./kot.jpg')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
image[0:cY, 0:cX] = (255, 0, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)