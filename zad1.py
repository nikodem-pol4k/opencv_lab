import cv2

# Odczyt wartości piksela
# a. Wczytaj obraz i pobierz wartość piksela znajdującego się w lewym górnym
# rogu (współrzędne 0,0 ).
# b. Wyświetl wartości składowych koloru (R, G, B).

image = cv2.imread('./kot.jpg')
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: {}, Green: {}, Blue: {}".format(r, g, b))