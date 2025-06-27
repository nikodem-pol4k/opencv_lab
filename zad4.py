# Złożona figura
# a. Narysuj na obrazie figurę składającą się z kwadratu o wymiarach 100x100
# px, wewnątrz którego znajduje się mniejszy okrąg o promieniu 30 px.
# Wszystko powinno być wycentrowane na obrazie.
import cv2 
import numpy as np

canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
red = (0, 0, 255)
white = (255, 255, 255)
cv2.rectangle(canvas, (centerY - 50, centerX - 50), (centerY + 50, centerX + 50), white, -1)
cv2.circle(canvas, (centerX, centerY), 30, red, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)