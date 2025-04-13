import cv2
import numpy as np


def zad1():
    img = cv2.imread('img.png')
    M = np.ones(img.shape, dtype="uint8") * 150
    added = cv2.add(img, M)
    cv2.imshow("OpenCV", added)
    cv2.waitKey(0)

    added = img + np.uint8([50])
    cv2.imshow("Numpy", added)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad2():
    img = cv2.imread('img.png')
    M = np.ones(img.shape, dtype="uint8") * 150
    added = cv2.add(img, M)
    cv2.imshow("OpenCV", added)
    cv2.waitKey(0)

    added = img + np.uint8([150])
    cv2.imshow("Numpy", added)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad3():
    img = cv2.imread('img.png')
    M = np.ones(img.shape, dtype="uint8") * 150
    added = cv2.subtract(img, M)
    cv2.imshow("OpenCV", added)
    cv2.waitKey(0)

    added = img - np.uint8([150])
    cv2.imshow("Numpy", added)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad4():
    img = cv2.imread('img.png')
    blue = img[:, :, 0]
    green = img[:, :, 2]
    red = img[:, :, 3]

    Mblue = blue + np.ones(img.shape, dtype="uint8") * 30
    Mgreen = green - np.ones(img.shape, dtype="uint8") * 20
    Mred = red + np.ones(img.shape, dtype="uint8") * 10

    modified_img = cv2.merge([Mblue, Mgreen, Mred])
    cv2.imshow("Numpy", modified_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
# zad1()
# zad2()
# zad3()

zad4()