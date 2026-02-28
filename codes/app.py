import numpy as np
import cv2

#usar funciones de otro archivo
import my_functions

path="images/5.jpeg"

if __name__ == "__main__":
    imageColor = my_functions.readImage(path,1) # Leer imagen a color
    imageGray = my_functions.readImage(path,0)  # Leer imagen en escala de grises
    my_functions.showImage("Imagen a color", imageGray) # Mostrar imagen en escala de grises
    my_functions.closeImage(0)
## -------------------------------Conversión a binario------------------------------
        
    imageBinary = my_functions.binaryImageGray(imageGray,223,cv2.THRESH_BINARY) # Convertir imagen de gris a binario
    my_functions.showImage("Imagen binaria", imageBinary) # Mostrar imagen binaria
    my_functions.closeImage(0)
    