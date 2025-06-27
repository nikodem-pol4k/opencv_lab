# Przetestuj odporność algorytmu na "fałszywe trafienia".
# a Wczytaj obraz z wieloma podobnymi obiektami (np. klocki LEGO,
# opakowania).
# b Wytnij jeden jako szablon.
# c Spróbuj wykryć jego wystąpienia.
# d Czy pojawiły się błędne detekcje? Jak to wyeliminować?

import cv2

image = cv2.imread("balatro_cards.png")
template = cv2.imread("test_card.png")
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = zip(*((result >= threshold).nonzero()[::-1]))

for pt in loc:
    cv2.rectangle(image, pt, (pt[0] + template.shape[1], pt[1] + template.shape[0]), (0,255,0), 2)

cv2.imshow("Dopasowania", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
