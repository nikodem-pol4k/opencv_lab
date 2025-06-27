import cv2
# Sprawdzenie różnicy wartości pikseli
# a. Pobierz wartości pikseli w dwóch różnych miejscach obrazu i porównaj je
# (np. (50,50) i (200,200) ).
# b. Wypisz różnice w wartościach R, G, B.

image = cv2.imread('./kot.jpg')
(b1, g1, r1) = image[50, 50]
(b2, g2, r2) = image[200, 200]
print("Pixel at (50, 50) - Red: {}, Green: {}, Blue: {}".format(r1, g1, b1))
print("Pixel at (200, 200) - Red: {}, Green: {}, Blue: {}".format(r2, g2, b2))
print("Difference - Red: {}, Green: {}, Blue: {}".format(abs(r2-r1), abs(g2-g1), abs(b2-b1)))