import cv2
import numpy as np
 
# definir variables globales
drawing = False
x_init, y_init = -1,-1
top_left_pt = (-1,-1)
bottom_right_pt = (-1, -1)
 
def draw_rectangle(event, x, y, flags, params):
    global drawing, x_init, y_init, top_left_pt, bottom_right_pt
 
    if event == cv2.EVENT_LBUTTONDOWN:
        ##Quiero empezar a dibujar el rectangulo
        drawing = True
        x_init, y_init = x,y
        top_left_pt = (x,y)
        bottom_right_pt = (x,y)
   
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        ## Actualizar coordenadas en movimiento
        # para top_left siempre guardar el mínimo
        #para bottom_right el máximo
        top_left_pt =(min(x_init,x), min(y_init, y))
        bottom_right_pt = (max(x_init,x), max(y_init, y))
        print(top_left_pt,bottom_right_pt)
   
    elif event == cv2.EVENT_LBUTTONUP:
        ## Terminar de dibujar el rectangulo
        drawing = False
        top_left_pt =(min(x_init,x), min(y_init, y))
        bottom_right_pt = (max(x_init,x), max(y_init, y))
 
if __name__ == '__main__':
    #cap = cv2.VideoCapture(0) # 0 para la cámara por defecto, o puedes usar la ruta de un video
    # para tomar un video de ejemplo, puedes usar la ruta de un video en lugar de 0, por ejemplo: 'video.mp4'
    cap = cv2.VideoCapture("C:\\Users\\jhoan\\OneDrive - Universidad EIA\\Semestres\\10 semestre (2026_1)\\Vision_artificial\\clase_video\\videos\\Car_194.mp4")
    if not cap.isOpened():
        raise IOError("No fue posible conectarse a la cámara")
   
    cv2.namedWindow('WebCam')
    cv2.setMouseCallback('WebCam', draw_rectangle)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
       
        (x0, y0), (x1, y1) = top_left_pt, bottom_right_pt
        # if x0 >= 0 and y0 >= 0 and x1 > x0 and y1 > y0:
        #     frame[y0:y1, x0:x1] = 255 - frame[y0:y1, x0:x1]
 
        ##Dibujar rectangle
        cv2.rectangle(frame, top_left_pt, bottom_right_pt, (255,0,0), 3)
 
        #Extrar regón parcial de la imagen
       
        if x0 >= 0 and y0 >= 0 and x1 > x0 and y1 > y0:
            roi_image = frame[y0:y1, x0:x1]
            cv2.imshow('ROI_WebCam', roi_image)
 
        cv2.imshow('WebCam', frame)
       
        c = cv2.waitKey(1)
        if c == 27:
            break
   
    cap.release()
    cv2.destroyAllWindows()
 