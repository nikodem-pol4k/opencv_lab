# Połącz wiedzę z poprzednich zajęć o konturach i template matchingu.
# a Najpierw znajdź obiekty za pomocą konturów ( cv2.findContours ).
# b Dla każdego z wyciętych fragmentów wykonaj template matching –
# porównaj z szablonem.
# c Zidentyfikuj, które obiekty są podobne do wzorca.

import cv2
import numpy as np
import imutils


image = cv2.imread("kostka.png")
resized = imutils.resize(image, width=300)
ratio = image.shape[0] / float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)

print(f"Liczba konturów: {len(cnts)}")

template_contour = cnts[0]
x, y, w, h = cv2.boundingRect(template_contour)
template = gray[y:y+h, x:x+w]

min_similarity = 0.7 
for i, c in enumerate(cnts):
    x, y, w, h = cv2.boundingRect(c)
    roi = gray[y:y+h, x:x+w]
    try:
        roi_resized = cv2.resize(roi, (template.shape[1], template.shape[0]))
        result = cv2.matchTemplate(roi_resized, template, cv2.TM_CCOEFF_NORMED)
        _, maxVal, _, _ = cv2.minMaxLoc(result)
    except:
        print(f"Za mały kontur: {i}")
        continue

    if maxVal >= min_similarity:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(image, f"{maxVal:.2f}", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
        print(f"Kontur {i}: podobieństwo = {maxVal:.2f} -> dziala")
    else:
        print(f"Kontur {i}: podobieństwo = {maxVal:.2f}")

cv2.imshow("Dopasowane", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
