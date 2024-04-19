# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 10:19:02 2023

@author: TOP INFORMATIQUE
"""
 
import cv2 as cv

# charger le classificateur en cascade
cascade = cv.CascadeClassifier("E:/ISE 2/SEMESTRE 1/Machine learning/Projet/haarcascade_frontalface_default.xml")

# charger les images 
img = cv.imread("E:/DISQUE DONNEES/ISE 2/SEMESTRE 1/Machine learning/work_folder_projet/images/im_1.jpg")

#convert to grayscale
gray = cv.cvtcolor(img, cv.COLOR_BGR2GRAY)

# exécuter la détection de visage
faces = cascade.detectMultiSacle(gray, 1.1, 8)  # 1.1 = paramètre d'échelle,
                                                    # 8 = nombre minimum de voisin
                                                    # retourne coodonées des images


# afficher les images
i = 0
for face in faces:
    x, y, z, h = face
    
    # dessinner le rectangle sur l'image principale
    cv.rectangle(img, (x, y), (x+z, y+h), (0, 255, 0), 2)
    
    # extraire les visages de l'image principale
    face = img[y:y+h, x:x+z]
    
    # afficher face0, face1 ....
    cv.imshow('face{}'.format(i), face)
    i += 1
    
# affiche l'image principale
cv.imshow('image principale', img)
cv.waitKey(0)
cv.destroyAllWindows()
