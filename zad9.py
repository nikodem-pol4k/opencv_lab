# Dynamiczna zmiana rozmiaru w pętli
# a. Stopniowo zwiększaj rozmiar obrazu od 100% do 300% w krokach co
# 20%.
# b. Wyświetl każdą wersję na ekranie z krótkim opóźnieniem ( cv2.waitKey(500) ).

import cv2 

image = cv2.imread("image_small.jpg")

for i in range(10, 31, 2):
    w = int(image.shape[1] * (i/10))
    h = int(image.shape[0] * (i/10))
    image = cv2.resize(image, (w, h))
    cv2.imshow("Resizing", image)
    cv2.waitKey(500)   