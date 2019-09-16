#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 11:55:52 2019

@author: theleoad

### DIVISAO ###
"""
#Tive um pequeno problema com o setup na minha máquina e preciso dessas duas
#linhas abaixo para indicar ao python o caminho dos meus impports
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')

import cv2
import numpy

image = cv2.imread("campos.jpg")


height, width = image.shape[:2]

start_row, start_col = int(0), int(0)
end_row, end_col = int(height * .5), int(width)
partesuperior = image[start_row:end_row , start_col:end_col]

start_row, start_col = int(height * .5), int(0)
end_row, end_col = int(height), int(width)
parteinferior = image[start_row:end_row , start_col:end_col]

cv2.imshow('imagem original', image)
cv2.imshow('parte inferior da imagem', parteinferior)
cv2.imshow('parte superior da imagem', partesuperior)

cv2.waitKey(0)
cv2.destroyAllWindows()
