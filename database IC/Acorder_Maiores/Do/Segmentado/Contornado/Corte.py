import numpy as np
import cv2

file= open('caracteristicas.arff', 'w')

file.write('@relation caracteristicas\n\n')
file.write('@attribute cima numeric\n')
file.write('@attribute baixo numeric\n')
file.write('@attribute esquerda numeric\n')
file.write('@attribute direita numeric\n')
file.write('@attribute DES numeric\n')
file.write('@attribute DEI numeric\n')
file.write('@attribute DDS numeric\n')
file.write('@attribute DDI numeric\n')
file.write('@attribute altura numeric\n')
file.write('@attribute largura numeric\n')
file.write('@attribute convex numeric\n')
file.write('@attribute class {A, B, C, D, E}\n\n')
file.write('@data\n')

vet= np.zeros(8)
#pos0= cima, pos1= baixo, pos2= esquerda, pos3= direita,
#pos4= diagonal esquerda superior, pos5= diagonal esquerda inferior,
#pos6= diagonal direita superior, pos7= diagonal direita inferior

def normalizar(cnt):
    for j in range(1, len(cnt)):
        if cnt[j][0][0]== cnt[j- 1][0][0] and cnt[j][0][1]< cnt[j- 1][0][1]:
            vet[0]+= 1

        elif cnt[j][0][0]== cnt[j- 1][0][0] and cnt[j][0][1]> cnt[j- 1][0][1]:
            vet[1]+= 1

        elif cnt[j][0][0]< cnt[j- 1][0][0] and cnt[j][0][1]== cnt[j- 1][0][1]:
            vet[2]+= 1

        elif cnt[j][0][0]> cnt[j- 1][0][0] and cnt[j][0][1]== cnt[j- 1][0][1]:
            vet[3]+= 1

        elif cnt[j][0][0]< cnt[j- 1][0][0] and cnt[j][0][1]< cnt[j- 1][0][1]:
            vet[4]+= 1

        elif cnt[j][0][0]< cnt[j- 1][0][0] and cnt[j][0][1]> cnt[j- 1][0][1]:
            vet[5]+= 1

        elif cnt[j][0][0]> cnt[j- 1][0][0] and cnt[j][0][1]< cnt[j- 1][0][1]:
            vet[6]+= 1

        elif cnt[j][0][0]> cnt[j- 1][0][0] and cnt[j][0][1]> cnt[j- 1][0][1]:
            vet[7]+= 1

    return vet

for i in range(0, 64):
    
    image= cv2.imread(str(i)+'_mao.jpg')

    image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image= cv2.threshold(image, 150, 255,  cv2.THRESH_BINARY)[1]

    _, cnt, _= cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    maior= max(cnt)

    esquerda= tuple(maior[maior[:, :, 0].argmin()][0])
    direita= tuple(maior[maior[:, :, 0].argmax()][0])
    cima= tuple(maior[maior[:, :, 1].argmin()][0])
    baixo= tuple(maior[maior[:, :, 1].argmax()][0])

    largura= direita[0]- esquerda[0]
    altura= baixo[1]- cima[1]
    
    razao= (direita[0]- esquerda[0])/(baixo[1]- cima[1])

    image= cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    if razao> 2.5:
        print('Entrou')
        tamanho= direita[0]- esquerda[0]
        corte= (tamanho* 3)/ 4

        pixel_corte= int(direita[0]- corte)

        print(pixel_corte)

        indice1= np.full((2, ), 0)
        indice2= np.full((2, ), 0)

        for j in range(0, len(maior)):
            if maior[j][0][0]< pixel_corte:
                cv2.circle(image, (maior[j][0][0], maior[j][0][1]), 3, (0, 0, 0), -1)

                if maior[j][0][0]== pixel_corte and indice1[0]== 0:
                    indice1[0]= maior[j][0][0]
                    indice1[1]= maior[j][0][1]

                else:
                    indice2[0]= maior[j][0][0]
                    indice2[1]= maior[j][0][1]
                    
        cv2.line(image, indice1, indice2, (255, 255, 255), 2)

    image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    _, contornos, _= cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    c_maior= max(contornos)

    hull= cv2.convexHull(c_maior, returnPoints= False)
    defects= cv2.convexityDefects(c_maior, hull)

    image= cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

    for j in range(defects.shape[0]):
        s,e,f,d = defects[j,0]
        start = tuple(c_maior[s][0])
        end = tuple(c_maior[e][0])
        far = tuple(c_maior[f][0])
        cv2.line(image,start,end,(0,255,0),2)
        cv2.circle(image,far,5, (0,0,255),-1)

    maior= 0
    for j in range(defects.shape[0]):
        if maior< defects[j][0][3]:
            maior= int(defects[j][0][3])

    vet= normalizar(c_maior)
    
    file.write(str(vet[0])+','+str(vet[1])+','+str(vet[2])+','+str(vet[3])+','+str(vet[4])+','+str(vet[5])+','+str(vet[6])+','+str(vet[7])+','+str(altura)+','+str(largura)+','+str(maior)+',A\n')

    cv2.imshow('imagem', image)
    print(str(i)+' imagem')
    cv2.imwrite('Corte/'+str(i)+'_mao.jpg', image)
    
file.close()
