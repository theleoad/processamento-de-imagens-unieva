#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:20:06 2019

@author: theleoad

### ALTERACAO DE VALOR DO PIXEL ###
"""
#Tive um pequeno problema com o setup na minha máquina e preciso dessas duas
#linhas abaixo para indicar ao python o caminho dos meus impports
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')

import cv2

image = cv2.imread("campos.jpg")

image[200:350,200:350] = (0,0,0)

cv2.imshow('pixels com valores alterados', image)
cv2.waitKey(0)
cv2.destroyAllWindows()