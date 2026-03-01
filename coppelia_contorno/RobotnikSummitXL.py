import cv2
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import my_functions
##ruedas trocadas las derechas



# =====================
# AJUSTA ESTOS NOMBRES CON LAS RUTAS QUE COPIES DE COPPELIASIM
# =====================

ROBOT_NAME = '/RobotnikSummitXL'
VISION_SENSOR_NAME = '/RobotnikSummitXL/cameraCar'  # ajusta al nombre real

BL_JOINT_NAME = '/RobotnikSummitXL/bl_joint/back_left_wheel'
FL_JOINT_NAME = '/RobotnikSummitXL/fl_joint/front_left_wheel'
BR_JOINT_NAME = '/RobotnikSummitXL/br_joint/back_right_wheel'
FR_JOINT_NAME = '/RobotnikSummitXL/fr_joint/front_right_wheel'

# =====================
# CONEXIÓN CON COPPELIASIM
# =====================

client = RemoteAPIClient()  # host='localhost', port=23000 por defecto
sim = client.require('sim')

robot = sim.getObject(ROBOT_NAME)
vision = sim.getObject(VISION_SENSOR_NAME)

bl_joint = sim.getObject(BL_JOINT_NAME)
fl_joint = sim.getObject(FL_JOINT_NAME)
br_joint = sim.getObject(BR_JOINT_NAME)
fr_joint = sim.getObject(FR_JOINT_NAME)

# Modo stepping controlado desde Python
sim.setStepping(True)
sim.startSimulation()



print("Simulación iniciada. Pulsa 'q' en la ventana de OpenCV para salir.")

try:
    while True:
        # Leer imagen del sensor de visión
        img_bytes, resolution = sim.getVisionSensorImg(vision)
        res_x, res_y = resolution[0], resolution[1]

        img = np.frombuffer(img_bytes, dtype=np.uint8)
        img = img.reshape((res_y, res_x, 3))
        img = cv2.flip(img, 0)  # invertir verticalmente

        # Coppelia envía RGB, OpenCV usa BGR
        img_bgr = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

        imageBinaryHsv = my_functions.binaryImageColorHsv(img_bgr, (120,15,15), (120,255,255))
        my_functions.showImage("mi imagen BinaryHsv",imageBinaryHsv) ##es mejor hsv porque no es tan sensible a camcios de iluminacion
        
        h,w=imageBinaryHsv.shape

     

                    
        
        # Mostrar imagen
        cv2.imshow('Summit camera', img_bgr)

        #movimiento llantas
        sim.setJointTargetVelocity(bl_joint, 0)
        sim.setJointTargetVelocity(br_joint, 0)
        sim.setJointTargetVelocity(fl_joint, 0)
        sim.setJointTargetVelocity(fr_joint, 0)

      
        # Avanzar simulación un paso
        client.step()

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
      
except KeyboardInterrupt:
    pass

sim.stopSimulation()
cv2.destroyAllWindows()
print("Simulación detenida.")