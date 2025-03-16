import numpy as np
import cv2
import imutils

M1 = np.float32([
    [1, 0, 25],
    [0, 1, 50]
])

M2= np.float32([
    [1, 0, -7],
    [0, 1, -23]
])

# load the image and display it to our screen
image = cv2.imread("balloon.jpg")
cv2.imshow("Original", image)

# Zad 1
# shift the image 30 pixels to the right and 50 pixels down
M = np.float32([[1, 0, 30], [0, 1, 40]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Down and Right", shifted)

# Zad 2
# shift the image 20 pixels to the left and 50 pixels up
M = np.float32([[1, 0, -20], [0, 1, -50]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# Zad 3
M = np.float32([[1, 0, -400], [0, 1, -250]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Shifted Up and Left", shifted)

# Zad 4
# No difference between imutils and opencv
shifted = imutils.translate(image, -400, -250)
cv2.imshow("imutils test", shifted)

# Zad 5
x = input("Podaj przesunięcie w pionie: ")
y = input("Podaj przesunięcie w poziomie: ")

M = np.float32([[1, 0, x], [0, 1, y]])
shifted = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
cv2.imshow("Dynamic shifting", shifted)

cv2.waitKey(100000)