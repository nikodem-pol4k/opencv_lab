import cv2

# 4. Wczytaj obraz w skali szarości i zapisz go jako nowy plik - znajdź w dokumentacji odpowiednią funkcję do tego.
file_name = './kot.jpg'
gray_img = cv2.imread(file_name, 0)
if gray_img is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")
    cv2.imwrite("szary_kot.jpg", gray_img)
