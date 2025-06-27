import cv2

file_name = './kot.jpg'
image = cv2.imread(file_name)
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

# 3. Wczytaj zdjęcie w odcieniach szarości i wyświetl liczbę kanałów.
image_gray = cv2.imread(file_name, cv2.IMREAD_GRAYSCALE)
(h_grey, w_grey, c_grey) = image.shape[:3]
print(f'channels grey: {c_grey}')
