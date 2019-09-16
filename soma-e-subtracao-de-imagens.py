#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:31:31 2019

@author: theleoad

### SOMA E SUBTRACAO DE IMAGENS ###
"""
#Tive um pequeno problema com o setup na minha máquina e preciso dessas duas
#linhas abaixo para indicar ao python o caminho dos meus impports
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')

import cv2

image = cv2.imread("campos.jpg")

imageblue = image.copy()
imageblue[:, :, 1] = 0
imageblue[:, :, 2] = 0

imagegreen = image.copy()
imagegreen[:, :, 0] = 0
imagegreen[:, :, 2] = 0

imagesum = imagegreen + imageblue
imagesub = imagegreen - imageblue


cv2.imshow('imagem original', image)
cv2.imshow('imagem somada', imagesum)
cv2.imshow('imagem subtraida', imagesub)


cv2.waitKey(0)
cv2.destroyAllWindows()



