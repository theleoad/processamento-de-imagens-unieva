#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 10:02:38 2019

@author: theleoad

### HISTOGRAMA ###
"""
#Tive um pequeno problema com o setup na minha máquina e preciso dessas duas
#linhas abaixo para indicar ao python o caminho dos meus impports
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')

import matplotlib.pyplot as plt
import cv2

image = cv2.imread("campos.jpg")

plt.hist(image.ravel(),256,[0,256])
plt.title("Histograma da Imagem")
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()


