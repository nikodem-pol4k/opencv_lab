import cv2
# Zamiana wartości piksela na czarny
# a. Pobierz od użytkownika współrzędne (x, y) .
# b. Stwórz walidację, która zweryfikuje czy podane współrzędne nie
# wychodzą poza wymiar zdjęcia.
# c. Ustaw piksel w tym miejscu na czarny (0, 0, 0) .

x = input('Podaj wspolrzedne x: ')
y = input('Podaj wspolrzedne y: ')
image = cv2.imread('./kot.jpg')
(h, w) = image.shape[:2]
if int(x) <= h and int(y) <= w:
    print('Wspolrzedne sa poprawne. Piksel zamieniony na czarny')
    image[int(x), int(y)] = (0, 0, 0)
    cv2.imshow("Changed", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Niepoprawne wspolrzedne.')