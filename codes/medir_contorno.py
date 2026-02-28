import cv2
import numpy as np
import my_functions

path = "images/banana_iluminada.jpeg"

if __name__ == "__main__":

    imageGray  = my_functions.readImage(path, 0)

    imageBinary = my_functions.binaryImageGray(
        imageGray, 165, cv2.THRESH_BINARY
    )

    # Encontrar contornos
    contours, _ = cv2.findContours(imageBinary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Tomar el contorno más grande (objeto principal)
    c = max(contours, key=cv2.contourArea)

    # Ajustar una elipse al contorno
    ellipse = cv2.fitEllipse(c)

    # ellipse = ((x,y), (major_axis, minor_axis), angle)
    (x, y), (MA, ma), angle = ellipse

    print("Centro:", (x, y))
    print("Eje mayor:", MA)
    print("Eje menor:", ma)
    print("Ángulo de rotación:", angle)

    # Dibujar la elipse sobre la imagen original
    imageColor = my_functions.readImage(path, 1)
    cv2.ellipse(imageColor, ellipse, (0,255,0), 2)

    cv2.imshow("Elipse ajustada", imageColor)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
