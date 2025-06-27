# Eksperymentowanie z pętlą
# a. Zmodyfikuj kod pętli rysującej okręgi, aby zamiast okręgów rysowała
# kwadraty. Każdy kolejny kwadrat powinien być większy o 20 pikseli od
# poprzedniego i mieć środek w tym samym miejscu.
import cv2 
import numpy as np

canvas = np.zeros((400, 400, 3), dtype="uint8")
(centerX, centerY) = (canvas.shape[1] // 2, canvas.shape[0] // 2)
white = (255, 255, 255)
for r in range(0, 180, 20):
    cv2.rectangle(canvas, (centerY - r//2, centerX - r//2), (centerY + r//2, centerX + r//2), white)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)