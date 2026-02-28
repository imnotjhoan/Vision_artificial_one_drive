import numpy as np
import cv2

def readImage(path,type):
    return cv2.imread(path,type)

def showImage(name,image, size=(700,900)):
    cv2.imshow(name,cv2.resize(image, size))

def closeImage(t):
    cv2.waitKey(t) # espera hasta que se presione una tecla
    cv2.destroyAllWindows # cierra todas las ventanas abiertas

def binaryImageGray(imageGray, threshold=128,Type=cv2.THRESH_BINARY):
    # Obtener dimensiones correctas de imageGray
    h, w = imageGray.shape
    return cv2.threshold(imageGray, threshold, 255, Type)[1] #INVESTIGAR QUÉ HACE Y CÓMO FUNCIONA ESTA FUNCIÓN

def binaryImageColor(img,u,type):
    #Funcion para cambiar de espacios de color 
    img= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #Leo la imagen a color y la paso a gris 
    return binaryImageGray(img,u, type)

def binaryImageColorBGR(img,lowerb,upperb, type=cv2.THRESH_BINARY):
    #Funcion para cambiar de espacios de color 
    img_hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #Leo la imagen a color y la paso a HSV 
    mask = cv2.inRange(img_hsv, lowerb, upperb)
    return mask
    #Al momento de identificar algo siempre debe ser blanco el objetivo, por lo cual si no aparece así uso 

# bgr del profe------------------------------------------------
def binaryImageColorBgr2(img,val_min,val_max):  
    return cv2.inRange(img,val_min,val_max)

def binaryImageColorHsv (img,val_min,val_max):  
    img_hsv= cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #Leo la imagen a color y la paso a HSV 
    return cv2.inRange(img_hsv,val_min,val_max)

# conversor de imagenes BGR a HSV
def convertBgrToHsv(img):
    return cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

#conversor de imagenes GRAY a BGR
def convertGrayToColor(img):
    return cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

def createTrackbar():
    cv2.namedWindow("trackbars", cv2.WINDOW_NORMAL)
    cv2.createTrackbar("Min H", "trackbars", 0, 255, lambda x: None)
    cv2.createTrackbar("Min S", "trackbars", 0, 255, lambda x: None)
    cv2.createTrackbar("Min V", "trackbars", 0, 255, lambda x: None)
    cv2.createTrackbar("Max H", "trackbars", 255, 255, lambda x: None)
    cv2.createTrackbar("Max S", "trackbars", 255, 255, lambda x: None)
    cv2.createTrackbar("Max V", "trackbars", 255, 255, lambda x: None)

def getTrackbarValues():
    min_h = cv2.getTrackbarPos("Min H", "trackbars")
    min_s = cv2.getTrackbarPos("Min S", "trackbars")
    min_v = cv2.getTrackbarPos("Min V", "trackbars")
    max_h = cv2.getTrackbarPos("Max H", "trackbars")
    max_s = cv2.getTrackbarPos("Max S", "trackbars")
    max_v = cv2.getTrackbarPos("Max V", "trackbars")
    return (min_h, min_s, min_v), (max_h, max_s, max_v)