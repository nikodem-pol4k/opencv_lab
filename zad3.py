# Rysowanie okręgów, utwórz czarny obraz o wymiarach 300x300 pikseli i
# narysuj na nim:
# a. Niebieski okrąg o promieniu 40 px w lewym górnym rogu.
# b. Czerwony okrąg o promieniu 60 px w środku obrazu.

import numpy as np
import cv2
canvas = np.zeros((400, 400, 3), dtype="uint8")
blue = (255, 0, 0)
red = (0, 0, 255)
cv2.circle(canvas, (40, 40), 40, blue)
cv2.circle(canvas, (200, 200), 60, red)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)