import cv2
import numpy as np


def zad1():
    image = cv2.imread("dwight.jpg")
    cv2.imshow("Original", image)

    mask = np.zeros(image.shape[:2], dtype="uint8")
    cv2.rectangle(mask, (260, 5), (450, 240), 255, -1)

    masked = cv2.bitwise_and(image, image, mask=mask)
    cv2.imshow("Mask Applied to Image", masked)

    cv2.waitKey()

def zad2():
    image = cv2.imread("dwight.jpg")
    cv2.imshow("Original", image)
    mask = np.zeros(image.shape[:2], dtype="uint8")

    top_left = (260, 90)
    bottom_right = (380, 140)
    cv2.rectangle(mask, top_left, bottom_right, 255, -1)
    inverted_mask = cv2.bitwise_not(mask)

    masked = cv2.bitwise_and(image, image, mask=inverted_mask)
    cv2.imshow("Mask Applied to Image", masked)

    cv2.waitKey()


def zad3():
    image = cv2.imread('dwight.jpg')

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 120, 70])
    upper_red = np.array([10, 255, 255])

    mask = cv2.inRange(hsv_image, lower_red, upper_red)

    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow('Original Image', image)
    cv2.imshow('Masked Image', result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

# zad1()
# zad2()
zad3()