import cv2
import numpy as np

img_color = cv2.imread(r"C:\Users\jhoan\OneDrive - Universidad EIA\Semestres\10 semestre (2026_1)\Vision_artificial\coppelia_contorno\images\a2.jpeg", 1)
img_gray  = cv2.imread(r"C:\Users\jhoan\OneDrive - Universidad EIA\Semestres\10 semestre (2026_1)\Vision_artificial\coppelia_contorno\images\a2.jpeg", 0)

# Ventana correctamente definida
cv2.namedWindow("img_color", cv2.WINDOW_NORMAL)
cv2.resizeWindow("img_color", 800, 600)
cv2.imshow("img_color", img_color)
cv2.waitKey(0)

ret, imgBin = cv2.threshold(img_gray, 0, 255,cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

cnts, _ = cv2.findContours(imgBin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

H, W = img_color.shape[:2]
imagen_cnt = np.zeros((H, W, 3), np.uint8)

for cont in cnts:
    x, y, w_box, h_box = cv2.boundingRect(cont)
    cv2.rectangle(img_color, (x, y), (x + w_box, y + h_box), (255, 0, 255), 2)
    cv2.drawContours(imagen_cnt, [cont], -1, (0, 0, 255), 2)

# Ventanas configuradas explícitamente
cv2.namedWindow("img_color", cv2.WINDOW_NORMAL)
cv2.namedWindow("imagen_cnt", cv2.WINDOW_NORMAL)

cv2.resizeWindow("img_color", 800, 600)
cv2.resizeWindow("imagen_cnt", 800, 600)

# Mostrar
cv2.imshow("img_color", img_color)
cv2.imshow("imagen_cnt", imagen_cnt)
cv2.waitKey(0)
cv2.destroyAllWindows()