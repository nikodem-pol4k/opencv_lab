import cv2

# 6. Zmień rozmiar okna wyświetlania obrazu tak, by dostosować je do różnych ekranów, np. cv2.WINDOW_NORMAL - znajdź w dokumentacji odpowiednią funkcję do tego.
fname1 = './kot.jpg'
image1 = cv2.imread(fname1)
cv2.namedWindow("KOT", cv2.WINDOW_NORMAL)
cv2.imshow("KOT", image1)
cv2.waitKey(0)
cv2.destroyAllWindows() 
