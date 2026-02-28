import cv2
import numpy as np
img_color = cv2.imread("images/1.png", 1)
img_gray = cv2.imread("images/1.png", 0)
cv2.imshow("img_color", img_color)
cv2.waitKey(0)
ret, imgBin = cv2.threshold(img_gray, 0,255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
cv2.imshow("img_bin", imgBin)
cv2.waitKey(8)
cnts, hie = cv2.findContours(imgBin.copy(), cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
h,w = img_color.shape[:2]
imagen_cnt = 255*np.zeros((h,w,3), np.uint8)
for cont in cnts:
x,y,w,h = cv2.boundingRect(cont)
cv2.rectangle(img_color, (x,y), (x+w, y+h), (255,0,255),2)
cv2.drawContours(imagen_cnt, cont,-1, (0,0,255),2)
cv2.imshow("imagen_cnt", imagen_cnt)
cv2.imshow("img_color",img_color)
cv2.waitKey(0)
cv2.destroyAllWindows()