import cv2
# Wycięcie fragmentu obrazu
# a. Podziel obraz na 9 równych części.
# b. Pobierz fragment obrazu obejmujący środek.
# c. Wyświetl wycięty fragment osobno.

image = cv2.imread('./kot.jpg')
(h, w) = image.shape[:2]
(cX, cY) = (w // 3, h // 3)
center_of_image = image[cY:2*cY, cX:2*cX] 
cv2.imshow("Updated", center_of_image)
cv2.waitKey(0)