import cv2
# Modyfikacja całego wiersza pikseli
# Pobieranie i ustawianie wartości pikseli 10
# a. Wczytaj obraz i zmień kolor wszystkich pikseli w 100. wierszu na zielony
# (0, 255, 0) .
# b. Wyświetl obraz przed i po zmianie.

image = cv2.imread('./kot.jpg')
(h, w) = image.shape[:2]
cv2.imshow("Old", image)
image[100, 0:w] = (0, 255, 0)
cv2.imshow("Updated", image)
cv2.waitKey(0)
