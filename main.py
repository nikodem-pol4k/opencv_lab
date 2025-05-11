import cv2
import os
import numpy as np


def zad1():
    img = cv2.imread('kostka.PNG')

    height, width = img.shape[:2]
    new_width = 300
    scale = new_width / width
    new_height = int(height * scale)
    resized_img = cv2.resize(img, (new_width, new_height))

    gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    threshold_values = [100, 140, 180]
    for t in threshold_values:
        _, thresh = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
        cv2.imshow(f'Progowanie {t}', thresh)

    cv2.imshow('Oryginalny obraz (przeskalowany)', resized_img)

    cv2.waitKey(0)


def zad2():
    img = cv2.imread('kostka.PNG')

    height, width = img.shape[:2]
    new_width = 300
    scale = new_width / width
    new_height = int(height * scale)
    resized_img = cv2.resize(img, (new_width, new_height))

    gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

    _, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    contour_img = resized_img.copy()
    cv2.drawContours(contour_img, contours, -1, (0, 0, 255), 2)  # kolor czerwony, grubość 2px

    cv2.imshow('Kontury', contour_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad3():
    img = cv2.imread('kostka.PNG')

    widths = [100, 200, 300, 400]

    threshold_value = 140

    for width in widths:
        height, orig_width = img.shape[:2]
        scale = width / orig_width
        new_height = int(height * scale)
        resized_img = cv2.resize(img, (width, new_height))

        gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)

        _, thresh = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        contour_img = resized_img.copy()
        cv2.drawContours(contour_img, contours, -1, (0, 0, 255), 2)

        print(f"Szerokość: {width}px -> Liczba wykrytych konturów: {len(contours)}")
        cv2.imshow(f'Kontury przy szerokości {width}px', contour_img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad4():

    img = cv2.imread('kostka.PNG')
    height, width = img.shape[:2]
    scale = 300 / width
    new_height = int(height * scale)
    resized_img = cv2.resize(img, (300, new_height))
    gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    numbered_img = resized_img.copy()

    output_folder = "kostki"
    os.makedirs(output_folder, exist_ok=True)

    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)

        cx = x + w // 2
        cy = y + h // 2

        cv2.putText(numbered_img, str(i + 1), (cx - 10, cy - 10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.5, (0, 255, 0), 1, cv2.LINE_AA)

        cv2.drawContours(numbered_img, [contour], -1, (0, 0, 255), 2)

        cut_tile = resized_img[y:y + h, x:x + w]
        filename = os.path.join(output_folder, f'kostka_{i + 1:02d}.png')
        cv2.imwrite(filename, cut_tile)

    cv2.imshow('Obraz z numerami kostek', numbered_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad5():
    img = cv2.imread('kostka.PNG')

    height, width = img.shape[:2]
    scale = 300 / width
    new_height = int(height * scale)
    resized_img = cv2.resize(img, (300, new_height))

    gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    measured_img = resized_img.copy()

    output_folder = "kostki"
    os.makedirs(output_folder, exist_ok=True)


    for i, contour in enumerate(contours):
        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(measured_img, (x, y), (x + w, y + h), (255, 0, 0), 2)

        label = f"{w}x{h} px"
        cv2.putText(measured_img, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX,
                    0.4, (0, 255, 0), 1, cv2.LINE_AA)

        cut_tile = resized_img[y:y + h, x:x + w]
        filename = os.path.join(output_folder, f'kostka_{i + 1:02d}.png')
        cv2.imwrite(filename, cut_tile)

    cv2.imshow('Wymiary kostek', measured_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad6():
    img = cv2.imread('kostka.PNG')
    img = cv2.resize(img, (300, int(img.shape[0] * 300 / img.shape[1])))  # skalowanie
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


    min_area = 3000
    max_area = 5000

    filtered_img = img.copy()

    for contour in contours:
        area = cv2.contourArea(contour)
        if min_area <= area <= max_area:
            cv2.drawContours(filtered_img, [contour], -1, (0, 0, 255), 2)  # czerwone kontury

    cv2.imshow('Kontury po filtracji powierzchni', filtered_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def zad7():
    img = cv2.imread('kostka.PNG')

    height, width = img.shape[:2]
    scale = 300 / width
    new_height = int(height * scale)
    resized_img = cv2.resize(img, (300, new_height))

    gray = cv2.cvtColor(resized_img, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    annotated_img = resized_img.copy()

    output_folder = "kostki"
    os.makedirs(output_folder, exist_ok=True)

    min_area = 500
    max_area = 5000

    widths = []
    heights = []

    index = 1

    for contour in contours:
        area = cv2.contourArea(contour)
        if area < min_area or area > max_area:
            continue

        x, y, w, h = cv2.boundingRect(contour)

        widths.append(w)
        heights.append(h)

        cv2.rectangle(annotated_img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        label = f"{w}x{h}px"
        cv2.putText(annotated_img, label, (x, y - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

        cut_tile = resized_img[y:y + h, x:x + w]
        filename = os.path.join(output_folder, f'kostka_{index:02d}.png')
        cv2.imwrite(filename, cut_tile)

        index += 1

    if widths and heights:
        print("\n=== RAPORT ===")
        print(f"Liczba wykrytych kostek: {len(widths)}")
        print(f"Średnia szerokość: {np.mean(widths):.2f} px")
        print(f"Średnia wysokość: {np.mean(heights):.2f} px")
        print(f"Minimalny rozmiar: {min(widths)}x{min(heights)} px")
        print(f"Maksymalny rozmiar: {max(widths)}x{max(heights)} px")
    else:
        print("Nie wykryto żadnych kostek spełniających kryteria.")

# zad1()  # 140 najlepsze
# zad2()  # cv2.RETR_EXTERNAL najlepsz - najmniej błedów
# zad3()
# zad4()
# zad5()
# zad6()
zad7()