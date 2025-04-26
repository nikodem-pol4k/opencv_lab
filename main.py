import cv2
import numpy as np

# draw a rectangle
rectangle = np.zeros((300, 300), dtype="uint8")
cv2.rectangle(rectangle, (25, 25), (275, 275), 255, -1)
# cv2.imshow("Rectangle", rectangle)

# draw a circle
circle = np.zeros((300, 300), dtype="uint8")
cv2.circle(circle, (150, 150), 150, 255, -1)
# cv2.imshow("Circle", circle)

# draw a triangle
triangle = np.zeros((300, 300, 1), np.uint8) * 255

pt1 = (150, 30)
pt2 = (30, 270)
pt3 = (270, 270)

triangle_cnt = np.array([pt1, pt2, pt3])
cv2.drawContours(triangle, [triangle_cnt], 0, (255, 255, 255), -1)

# cv2.imshow("triangle", triangle)
# cv2.waitKey()


def zad1():
    image = cv2.bitwise_and(circle, triangle)
    cv2.imshow("Image 1 and", image)
    image = cv2.bitwise_or(circle, triangle)
    cv2.imshow("Image 1 or", image)
    image = cv2.bitwise_xor(circle, triangle)
    cv2.imshow("Image 1 xor", image)
    image = cv2.bitwise_not(image)
    cv2.imshow("Image 1 not", image)
    cv2.waitKey()


def zad2():
    image1 = cv2.imread(".\\pic1.jpg")
    image2 = cv2.imread(".\\pic2.jpg")

    im_xor = cv2.bitwise_xor(image1, image2)
    cv2.imshow("Image 2", im_xor)
    cv2.waitKey()

zad1()
zad2()