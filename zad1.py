import cv2

# 1. Wczytaj i wyświetl obraz z podanej przez siebie ścieżki. Sprawdź, co się stanie, gdy podasz błędną ścieżkę.
file_name = './kot.jpg'
image = cv2.imread(file_name)
cv2.imshow("Wyświetlony obraz", image) # Tworzy okno i wyświetla obraz
cv2.waitKey(0) # Czeka na dowolny klawisz, by zamknąć okno
cv2.destroyAllWindows() # Zamknięcie wszystkich okien

file_name = 'nie istnieje.jpg'
image = cv2.imread(file_name)