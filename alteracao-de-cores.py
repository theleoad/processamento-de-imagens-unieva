#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:06:04 2019

@author: theleoad

### ALTERACAO DE CORES ###
"""

#Tive um pequeno problema com o setup na minha máquina e preciso dessas duas
#linhas abaixo para indicar ao python o caminho dos meus impports
import sys
sys.path.append('/usr/local/lib/python3.7/site-packages')

import cv2
import numpy

image = cv2.imread("campos.jpg")

imageblue = cv2.imread("campos.jpg")
# exclui verde e vermelho dos canais de cores
imageblue[:, :, 1] = 0
imageblue[:, :, 2] = 0

imagegreen = cv2.imread("campos.jpg")
# exclui azul e vermelho dos canais de cores
imagegreen[:, :, 0] = 0
imagegreen[:, :, 2] = 0

imagered = cv2.imread("campos.jpg")
# seta o azul e o verde para zero
imagered[:, :, 0] = 0
imagered[:, :, 1] = 0

imageblackwhite = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


cv2.imshow('imagem original', image)
cv2.imshow('imagem azul', imageblue)
cv2.imshow('imagem verde', imagegreen)
cv2.imshow('imagem vermelha', imagered)
cv2.imshow('imagem preto e branco', imageblackwhite)
cv2.waitKey(0)
cv2.destroyAllWindows()