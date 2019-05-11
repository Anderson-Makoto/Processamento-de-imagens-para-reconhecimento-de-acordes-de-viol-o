import cv2
import numpy

for i in range(63, 64):
    imagem= cv2.imread(str(i)+'_mao.jpg')

    _, imagem= cv2.threshold(imagem, 127, 127, cv2.THRESH_BINARY)

    cv2.imwrite(str(i)+'_mao_cinza.jpg', imagem)
    print(str(i)+' imagem(ns) feita(s)')
