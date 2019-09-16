#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 08:55:39 2019

@author: theleoad

### QUANTIZACAO ###
"""
#Tive um pequeno problema com o setup na minha máquina e preciso dessas duas
#linhas abaixo para indicar ao python o caminho dos meus impports
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')

import cv2
import numpy

image = cv2.imread("campos.jpg")

r = 31
image = numpy.uint8(image / r) * r

cv2.imshow('campos com quantizacao', image)
cv2.waitKey(0)
cv2.destroyAllWindows()