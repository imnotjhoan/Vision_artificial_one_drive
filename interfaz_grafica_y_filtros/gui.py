#pip install pillow
#python -m tkinter

from tkinter import *
import tkinter as tk
from tkinter import ttk

from PIL import Image
from PIL import ImageTk
import numpy as np
import cv2
import loadImage
# Crear 4 labels para los 4 cuadrantes
cuadrant_width = 560
cuadrant_height = 320
padding = 20
class Application(ttk.Frame):
    def __init__(self, master=None):
        try:
            super().__init__(master)
            self.filtrada = loadImage.ProcessingImage(path="C:\\Users\\jhoan\OneDrive - Universidad EIA\\Semestres\\10 semestre (2026_1)\\Vision_artificial\\interfaz_grafica_y_filtros\\images\\barras_cir.png")
            self.filtrada_color = loadImage.ProcessingImage(path="C:\\Users\\jhoan\OneDrive - Universidad EIA\\Semestres\\10 semestre (2026_1)\\Vision_artificial\\interfaz_grafica_y_filtros\\images\\barras_cir.png")
            self.imagegray1=loadImage.ProcessingImage(path="C:\\Users\\jhoan\OneDrive - Universidad EIA\\Semestres\\10 semestre (2026_1)\\Vision_artificial\\interfaz_grafica_y_filtros\\images\\barras_cir.png")
            self.binary=loadImage.ProcessingImage(path="C:\\Users\\jhoan\OneDrive - Universidad EIA\\Semestres\\10 semestre (2026_1)\\Vision_artificial\\interfaz_grafica_y_filtros\\images\\barras_cir.png")
            
            
            self.master = master
            self.master.geometry("1200x900")  # Ventana más grande para 4 cuadrantes

            self.createLabelWidgets()
            self.createWindowWidgets()
            self.createButtonWidgets()
            self.master.mainloop()
        except Exception as e:
            print("Error en constructor: " + str(e))

    def createLabelWidgets(self):
        # Cuadrante superior izquierdo
        self.labelQuadrant1 = tk.Label(self.master, borderwidth=2, relief="solid")
        self.labelQuadrant1.place(x=padding, y=padding)

        # Cuadrante superior derecho
        self.labelQuadrant2 = tk.Label(self.master, borderwidth=2, relief="solid")
        self.labelQuadrant2.place(x=cuadrant_width+ 2 * padding, y=padding)

        # Cuadrante inferior izquierdo
        self.labelQuadrant3 = tk.Label(self.master, borderwidth=2, relief="solid")
        self.labelQuadrant3.place(x=padding, y=cuadrant_height + 2*padding)

        # Cuadrante inferior derecho
        self.labelQuadrant4 = tk.Label(self.master, borderwidth=2, relief="solid")
        self.labelQuadrant4.place(x=cuadrant_width + 2*padding, y=cuadrant_height + 2*padding)

    def createWindowWidgets(self):
        # Crear imagen negra inicial para todos los cuadrantes
        frameBlack = np.zeros([cuadrant_height,cuadrant_width, 3], dtype=np.uint8)
        frameRgb = cv2.cvtColor(frameBlack, cv2.COLOR_BGR2RGB)
        frameArray = Image.fromarray(frameRgb)
        framePhotImage = ImageTk.PhotoImage(image=frameArray)

        # Asignar imagen inicial a todos los cuadrantes
        for label in [self.labelQuadrant1, self.labelQuadrant2,
                      self.labelQuadrant3, self.labelQuadrant4]:
            label.configure(image=framePhotImage)
            label.image = framePhotImage

    def createButtonWidgets(self):
        self.buttonLoadImage = tk.Button(self.master, text="Cargar Imagen",
                                         bg="#7d08eb", fg="#ffffff",
                                         width=20, command=self.loadImage)
        self.buttonLoadImage.place(x=520, y=700)

    def loadImage(self):

            # IMAGEN GRIS -------------------------------------------
            self.imagegray1.readImage()
            self.imagegray1.convertToGray()  # Convertir a escala de grises
            imageGrayRgb = cv2.cvtColor(self.imagegray1.imageGray, cv2.COLOR_GRAY2RGB)
            self.imagegray1.imageRgbResize = cv2.resize(
                imageGrayRgb,
                (cuadrant_width, cuadrant_height)
            )

            # IMAGEN BINARIA -------------------------------------------
            self.binary.readImage()
            self.binary.convertToGray()
            self.binary.imageBinary = cv2.inRange(self.binary.imageGray, 216, 255)
            self.binary.convertBinaryToRgb()

            self.binary.imageRgbResize = cv2.resize(
                self.binary.imageRgb,
                (cuadrant_width, cuadrant_height)
            )
            # IMAGEN FILTRADA -------------------------------------------
            self.filtrada.readImage()
            self.filtrada.convertToGray()
            self.filtrada.filterMediaImage(5)
            self.filtrada.imageBinary = cv2.inRange(self.filtrada.imageGray, 216, 255)
            self.filtrada.erodeImage(5,2)
            self.filtrada.dilateImage(5,2)

            self.filtrada.convertBinaryToRgb()
            self.filtrada.convertBinaryToRgb()

            self.filtrada.imageRgbResize = cv2.resize(
                self.filtrada.imageRgb,
                (cuadrant_width, cuadrant_height)
            )
            
            # IMAGEN FILTRADA CON COLOR -------------------------------------------
            binary = self.filtrada.imageBinary

            imagePurple = np.zeros(
                (binary.shape[0], binary.shape[1], 3),
                dtype=np.uint8
            )

            imagePurple[binary == 255] = [141, 50, 168]

            
            imagePurple = np.zeros((self.filtrada_color.imageBinary.shape[0], 
                                self.filtrada_color.imageBinary.shape[1], 3), dtype=np.uint8)
            imagePurple[self.filtrada_color.imageBinary == 255] = [141, 50, 168]  # Verde
            self.filtrada_color.imageRgb = imagePurple

            self.filtrada_color.imageRgbResize = cv2.resize(
                self.filtrada_color.imageRgb,
                (cuadrant_width, cuadrant_height)
            )

            self.loadRgbImages() 

    def loadRgbImages(self):

        # CUADRANTE 1 A GRIS -------------------------------------------------
        frameArray = Image.fromarray(self.imagegray1.imageRgbResize)
        framePhotImage = ImageTk.PhotoImage(image=frameArray)
        self.labelQuadrant1.configure(image=framePhotImage)
        self.labelQuadrant1.image = framePhotImage

        # CUADRANTE 2 binary -------------------------------------------------
        frameArray = Image.fromarray(self.binary.imageRgbResize)
        framePhotImage = ImageTk.PhotoImage(image=frameArray)
        self.labelQuadrant2.configure(image=framePhotImage)
        self.labelQuadrant2.image = framePhotImage

        # CUADRANTE 3 A COLOR -------------------------------------------------
        frameArray = Image.fromarray(self.filtrada.imageRgbResize)
        framePhotImage = ImageTk.PhotoImage(image=frameArray)
        self.labelQuadrant3.configure(image=framePhotImage)
        self.labelQuadrant3.image = framePhotImage

        # CUADRANTE 4 FILTRADA -------------------------------------------------
        frameArray = Image.fromarray(self.filtrada_color.imageRgbResize)
        framePhotImage = ImageTk.PhotoImage(image=frameArray)
        self.labelQuadrant4.configure(image=framePhotImage)
        self.labelQuadrant4.image = framePhotImage


def main():
    root = tk.Tk()
    root.title("Interfaz con 4 Cuadrantes")
    app = Application(master=root)

if __name__ == "__main__":
    main()