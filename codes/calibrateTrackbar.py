# se va a utilizar para obtener los valores minimos y maximos de los canales BGR y HSV
import numpy as np
import cv2

#usar funciones de otro archivo
import my_functions

path="images/banana_iluminada.jpeg"
path="images/5.jpeg"

if __name__ == "__main__":
    imageColor = my_functions.readImage(path,1) # Leer imagen a color

    my_functions.showImage("Imagen a color", imageColor) # Mostrar imagen a color
    
    imageHsv= my_functions.convertBgrToHsv(imageColor)
    my_functions.createTrackbar()
    while True:
        list_values = my_functions.getTrackbarValues()

        print(list_values)
        imageBinaryHSV = my_functions.binaryImageColorHsv(imageColor,list_values[0],list_values[1]) # Convertir imagen de color a binario
        my_functions.showImage("Imagen binaria HSV", imageHsv)
        my_functions.showImage("Imagen binaria HSV", imageBinaryHSV)

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Salir con la tecla 'q'
            break