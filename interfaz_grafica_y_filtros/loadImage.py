# import cv2
# import numpy as np

# class ProcessImage:
#     def __init__(self, path):
#         self.path = path
 
#     def readImage(self):
#         self.imageColor = cv2.imread(self.path, 1)
import cv2
import numpy as np

class ProcessingImage():
    def __init__(self, path=None):
        self.path = path

    def readImage(self):
        self.imageColor = cv2.imread(self.path, 1)
        

    def convertToGray(self):
        self.imageGray = cv2.cvtColor(self.imageColor, 
                                     cv2.COLOR_BGR2GRAY)

    def convertToRgb(self):
        self.imageRgb = cv2.cvtColor(self.imageColor, 
                                     cv2.COLOR_BGR2RGB)
        
    def resizeImage(self):
        self.imageRgbResize = cv2.resize(self.imageRgb, (320,320))

    def filterMediaImage(self):
        self.ImageFilterMedia = cv2.medianBlur(self.imageGray, 21)

    def convertGrayToRgb(self):
        self.imageRgb = cv2.cvtColor(self.ImageFilterMedia, 
                                     cv2.COLOR_GRAY2RGB)
        
    def binaryInRange(self, val_min, val_max):
         print(val_min,val_max, self.ImageFilterMedia.shape[:2])
         self.imageBinary = cv2.inRange(self.ImageFilterMedia, val_min, val_max)
            
    def convertBinaryToRgb(self):
        self.imageRgb = cv2.cvtColor(self.imageBinary, 
                                     cv2.COLOR_GRAY2RGB)
        
    def dilateImage(self,num_dilate,num_iterations):
        k2 = np.ones((num_dilate, num_dilate), np.uint8)
        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (num_dilate,num_dilate))
        self.imageDilate = cv2.dilate(self.imageBinary, kernel = k, iterations=num_iterations)
        self.imageBinary = self.imageDilate

    def erodeImage(self, num_erosion, num_iterations):
        k2 = np.ones((num_erosion, num_erosion), np.uint8)
        k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (num_erosion,num_erosion))
        self.imageErode = cv2.erode(self.imageBinary, kernel = k, iterations=num_iterations)
        self.imageBinary = self.imageErode


    def convertToGray(self):
        self.imageGray = cv2.cvtColor(self.imageColor, cv2.COLOR_BGR2GRAY)

    def convertToRgb(self):
        self.imageRgb = cv2.cvtColor(self.imageColor, cv2.COLOR_BGR2RGB)
    
        # def resizeImage(self):
        #     self.imageRgbResize = cv2.resize(self.imageRgb, (320, 320),)
        #     return self.imageRgbResize
        
    def filterMediaImage(self,num_filtro):
        self.ImageFilterMedia = cv2.medianBlur(self.imageGray, num_filtro)

    def convertGrayToRgb(self):
        self.imageRgb = cv2.cvtColor(self.ImageFilterMedia,
                                     cv2.COLOR_GRAY2RGB)
    
    def binaryInrange(self,valMin,valMax):
        imageBinary = cv2.inRange(self.ImageFilterMedia, valMin, valMax)
        return imageBinary
    
    
