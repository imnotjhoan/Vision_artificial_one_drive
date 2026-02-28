# Librería de procesamiento de imágenes
import cv2

#Ruta relativa de la imagen
path = "images/5.jpeg"


#---------------------funcion para cargar una imagen en color-----------------------

imageColor = cv2.imread(path,1) # cuando tiene la bandera en 1 carga la imagen en color
# imprimir pixeles de la imagen
#print(imageColor)

# imprimir tamaño de la imagen
w,h = imageColor.shape[:2] # obtener ancho y alto ( se puede obtener alto, ancho y gama de colores)
print(h, w)

#acceso al valor del primer pixel de la imagen
pix1 = imageColor[0,0]
print("Valor del primer pixel (BGR): ", pix1)
# primer componente de color (azul)
print("Componente azul del primer pixel: ", pix1[0])

#-----------------------leer una imagen en escala de grises-----------------------
imageGray = cv2.imread(path,0) # cuando tiene la bandera en 0 carga la imagen en escala de grises
#print(imageGray)
# imprimir el primer pixel de la imagen en escala de grises
pix2 = imageGray[0,0]
print("Valor del primer pixel en escala de grises: ", pix2)

#-----------------------mostrar las imagenes cargadas-----------------------
cv2.imshow("Mi primera imagen a color", imageColor) #mouestra imagen sin redimensionar

cv2.imshow("Mi primera imagen a color",cv2.resize(imageColor, (1200, 800))) #mostrar imagen redimensionada
cv2.waitKey(0) # espera hasta que se presione una tecla
cv2.destroyAllWindows() # cierra todas las ventanas abiertas

   



