# Odbicie na podstawie wyboru użytkownika
# a. Napisz skrypt, który wczytuje obraz i pyta użytkownika o sposób odbicia
# ( 0 – pionowe, 1 – poziome, -1 – oba).
# b. Na podstawie wyboru wykonuje operację i wyświetla wynik.

import cv2 

x = 0
try:
    x = int(input('Podaj odbicie (0 -> pionowe, 1 -> poziome, -1 -> oba): '))
except ValueError:
    print('Napisz liczbe!!!!( ｡ •̀ ⤙ •́ ｡ )')
    exit(1)

image = cv2.imread("image.jpg")
if x >= -1 and x <= 1:
    flipped = cv2.flip(image, x)
    cv2.imshow("Flipped", flipped)
    cv2.waitKey(0)
else:
    print('Input musi byc -1, 0, 1. ')
