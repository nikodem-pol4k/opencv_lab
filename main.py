import cv2

image = cv2.imread("bird.jpg")


def zad1():
    cv2.imshow("Zad1", image)
    (B, G, R) = cv2.split(image)
    cv2.imshow('Blue Channel', B)
    cv2.imshow('Green Channel', G)
    cv2.imshow('Red Channel', R)
    cv2.waitKey()


def zad2():
    ...


def zad3():
    ...


def zad4():
    ...


def zad5():
    ...


def zad6():
    ...

zad1()
# zad2()
# zad3()
# zad4()
# zad5()
# zad6()