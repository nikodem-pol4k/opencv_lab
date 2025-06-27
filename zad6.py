import cv2
# Wypełnienie konkretnego obszaru obrazu jednolitym kolorem
# Pobierz współrzędne środka obrazu.
# Wypełnij kwadrat o wymiarach 100x100 px, którego środek pokrywa się ze
# środkiem obrazu, kolorem czerwonym (0, 0, 255) .
# Wyświetl obraz po zmianach.

image = cv2.imread('./kot.jpg')
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
image[cY-100:cY+100, cX-100:cX+100] = (0, 0, 255)
cv2.imshow("Updated", image)
cv2.waitKey(0)
