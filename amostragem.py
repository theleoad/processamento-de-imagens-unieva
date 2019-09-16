#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:47:17 2019

@author: theleoad

### AMOSTRAGEM ###

"""
#Tive um pequeno problema com o setup na minha máquina e preciso dessas duas
#linhas abaixo para indicar ao python o caminho dos meus impports
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')



import numpy
import cv2

image = cv2.imread("campos.jpg")

n=2
image_reduzida = image [::n,::n]

m = 2
image_aumentada = numpy.repeat(image, m, axis = 0)
image_aumentada = numpy.repeat(image_aumentada, m, axis = 1)

cv2.imshow("campos original", image)
cv2.imshow("campos reduzidos", image_reduzida)
cv2.imshow("campos aumentados", image_aumentada)
cv2.waitKey(0)
cv2.destroyAllWindows()