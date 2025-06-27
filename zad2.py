# Zobacz, jak bardzo dopasowywanie szablonu jest wrażliwe na obró
# a Obróć obraz Fanty o 30° i 45° ( imutils.rotate() ).
# b Powtórz detekcję logo.
# c Zinterpretuj wynik: czy detekcja zadziałała? Jaki jest maxVal ?

import cv2
import imutils

image = cv2.imread('fanta.jpg')
template = cv2.imread('fanta_logo.png')
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

for angle in [30, 45]:
    rotated = imutils.rotate(image, angle)
    imageGray = cv2.cvtColor(rotated, cv2.COLOR_BGR2GRAY)
    
    result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

    startX, startY = maxLoc
    endX = startX + template.shape[1]
    endY = startY + template.shape[0]

    cv2.rectangle(rotated, (startX, startY), (endX, endY), (255, 0, 0), 3)

    print(f"Obrot {angle}° - maxVal: {maxVal}")
    cv2.imshow(f"Obrot {angle}°", rotated)
    cv2.waitKey(0)

cv2.destroyAllWindows()