import cv2
# Znajdowanie najjaśniejszego piksela w obrazie
# a. Przeszukaj cały obraz i znajdź piksel o najwyższej wartości jasności.
# b. Wyświetl jego współrzędne i wartość.

image = cv2.imread('./kot.jpg', cv2.IMREAD_GRAYSCALE)
(h, w) = image.shape[:2]

max_intensity = -1 
brightest_pixel = None
for y in range(h):
    for x in range(w):
        pixel_value = image[y, x]
        if pixel_value > max_intensity:
            max_intensity = pixel_value
            brightest_pixel = (x, y)
print(brightest_pixel)