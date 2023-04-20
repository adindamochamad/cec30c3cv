import cv2
import numpy as np

png1=cv2.imread("zevalente.jpg")
png2=cv2.imread("zevalente.jpg")

horizontalwindow=np.concatenate((png1, png2), axis=1)
verticalwindow=np.concatenate((png1, png2), axis=0)

cc2=(horizontalwindow,verticalwindow)
cv2.imshow("HORIZONTAL", cc2)

cv2.waitKey(0)
cv2.destroyAllWindows()