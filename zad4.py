# Porównanie efektów
# a. Wyświetl cztery wersje obrazu:
# i. Oryginał
# ii. Odbicie poziome
# iii. Odbicie pionowe
# iv. Odbicie względem obu osi

import cv2

image = cv2.imread("image.jpg")

flipping = [
    ('Original', image),
    ('Odbicie poziome', cv2.flip(image, 1)),
    ('Odbicie pionowe', cv2.flip(image, 0)),
    ('Odbicie względem obu osi', cv2.flip(image, -1))
]

for (name, flip) in flipping:
    print("[INFO] {}".format(name))
    cv2.imshow("{}".format(name), flip)
    cv2.waitKey(0)