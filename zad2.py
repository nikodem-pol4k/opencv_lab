import cv2

file_name = './kot.jpg'
image = cv2.imread(file_name)
if image is None:
    print("Błąd: nie można wczytać obrazu!")
else:
    print("Obraz wczytano poprawnie.")

# 2. Wczytaj zdjęcie w kolorze i wyświetl liczbę kanałów
(h, w, c) = image.shape[:3]
print(f'width: {w} pixels')
print(f'height: {h} pixels')
print(f'channels: {c}')
