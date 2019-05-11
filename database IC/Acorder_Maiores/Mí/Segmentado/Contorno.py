import cv2
import numpy as np

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
file.write('@attribute class {A, B, C, D, E}\n\n')
file.write('@data\n')


contornos= []
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

for i in range(2, 62):

    def nothing(x):
        pass

    cv2.namedWindow("Trackbar")
    cv2.createTrackbar("1", "Trackbar", 0, 5000, nothing)
    cv2.createTrackbar("2", "Trackbar", 5000, 5000, nothing)
    cv2.createTrackbar("3", "Trackbar", 0, 100, nothing)
    cv2.createTrackbar("4", "Trackbar", 4, 5, nothing)
    imagem2= cv2.imread(str(i)+'_mao_cinza.jpg')

    while True:
        imagem= cv2.imread(str(i)+'_mao_cinza.jpg')
        imagem= cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        l1= cv2.getTrackbarPos("1", "Trackbar")
        l2= cv2.getTrackbarPos("2", "Trackbar")
        l3= cv2.getTrackbarPos("3", "Trackbar")
        l4= cv2.getTrackbarPos("4", "Trackbar")

        _, contornos, _= cv2.findContours(imagem, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contornos:
            perimetro= cv2.arcLength(cnt, False)
            aprox= cv2.approxPolyDP(cnt, (l3/100)*cv2.arcLength(cnt, True), True)
            
            if perimetro> l1 and perimetro< l2:
                print('Tamanho do contorno'+str(len(aprox)))

                for k in range(0, 8):
                    vet[k]= 0

                vet= normalizar(aprox)
                
                cv2.drawContours(imagem, [aprox], 0, (255, 0, 0), l4)

        

        cv2.namedWindow(str(i)+' imagem', cv2.WINDOW_NORMAL)
        cv2.resizeWindow(str(i)+' imagem', 800, 600)
        cv2.imshow(str(i)+' imagem', imagem)

        key= cv2.waitKey(1)
        if key== 27:
            break
        
    print(str(i)+' feito')
    file.write(str(vet[0])+','+str(vet[1])+','+str(vet[2])+','+str(vet[3])+','+str(vet[4])+','+str(vet[5])+','+str(vet[6])+','+str(vet[7])+','+'C\n')
    print(sum(vet))
    contornos.append(vet)
    cv2.imwrite('Contornado/'+str(i)+'_mao.jpg', imagem)
    cv2.destroyAllWindows()


file.close()
