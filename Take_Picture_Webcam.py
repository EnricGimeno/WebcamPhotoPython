import numpy as np
import cv2
import Image, ImageTk
from PIL import Image, ImageTk
import time



cap = cv2.VideoCapture(1)
##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920.0)
##cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080.0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280.0)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720.0)
#cap.set(cv2.CAP_PROP_FPS, 10)
#print str(w) + "x" + str(h)

if not(cap.isOpened()):
    cap.open()
    

while(cap.isOpened()):
    # Obtenemos las dimensiones de la imagen. Por defecto es de 640x480
    width = cap.get(3)
    height = cap.get(4)
    fps = cap.get(5)
    print str(width) + "x" + str(height) + 'fps' + str(fps)
     
    # ret es un boolean que devuelve si el frame es correcto.
    # no servira para saber cuando acaba un video
    ret, frame = cap.read()
    

    cv2.imshow("Webcam", frame)
    bkg=frame.copy()

    print("Esperando al fondo - Pulse espacio")
    fondo = frame
    #fondo = Image.fromarray(frame)
    
    
    if cv2.waitKey(1) == 32:
        cv2.destroyWindow("Webcam")
        break
##fondo_pho = ImageTk.PhotoImage(fondo)
b,g,r = cv2.split(fondo)
rgb_img = cv2.merge([r,g,b])
fondo_arr = Image.fromarray(rgb_img)
fondo_arr.save('Targets4.png')
