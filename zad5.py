import cv2

# 5. Otwórz dwa obrazy jednocześnie w osobnych oknach. Upewnij się, że można je zamknąć niezależnie.
fname1 = './kot.jpg'
fname2 = './kot2.jpg'
image1 = cv2.imread(fname1)
image2 = cv2.imread(fname2)
cv2.imshow("kot", image1)
cv2.imshow("kot 2", image2)
cv2.waitKey(0)
cv2.destroyAllWindows() 
