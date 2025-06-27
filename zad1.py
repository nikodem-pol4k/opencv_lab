# Rysowanie linii
# a. Narysuj niebieską linię od środka obrazu do jego prawego dolnego rogu.
# Grubość linii: 2 px.
# import the necessary packages
import numpy as np
import cv2
canvas = np.zeros((300, 300, 3), dtype="uint8")
red = (255, 0, 0)
cv2.line(canvas, (150, 150), (300, 300), red, 2)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)