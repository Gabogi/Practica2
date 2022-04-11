import numpy as np
import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread('imagen_jpg1.jpg')
img2 = cv2.imread('imagen_jpg2.jpg')
img3=img1[1:600,1:300,:]
img4=img2[1:600,1:300,:]

suma = img3 + img4
resta = img3 - img4
mult = img3 * img4
div = img3 / img4
raiz = np.sqrt(img4)
logaritmo = np.log(img4)
potencia = img4**2


cv2.imshow("Imagen 1", img1), cv2.moveWindow("Imagen 1", 0, 70)
cv2.imshow("Imagen 2", img2), cv2.moveWindow("Imagen 2", 1066, 70)
 

cv2.imshow('suma',suma), cv2.moveWindow("suma", 533, 70)
cv2.imwrite('suma3.jpg',suma)


G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('suma')
elif G == 27:  
 	cv2.destroyAllWindows()

cv2.imshow('resta',resta), cv2.moveWindow("resta", 533, 70)
cv2.imwrite('resta3.jpg',resta)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('resta')
elif G == 27:  
 	cv2.destroyAllWindows()

cv2.imshow('multiplicacion',mult), cv2.moveWindow("multiplicacion", 533, 70)
cv2.imwrite('multiplicacion3.jpg',mult)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('multiplicacion')
elif G == 27:  
    cv2.destroyAllWindows() 

cv2.imshow('division',div), cv2.moveWindow("division", 533, 70)
cv2.imwrite('division3.jpg',div)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('division')
elif G == 27:  
    cv2.destroyAllWindows()

cv2.imshow('raiz',raiz), cv2.moveWindow("raiz", 533, 70)
cv2.imwrite('raiz3.jpg',raiz)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('raiz')
elif G == 27:  
    cv2.destroyAllWindows()

cv2.imshow('logaritmo',logaritmo), cv2.moveWindow("logaritmo", 533, 70)
cv2.imwrite('logaritmo3.jpg',logaritmo)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('logaritmo')
elif G == 27:  
    cv2.destroyAllWindows()

cv2.imshow('potencia',potencia), cv2.moveWindow("potencia", 533, 70)
cv2.imwrite('potencia3.jpg',potencia)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('potencia')
elif G == 27:  
    cv2.destroyAllWindows()



cv2.waitKey(0) 
cv2.destroyAllWindows()