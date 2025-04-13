import cv2



## Zad 1
def zad1():
    img = cv2.imread('img.png')


    roi = img[0:100, 0:100]

    cv2.imshow('ROI - Upper left', roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

## Zad 2
def zad2():
    img = cv2.imread('img.png')

    height = img.shape[0]

    half = height // 2
    lower_half = img[half:, :]

    cv2.imshow('Lower half', lower_half)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


## Zad 3
def zad3():
    img = cv2.imread('img.png')

    width = img.shape[1]

    half = width // 2
    right_half = img[:, half:]

    cv2.imshow('Right half', right_half)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

## Zad 4
def zad4():
    img = cv2.imread('img.png')

    height, width = img.shape[:2]
    print(f'Image dimesions: width={width}, height={height}')

    startX = int(input("Provide startX (0 - {}): ".format(width)))
    endX = int(input("Provide endX ({} - {}): ".format(startX + 1, width)))

    startY = int(input("Provide startY (0 - {}): ".format(height)))
    endY = int(input("Provide endY ({} - {}): ".format(startY + 1, height)))

    if startX < 0 or endX > width or startY < 0 or endY > height or startX >= endX or startY >= endY:
        print("Incorrect coordinates!")
    else:
        roi = img[startY:endY, startX:endX]

        cv2.imshow('Chosen image part (ROI)', roi)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


## Zad 5
def zad5():
    img = cv2.imread('img_face.png')
    # roi = img[startY:endY, startX:endX]
    roi = img[5:70, 110:165]
    cv2.imshow('Face', roi)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

## Zad 6
def zad6():
    img = cv2.imread('img.png')
    fragment = img[0:100, 0:100]

    height, width = img.shape[:2]

    startY = height - 150
    startX = width - 170

    img[startY:startY + 100, startX:startX + 100] = fragment

    cv2.imshow('Image after modifications', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

## Zad 7
def zad7():
    img = cv2.imread('img.png')
    height, width = img.shape[:2]

    cell_height = height // 3
    cell_width = width // 3

    count = 1

    for row in range(3):
        for col in range(3):
            y1 = row * cell_height
            y2 = y1 + cell_height
            x1 = col * cell_width
            x2 = x1 + cell_width

            cell = img[y1:y2, x1:x2]

            window_name = f'Fragment {count}'
            cv2.imshow(window_name, cell)
            count += 1

    cv2.waitKey(0)
    cv2.destroyAllWindows()

## Zad 8
def zad8():
    img = cv2.imread('img_1.png')
    roi_width = 600
    roi_height = img.shape[0]
    max_shift = img.shape[1] - roi_width
    x = 0

    while x <= max_shift:
        roi = img[0:roi_height, x:x + roi_width]
        cv2.imshow('Animated ROI', roi)
        key = cv2.waitKey(0)
        if key == 27:  # ESC
            break
        x += 10

    cv2.destroyAllWindows()

## Zad 9
def zad9():
    img = cv2.imread('img_1.png')

    cropped = img[0:300, 0:300]

    cv2.imwrite('cropped_image.jpg', cropped)

    cv2.imshow('Cropped Image', cropped)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# zad1()
# zad2()
# zad3()
# zad4()
# zad5()
# zad6()
# zad7()
zad8()
# zad9()