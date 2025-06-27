# Wykrywanie logo w butelce Fanty
# a. Wczytaj obraz butelki i szablon logo.
# b. Wykonaj cv2.matchTemplate .
# c. Zaznacz wykryte logo ramką.
# d. Wskaż współrzędne wykrytego logo i wartość dopasowania ( maxVal ).
import cv2 

image = cv2.imread('fanta.jpg')
template = cv2.imread('fanta_logo.png')
cv2.imshow("Image", image)
cv2.imshow("Template", template)

imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(result)
startX, startY = maxLoc
endX = startX + template.shape[1]
endY = startY + template.shape[0]
cv2.rectangle(image, (startX, startY), (endX, endY), (255, 0, 0), 3)
print(f"Wykryto logo -> ({startX}, {startY})")
print(f"Najwyższa wartość dopasowania: {maxVal}")
cv2.imshow("Dopasowanie logo", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
