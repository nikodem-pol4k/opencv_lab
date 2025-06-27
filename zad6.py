# Zamazywanie szczegółów na zdjęciu
# a. Znajdź w Internecie profilowe zdjęcie osoby.
# b. Czerwonymi kołami “zasłoń” osobie na zdjęciu oczy.
# c. Zielonym prostokątem “zasłoń” osobie na zdjęciu usta.
# d. Niebieskim okręgiem obejmij dookoła twarz osoby.

import cv2 

fname = 'thispersondoesnotexist.jpg'
image = cv2.imread(fname)
print(image.shape)
red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
cv2.circle(image, (390, 490), 20, red, -1)
cv2.circle(image, (645, 490), 20, red, -1)
cv2.rectangle(image, (390, 700), (650, 800), green, -1)
cv2.circle(image, (530, 512), 350, blue, 10)
cv2.imshow("Canvas", image)
cv2.waitKey(0)