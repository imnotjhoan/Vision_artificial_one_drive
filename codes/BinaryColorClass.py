import numpy as np
import cv2

#usar funciones de otro archivo
import my_functions

path="images/banana_iluminada.jpeg"

if __name__ == "__main__":
    imageColor = my_functions.readImage(path,1) # Leer imagen a color

    my_functions.showImage("Imagen a color", imageColor) # Mostrar imagen a color
    my_functions.closeImage(0)
## -------------------------------Conversión a binario------------------------------
        
    imageBinary = my_functions.binaryImageColor(imageColor,160,cv2.THRESH_BINARY) # Convertir imagen de color a binario
    my_functions.showImage("Imagen binaria", imageBinary) # Mostrar imagen binaria
    my_functions.closeImage(0)

    imageBinaryBGR = my_functions.binaryImageColorBgr2(imageColor,(3,174,200),(143,253,247)) # Convertir imagen de color a binario
    my_functions.showImage("Imagen binaria BGR", imageBinaryBGR) # Mostrar imagen binaria
    my_functions.closeImage(0)

    imageBinaryHSV = my_functions.binaryImageColorHsv(imageColor,(3,174,200),(143,253,247)) # Convertir imagen de color a binario
    my_functions.showImage("Imagen binaria HSV", imageBinaryHSV) # Mostrar imagen binaria
    my_functions.closeImage(0)

    
    
    