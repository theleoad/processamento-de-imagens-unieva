#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:14:46 2019

@author: theleoad

### EXTRACAO DE FRACAO E INSERCAO DA FRACAO NA IMAGEM ###
"""
#Tive um pequeno problema com o setup na minha máquina e preciso dessas duas
#linhas abaixo para indicar ao python o caminho dos meus impports
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')

import cv2

image = cv2.imread("campos.jpg")

fracao = image[300:400, 150:300]
imagecomfracao = image.copy()
imagecomfracao[300:400, 300:450] = fracao

cv2.imshow('imagem original', image)
cv2.imshow('fracao da imagem', fracao)
cv2.imshow('imagem com fracao', imagecomfracao)

cv2.waitKey(0)
cv2.destroyAllWindows()

