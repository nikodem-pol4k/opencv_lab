# Zastosowanie odbicia na wybranym obszarze
# a. Wczytaj obraz i wytnij z niego fragment (np. środek obrazu lub prawą
# połowę).
# b. Odbij tylko wycięty fragment i wklej go z powrotem do obrazu.

import cv2 

image = cv2.imread("image.jpg")
image_cropped = image[400:1400, 200:800]
image_cropped_flipped = cv2.flip(image_cropped, 1)
image[400:1400, 200:800] = image_cropped_flipped
cv2.imshow("Cropped, flipped, pasted", image)
cv2.waitKey(0)