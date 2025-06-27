# Przetestuj kilka metod z cv2.matchTemplate i porównaj wyniki.
# a Użyj wszystkich sześciu metod:
# cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
# cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED.
# b Narysuj wykryty prostokąt.
# c Wypisz wartości dopasowania.
# d Która metoda działa najlepiej w Twoim przypadku?
import cv2

image = cv2.imread('fanta.jpg')
template = cv2.imread('fanta_logo.png')
imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

if templateGray.shape[0] > imageGray.shape[0] or templateGray.shape[1] > imageGray.shape[1]:
    scale_factor = min(imageGray.shape[1] / templateGray.shape[1], imageGray.shape[0] / templateGray.shape[0])
    new_size = (int(templateGray.shape[1] * scale_factor), int(templateGray.shape[0] * scale_factor))
    templateGray = cv2.resize(templateGray, new_size, interpolation=cv2.INTER_AREA)
    result = cv2.matchTemplate(imageGray, templateGray, cv2.TM_CCOEFF_NORMED)

methods = [
    cv2.TM_CCOEFF,
    cv2.TM_CCOEFF_NORMED,
    cv2.TM_CCORR,
    cv2.TM_CCORR_NORMED,
    cv2.TM_SQDIFF,
    cv2.TM_SQDIFF_NORMED
]

for method in methods:
    result = cv2.matchTemplate(imageGray, templateGray, method)
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        topLeft = minLoc
    else:
        topLeft = maxLoc

    bottomRight = (topLeft[0] + template.shape[1], topLeft[1] + template.shape[0])
    clone = image.copy()
    cv2.rectangle(clone, topLeft, bottomRight, (0, 255, 0), 2)

    print(f"Metoda {method} => maxVal: {maxVal}")
    cv2.imshow(f"Metoda {method}", clone)
    cv2.waitKey(0)

cv2.destroyAllWindows()
