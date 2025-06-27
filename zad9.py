import cv2
# Zmiana wartości pikseli w określonym zakresie
# a. Wypełnij obszar od (50,50) do (100,100) kolorem białym (255, 255, 255) .
# b. Wyświetl obraz przed i po zmianie.

image = cv2.imread('./kot.jpg')
(h, w) = image.shape[:2]
image[50:100, 50:100] = (255, 255, 255)
cv2.imshow("Updated", image)
cv2.waitKey(0)
