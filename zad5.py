# Detekcja małych ikon interfejsu
# a Wybierz zrzut ekranu aplikacji (np. ikonę kosza, lupy, itp.).
# b Wyodrębnij mały fragment jako szablon.
# c Wykonaj dopasowanie na pełnym zrzucie.
# d Zaznacz wynik i porównaj z oczekiwanym

import cv2

image = cv2.imread("balatro.jpg")
template = cv2.imread("card.jpg")
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

startX, startY = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]

cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 2)
print(f"maxVal: {maxVal}")

cv2.imshow("Dopasowanie", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
