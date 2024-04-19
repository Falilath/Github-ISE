# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 04:31:37 2023

@author: TOP INFORMATIQUE
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:19:02 2023

@author: TOP INFORMATIQUE
"""

import cv2 as cv

# charger le classificateur en cascade
eye_casade = cv.CascadeClassifier("haarcascade_eye.xlm")


# charger les images 
img = cv.imread("im_1.png")

#convert to grayscale
gray = cv.cvtcolor(img, cv.COLOR_BGR2GRAY)

# exécuter la détection de visage
faces = face_casade.detectMultiSacle(gray, 1.1, 8)  # 1.1 = paramètre d'échelle,
                                                    # 8 = nombre minimum de voisin
                                                    # retourne coodonées des images


# afficher les images
for face in faces:
    x, y, z, h = face
    
    # dessinner le rectangle sur l'image principale
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    
# exécution de la détection des yeux
eyes = eye_casade.detectMultiScale(gray, 1.1, 3)

# affichage des yeux
for (ex, ey, ew, eh) in eyes:
    
    # dessinner le rectangle sur l'image principale
    cv.rectangle(img, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

# affiche l'image principale
cv.imshow('image principale', img)
cv.waitKey(0)
cv.destroyAllWindows()
