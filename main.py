import cv2
import imutils

image = cv2.imread("balloon.jpg")
cv2.imshow("Original", image)

(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)


# Zad 1
def task1():
    M = cv2.getRotationMatrix2D((cX, cY), 45, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by 45 Degrees", rotated)


# Zad 2
def task2():
    M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by -90 Degrees", rotated)


# Zad 3
def task3():
    M = cv2.getRotationMatrix2D((0, 0), 30, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by -90 Degrees", rotated)


# Zad 4
def task4():
    angle = float(input("Podaj kąt obrotu: "))
    M = cv2.getRotationMatrix2D((cX, cY), angle, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow(f"Rotated by {angle} Degrees", rotated)


# Zad 5
def task5():
    rotated = imutils.rotate(image, 180)
    cv2.imshow(f"Rotated by 180 Degrees", rotated)


# Zad 6
def task6():
    rotated = imutils.rotate_bound(image, -33)
    cv2.imshow(f"Rotated by -33 Degrees", rotated)


# Zad 7
def task7():
    rotated = imutils.rotate(image, 60)
    cv2.imshow(f"Rotated by 60 Degrees - imutils", rotated)

    M = cv2.getRotationMatrix2D((cX, cY), 60, 1.0)
    rotated = cv2.warpAffine(image, M, (w, h))
    cv2.imshow("Rotated by 60 Degrees - wrapAffine", rotated)


# Zad 8
def task8():
    rotated1 = imutils.rotate(image, 30)
    rotated2 = imutils.rotate(rotated1, 30)
    rotated3 = imutils.rotate(rotated2, 30)

    rotated90 = imutils.rotate(image, 90)
    cv2.imshow("Rotated by 3x30 Degrees", rotated3)
    cv2.imshow("Rotated by 90 Degrees", rotated90)


# Zad 9
def task9():
    rotated = imutils.rotate(image, 75)
    cv2.imshow("Rotated by 75 Degrees", rotated)
    cv2.imwrite("rotated_output.jpg", rotated)


# Zad 10
def task10():
    r = range(0, 361, 15)
    for i in r:
        rotated = imutils.rotate(image, i)
        cv2.imshow(f"Rotated by {i} Degrees", rotated)
        cv2.waitKey(500)


# task1()
# task2()
# task3()
# task4()
# task5()
# task6()
# task7()
# task8()
# task9()
task10()


cv2.waitKey(10000)
