import cv2
import numpy as np

img_color = cv2.imread(r"C:\Users\jhoan\OneDrive - Universidad EIA\Semestres\10 semestre (2026_1)\Vision_artificial\coppelia_contorno\images\a2.jpeg", 1)
img_color =cv2.resize(img_color, (640,480))

img_gray  = cv2.imread(r"C:\Users\jhoan\OneDrive - Universidad EIA\Semestres\10 semestre (2026_1)\Vision_artificial\coppelia_contorno\images\a2.jpeg", 0)

img_gray =cv2.resize(img_gray, (640,480))  


cv2.imshow("img_color", img_color)
cv2.waitKey(0)

ret, imgBin = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) ##valor que me diferencia uno de otro en la misma imagen por eso 
                                                                                   ##no se le pone el umbral, el se lo asigna     
                                                                                   ##ret es el umbral calculado por otsu 

##print(ret)
cv2.imshow("img_bin", imgBin)
cv2.waitKey(0)

cnts, hie = cv2.findContours(imgBin.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)                               ###CHAIN_APPROX_NONE, me tare todos los valores de xy del contorno
##cnt,lista de todos los contornos ##img binarizada  ##hierarchy(jerarquia,no se usa,buscar lo que devuelve)    ##CHAIN_APPROX_NONE_SIMPLE,me tra solo unos puntos con lo cuales se puede crear ese contorno
##hie,jerquia                                        ##tree(me da jerarquia)                                    
                                                     ##list(traer info)
                                                     ##external(90%de los cosos)


h, w = img_color.shape[:2]                 ##extraigo mi tamaño, el .shape=(640,480,3) ##la funcion len() me dice cuantas posiciones tiene una lista
imagen_cnt = 255 * np.zeros((h, w, 3), np.uint8) ###imagen en blanco o negro del mismo tamaño de mi original

for cont in cnts: ##lee contorno por contorno
                 
    x, y, w, h = cv2.boundingRect(cont)                  ###devuelve un rectángulo que encierra el contorno,x, y → coordenadas de la esquina superior izquierda del rectángulo w y h es el ancho y alto
    cv2.rectangle(img_color,(x,y),(x+w,y+h),(255, 0, 0), 2)  ####imagen donde dibujo,origen,coordenada de su diagonal,color,espesor
    
    # ===== CENTROIDE REAL DEL CONTORNO =====
    M = cv2.moments(cont)

    if M["m00"] != 0:  ##por si hay un area que es 0, por la division
        cx = int(M["m10"] / M["m00"])
        cy = int(M["m01"] / M["m00"])    ##m00 → área
                                         #m10 → momento respecto a 
                                         #m01 → momento respecto a Y   
                                    


        # Dibujar centroide en la imagen original
        cv2.circle(img_color, (cx, cy), 15, (10,255,25), -1)  #cv2.circle(imagen, centro, radio, color, grosor)-1 rellena el circulo

    cv2.drawContours(imagen_cnt, cont, -1, (0, 0, 255), 2)   ##imagen a color donde se dibujara el contorno-contornos encontrados -dibujar contornos(<0 todos los contornos)- color-espsesor(entre1 y 3)

    cv2.imshow("imagen_cnt", imagen_cnt)
    cv2.imshow("imagen_color", img_color)
    cv2.waitKey(0)

cv2.destroyAllWindows()


    