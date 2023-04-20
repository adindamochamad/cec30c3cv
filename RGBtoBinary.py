import cv2
import numpy as np
import matplotlib.pyplot as plt

jpgmentah=cv2.imread('zevalente.jpg')
w=int(jpgmentah.shape[1]*50/100)
h=int(jpgmentah.shape[0]*50/100)
newdimension=(w,h)

resize=cv2.resize(jpgmentah, newdimension, interpolation =cv2.INTER_AREA)

#grayscale
imggray=cv2.cvtColor(resize, cv2.COLOR_BGR2GRAY)

#binary
threshold=127
ret, imgbiner=cv2.threshold(imggray,threshold,255,cv2.THRESH_BINARY)

cv2.imshow("RGB Image", resize)
cv2.imshow("Grayscale", imggray)
cv2.imshow("Biner", imgbiner)

cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.subplot(131),plt.imshow(imgRGB,cmap = 'gray'),plt.title('Original Image'), plt.axis('off')
#plt.subplot(132),plt.imshow(imgbinary, cmap="gray"),plt.title('Binary'), plt.axis('off')
