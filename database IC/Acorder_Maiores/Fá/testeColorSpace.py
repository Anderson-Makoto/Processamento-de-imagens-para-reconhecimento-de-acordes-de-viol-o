import cv2
import numpy as no

imagem= cv2.imread('61.jpg')

imagemYCrCb= cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
imagemHSV= cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
imagemLAB= cv2.cvtColor(imagem, cv2.COLOR_BGR2LAB)

imagemYCrCb= cv2.bilateralFilter(imagemYCrCb, 15, 11, 11)
imagemHSV= cv2.bilateralFilter(imagemHSV, 15, 11, 11)
imagemLAB= cv2.bilateralFilter(imagemLAB, 15, 11, 11)

cv2.namedWindow('HSV', cv2.WINDOW_NORMAL)
cv2.namedWindow('YCRCB', cv2.WINDOW_NORMAL)
cv2.namedWindow('LAB', cv2.WINDOW_NORMAL)

cv2.imshow('HSV', imagemHSV)
cv2.imshow('YCRCB', imagemYCrCb)
cv2.imshow('LAB', imagemLAB)
