#  Sprawdź wrażliwość na zmianę rozmiaru szablonu.
# a Zmniejsz lub powiększ oryginalny obraz Fanty.Dopasowywanie szablonów4
# b Wykonaj dopasowanie tym samym szablonem.
# c Zaobserwuj, czy detekcja zadziałała poprawnie.

import cv2
import imutils

template = cv2.imread("fanta_logo.png")
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

for scale in [0.5, 1.5]:
    image = cv2.imread("fanta.jpg")
    resized = imutils.resize(image, width=int(image.shape[1] * scale))
    imageGray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    if templateGray.shape[0] > imageGray.shape[0] or templateGray.shape[1] > imageGray.shape[1]:
        scale_factor = min(imageGray.shape[1] / templateGray.shape[1], imageGray.shape[0] / templateGray.shape[0])
        new_size = (int(templateGray.shape[1] * scale_factor), int(templateGray.shape[0] * scale_factor))
        templateGray = cv2.resize(templateGray, new_size, interpolation=cv2.INTER_AREA)

    result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)
    (_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

    startX, startY = maxLoc
    endX = startX + template.shape[1]
    endY = startY + template.shape[0]

    cv2.rectangle(resized, (startX, startY), (endX, endY), (255, 0, 0), 3)
    print(f"Skala {scale} - maxVal: {maxVal}")
    cv2.imshow(f"Skalowany obraz {scale}", resized)
    cv2.waitKey(0)

cv2.destroyAllWindows()
