import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import *
import sympy as sp

img1 = cv2.imread('imagen_jpg1.jpg')
img2 = cv2.imread('imagen_jpg2.jpg')
img3=img1[1:600,1:300,:]
img4=img2[1:600,1:300,:]


suma1 = cv2.addWeighted(img3,0.7,img4,0.3,0)
suma2 = cv2.add(img3,img4)
suma3 = img3 + img4
resta1 = cv2.subtract(img3,img4)
resta2 = cv2.absdiff(img3,img4)
resta3 = img3 - img4
mult1 = cv2.multiply(img3,img4)
mult3 = img3 * img4
div1 = cv2.divide(img3,img4)
div3 = img3 / img4
c = 255 / np.log(1 + np.max(img3)) 
log_img3 = c * (np.log(img3 + 1))    
log_img3 = np.array(log_img3, dtype = np.uint8) 
c = 255 / np.log(1 + np.max(img4)) 
log_img4 = c * (np.log(img4 + 1))    
log_img4 = np.array(log_img4, dtype = np.uint8)
logn1 = cv2.addWeighted(log_img3,1,log_img4,1,0)
raiz1 = img4**0.5
potencia1 = cv2.pow(img3, 2)
potencia2 = cv2.pow(img4, 2)
potenciaT1 = cv2.addWeighted(potencia1,1,potencia2,1,0)
potencia3 = img3**2
potencia4 = img4**2
potenciaT2 = cv2.addWeighted(potencia3,1,potencia4,1,0)


cv2.imshow("Imagen 1", img3), cv2.moveWindow("Imagen 1", 0, 70)
cv2.imshow("Imagen 2", img4), cv2.moveWindow("Imagen 2", 1066, 70)


cv2.imshow('suma1',suma1), cv2.moveWindow("suma1", 533, 70)
cv2.imwrite('suma1.jpg',suma1)


G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('suma1')
elif G == 27:  
 	cv2.destroyAllWindows()

cv2.imshow('suma2',suma2), cv2.moveWindow("suma2", 533, 70)
cv2.imwrite('suma2.jpg',suma2)


G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('suma2')
elif G == 27:  
    cv2.destroyAllWindows()

cv2.imshow('suma3',suma3), cv2.moveWindow("suma3", 533, 70)
cv2.imwrite('suma3.jpg',suma3)


G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('suma3')
elif G == 27:  
    cv2.destroyAllWindows()

cv2.imshow('resta1',resta1), cv2.moveWindow("resta1", 533, 70)
cv2.imwrite('resta1.jpg',resta1)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('resta1')
elif G == 27:  
 	cv2.destroyAllWindows()

cv2.imshow('resta2',resta2), cv2.moveWindow("resta2", 533, 70)
cv2.imwrite('resta2.jpg',resta2)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('resta2')
elif G == 27:  
    cv2.destroyAllWindows()

cv2.imshow('resta3',resta3), cv2.moveWindow("resta3", 533, 70)
cv2.imwrite('resta3.jpg',resta3)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('resta3')
elif G == 27:  
    cv2.destroyAllWindows()

cv2.imshow('multiplicacion1',mult1), cv2.moveWindow("multiplicacion1", 533, 70)
cv2.imwrite('multiplicacion1.jpg',mult1)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('multiplicacion1')
elif G == 27:  
    cv2.destroyAllWindows() 

cv2.imshow('multiplicacion3',mult3), cv2.moveWindow("multiplicacion3", 533, 70)
cv2.imwrite('multiplicacion3.jpg',mult3)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('multiplicacion3')
elif G == 27:  
    cv2.destroyAllWindows() 

cv2.imshow('division1',div1), cv2.moveWindow("division1", 533, 70)
cv2.imwrite('division1.jpg',div1)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('division1')
elif G == 27:  
    cv2.destroyAllWindows()

cv2.imshow('division3',div3), cv2.moveWindow("division3", 533, 70)
cv2.imwrite('division3.jpg',div3)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('division3')
elif G == 27:  
    cv2.destroyAllWindows()

cv2.imshow('logaritmo1',logn1), cv2.moveWindow("logaritmo1", 533, 70)
cv2.imwrite('logaritmo1.jpg',logn1)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('logaritmo1')
elif G == 27:  
    cv2.destroyAllWindows()

cv2.imshow('raiz1',raiz1), cv2.moveWindow("raiz1", 533, 70)
cv2.imwrite('raiz1.jpg',raiz1)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('raiz1')
elif G == 27:  
    cv2.destroyAllWindows()


cv2.imshow('potencia1',potenciaT1), cv2.moveWindow("potencia1", 533, 70)
cv2.imwrite('potencia1.jpg',potenciaT1)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('potencia1')
elif G == 27:  
    cv2.destroyAllWindows()

cv2.imshow('potencia2',potenciaT2), cv2.moveWindow("potencia2", 533, 70)
cv2.imwrite('potencia2.jpg',potenciaT2)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('potencia2')
elif G == 27:  
    cv2.destroyAllWindows()



cv2.waitKey(0) 
cv2.destroyAllWindows()




#Dimensiones de la imagen1: (623, 312, 3)
#Dimensiones de la imagen2: (623, 347, 3)