import cv2
# Znajdowanie środka obrazu
# a. Wczytaj obraz i oblicz współrzędne jego środka.
# b. Pobierz wartość koloru piksela w tym miejscu i wyświetl ją w konsoli.
image = cv2.imread('./kot.jpg')
(h, w) = image.shape[:2]
print(f"The center of image: {h//2}, {w//2}")
(b, g, r) = image[h // 2, w //2]
print("Pixel at the center - Red: {}, Green: {}, Blue: {}".format(r, g, b))