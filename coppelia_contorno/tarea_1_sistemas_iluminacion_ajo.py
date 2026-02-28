import numpy as np
import cv2
import math

#usar funciones de otro archivo
import my_functions


 
if __name__ == "__main__":

    
    # ajo iluminado--------------------------------------------------------------
    path=r"C:\Users\jhoan\OneDrive - Universidad EIA\Semestres\10 semestre (2026_1)\Vision_artificial\coppelia_contorno\images\a1.jpeg"
    imageColor = my_functions.readImage(path,1)  # Leer imagen a color
    imageGray = my_functions.readImage(path,0)  # Leer imagen en escala de grises
    my_functions.showImage("Imagen a escala de grises", imageGray) # Mostrar imagen en escala de grises
    my_functions.closeImage(0)
    ## -------------------------------Conversión a binario------------------------------
        
    imageBinary = my_functions.binaryImageGray(imageGray,135,cv2.THRESH_BINARY) # Convertir imagen de gris a binario
    my_functions.showImage("Imagen binaria", imageBinary) # Mostrar imagen binaria
    my_functions.closeImage(0)
    
    h,w=imageBinary.shape[:2]
    # Guardar la imagen binaria
    cv2.imwrite("images/ajo_binario.jpeg", imageBinary)
 

    # -------------------------------Encontrar contornos y ejes sin herramientas de cv2------------------------------
    #vector horizonal
    v_h=[]
    #vector vertical
    v_v=[]
    #vector horizonal
    v_h2=[]
    #vector vertical
    v_v2=[]

# recorer la imagen binaria por filas y columnas
    for i in range(h):
        for j in range(w):
            # solo guarde los pixeles blancos que no sean falsos positivos
            if imageBinary[i,j]==255 and imageBinary[i,j-4]!=0 and imageBinary[i,j+4] != 0 and imageBinary[i-4,j]!=0 and imageBinary[i+4,j]!=0:  # Pixel blanco
                v_h.append(j)  # Guardar la posición horizontal
                v_v.append(i)  # Guardar la posición vertical
            
                
# recorrer la imagen binaria por columnas y filas    
    for j in range(w):
        for i in range(h):
            # solo guarde los pixeles blancos que no sean falsos positivos
            if imageBinary[i,j]==255 and imageBinary[i,j-4]!=0 and imageBinary[i,j+4] != 0 and imageBinary[i-4,j]!=0 and imageBinary[i+4,j]!=0:  # Pixel blanco
                v_h2.append(j)  # Guardar la posición horizontal
                v_v2.append(i)  # Guardar la posición vertical            
    
    # Dibujar los ejes en la imagen a color
    cv2.line(imageColor,(v_h[0],v_v[0]),(v_h[-1],v_v[-1]),(255, 0, 0), 10)
    cv2.line(imageColor,(v_h2[0],v_v2[0]),(v_h2[-1],v_v2[-1]),(0, 0, 255), 10)
    
    my_functions.showImage("Ejes dibujados sin cv2", imageColor)
    my_functions.closeImage(0)
    
    # formula distancia entre dos puntos
    distancia_eje1 = math.sqrt((v_h[-1] - v_h[0])**2 + (v_v[-1] - v_v[0])**2)
    distancia_eje2 = math.sqrt((v_h2[-1] - v_h2[0])**2 + (v_v2[-1] - v_v2[0])**2)
    

    #imprimir valores de los ejes mayor y menor
    if distancia_eje1>distancia_eje2:
        print("Eje mayor:", distancia_eje1)
        print("Eje menor:", distancia_eje2)
    else:
        print("Eje mayor:", distancia_eje2)
        print("Eje menor:", distancia_eje1)
    