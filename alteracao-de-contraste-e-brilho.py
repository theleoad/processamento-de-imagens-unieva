#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:37:16 2019

@author: theleoad

### ALTERACAO DE CONTRASTE E BRILHO ###
"""
#Tive um pequeno problema com o setup na minha máquina e preciso dessas duas
#linhas abaixo para indicar ao python o caminho dos meus impports
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')

import cv2
import numpy

image = cv2.imread("campos.jpg")

brightness = 50
contrast = 30

img = numpy.int16(image)
img = img * (contrast/127+1) - contrast + brightness
img = numpy.clip(img, 0, 255)
img = numpy.uint8(img)

cv2.imshow('imagem original', image)
cv2.imshow('imagem com brilho e contraste alterados', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

