import numpy as np
import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread('imagen_jpg1.jpg')
img2 = cv2.imread('imagen_jpg2.jpg')
img3=img1[1:600,1:300,:]
img4=img2[1:600,1:300,:]

suma = cv2.add(img3,img4)
resta = cv2.absdiff(img3,img4)
mult = img3.mul(img4,1.0)
potencia1 = cv2.pow(img3, 2)
potencia2 = cv2.pow(img4, 2)

cv2.imshow("Imagen 1", img3)
cv2.imshow("Imagen 2", img4)
 
cv2.imshow('suma',suma)
cv2.imwrite('suma2.jpg',suma)



G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('suma')
elif G == 27:  
 	cv2.destroyAllWindows()

cv2.imshow('resta',resta)
cv2.imwrite('resta2.jpg',resta)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('resta')
elif G == 27:  
 	cv2.destroyAllWindows()

cv2.imshow('potencia1',potencia1)
cv2.imwrite('potencia2-1.jpg',potencia1)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('potencia1')
elif G == 27:  
    cv2.destroyAllWindows()

cv2.imshow('potencia2',potencia2)
cv2.imwrite('potencia2-2.jpg',potencia2)

G = cv2.waitKey(0) 
if G == ord('g'):
    cv2.destroyWindow('potencia2')
elif G == 27:  
    cv2.destroyAllWindows()



cv2.waitKey(0) 
cv2.destroyAllWindows()