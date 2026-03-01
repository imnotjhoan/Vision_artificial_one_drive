import numpy as np
import cv2
import math

#usar funciones de otro archivo
import my_functions


 
if __name__ == "__main__":

    
    # ajo iluminado--------------------------------------------------------------
    path="Quiz1_jhoan_chacon/images/barras.png"
    imageColor = my_functions.readImage(path,1)  # Leer imagen a color
    imageGray = my_functions.readImage(path,0)  # Leer imagen en escala de grises
    my_functions.showImage("Imagen a escala de grises", imageGray) # Mostrar imagen en escala de grises
    my_functions.closeImage(0)
    ## -------------------------------Conversión a binario------------------------------
        
    imageBinary = my_functions.binaryImageGray(imageGray,50,cv2.THRESH_BINARY) # Convertir imagen de gris a binario
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
    v=0
    index=0
    fin_barras_x=[]
    fin_barras_y=[]
    inicio_barras_x=[]
    inicio_barras_y=[]

# recorer la imagen binaria por filas y columnas
    for i in range(h):
        for j in range(w):
            if imageBinary[i,j]==255 :  # Pixel blanco
                
                v_h.append(j)  # Guardar la posición horizontal
                v_v.append(i)  # Guardar la posición vertical
                v=v+1
                if v==1:
                    index==i
            if i==50 and imageBinary[i,j]==255 and  imageBinary[i,j-1]==255 and  imageBinary[i,j-4]==255 and  imageBinary[i,j+1]==0 and  imageBinary[i,j+2]==0 :  # Pixel blanco
                fin_barras_x.append(j)
                fin_barras_y.append(i)
            if j<476:
                if i==50 and imageBinary[i,j]==0 and  imageBinary[i,j-1]==0 and  imageBinary[i,j-2]==0 and  imageBinary[i,j+1]==255 and  imageBinary[i,j+2]==255 :  # Pixel blanco
                    inicio_barras_x.append(j)
                    inicio_barras_y.append(i)
          
            
       

    i=0
    conteo_barras=0
    distancia_eje=[]
    while True:
        # cv2.line(imageColor,(inicio_barras_x[i],inicio_barras_y[i]),(fin_barras_x[i],fin_barras_y[i]),(255, 255, 255), 1)
        distancia_eje.append(math.sqrt((fin_barras_x[i]-inicio_barras_x[i])**2 + (fin_barras_y[i]-inicio_barras_y[i])**2))
        if distancia_eje[i]>15:
            conteo_barras+=1
        i=i+1
        if i==16:  # Salir con la tecla 'q'
            break

    i=0
    while True:
        cv2.line(imageColor,(fin_barras_x[i],fin_barras_y[i]),(inicio_barras_x[i+1],inicio_barras_y[i+1]),(0, 255, 0), 2)
        
        i=i+1
        if i==15:  # Salir con la tecla 'q'
            break
    
    print("LA CANTIDAD DE BARRAS ES: ",conteo_barras)
    
    my_functions.showImage("Ejes dibujados sin cv2", imageColor)
    my_functions.closeImage(0)
    