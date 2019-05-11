import numpy as np
import cv2

def nothing(x):
    pass

cv2.namedWindow("Trackbar")
cv2.createTrackbar("1", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("2", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("3", "Trackbar", 0, 255, nothing)
cv2.createTrackbar("4", "Trackbar", 255, 255, nothing)
cv2.createTrackbar("5", "Trackbar", 255, 255, nothing)
cv2.createTrackbar("6", "Trackbar", 255, 255, nothing)
cv2.createTrackbar("7", "Trackbar", 0, 35, nothing)
cv2.createTrackbar("8", "Trackbar", 0, 35, nothing)

imagem= cv2.imread('53.jpg.jpg')
imagem= cv2.resize(imagem, (int(imagem.shape[1]/ 3), int(imagem.shape[0]/ 3)))
imagem= cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
preprocessada= cv2.bilateralFilter(imagem, 15, 11, 11)

#sofa(48, 136, 104), (214, 160, 145), (7, 7)
#parede cor de pele: (66, 134, 108), (209, 144, 134), (9, 13)
#cadeira mesa(67, 134, 108), (204, 162, 136), (19, 7)

while False:

    l1= cv2.getTrackbarPos("1", "Trackbar")
    l2= cv2.getTrackbarPos("2", "Trackbar")
    l3= cv2.getTrackbarPos("3", "Trackbar")
    l4= cv2.getTrackbarPos("4", "Trackbar")
    l5= cv2.getTrackbarPos("5", "Trackbar")
    l6= cv2.getTrackbarPos("6", "Trackbar")
    l7= cv2.getTrackbarPos("7", "Trackbar")
    l8= cv2.getTrackbarPos("8", "Trackbar")

    down= np.array([l1, l2, l3])
    upper= np.array([l4, l5, l6])

    mascara= cv2.inRange(preprocessada, down, upper)
    if l7%2!= 0:
        mascara= cv2.morphologyEx(mascara, cv2.MORPH_OPEN, np.ones((l7, l7), np.uint8))
        mascara= cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, np.ones((l8, l8), np.uint8))

    cv2.imshow('segmentada', mascara)

    key= cv2.waitKey(1)
    if key== 27:
        break
    
cv2.destroyAllWindows()

for sofa in range(0, 5):
    imagem= cv2.imread(str(sofa)+'.jpg.jpg')
    imagem= cv2.resize(imagem, (int(imagem.shape[1]/3), int(imagem.shape[0]/3)))
    imagem= cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    preprocessada= cv2.bilateralFilter(imagem, 15, 11, 11)

    down= np.array([48, 136, 104])
    upper= np.array([214, 160, 145])

    mascara= cv2.inRange(preprocessada, down, upper)

    mascara= cv2.morphologyEx(mascara, cv2.MORPH_OPEN, np.ones((7, 7), np.uint8))
    mascara= cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))

    cv2.imwrite('Segmentado/'+str(sofa)+'_mao.jpg', mascara)
    print(sofa)

for cadeiraMesa in range(5, 10):
    imagem= cv2.imread(str(cadeiraMesa)+'.jpg.jpg')
    imagem= cv2.resize(imagem, (int(imagem.shape[1]/3), int(imagem.shape[0]/3)))
    imagem= cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    preprocessada= cv2.bilateralFilter(imagem, 15, 11, 11)

    down= np.array([67, 134, 108])
    upper= np.array([204, 162, 136])

    mascara= cv2.inRange(preprocessada, down, upper)

    mascara= cv2.morphologyEx(mascara, cv2.MORPH_OPEN, np.ones((19, 19), np.uint8))
    mascara= cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))

    cv2.imwrite('Segmentado/'+str(cadeiraMesa)+'_mao.jpg', mascara)
    print(cadeiraMesa)
    

for parede in range(10, 15):
    imagem= cv2.imread(str(parede)+'.jpg.jpg')
    imagem= cv2.resize(imagem, (int(imagem.shape[1]/3), int(imagem.shape[0]/3)))
    imagem= cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    preprocessada= cv2.bilateralFilter(imagem, 15, 11, 11)

    down= np.array([66, 134, 108])
    upper= np.array([209, 144, 134])

    mascara= cv2.inRange(preprocessada, down, upper)

    mascara= cv2.morphologyEx(mascara, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    mascara= cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, np.ones((13, 13), np.uint8))

    cv2.imwrite('Segmentado/'+str(parede)+'_mao.jpg', mascara)
    print(parede)

for sofa in range(15, 30):
    imagem= cv2.imread(str(sofa)+'.jpg.jpg')
    imagem= cv2.resize(imagem, (int(imagem.shape[1]/3), int(imagem.shape[0]/3)))
    imagem= cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    preprocessada= cv2.bilateralFilter(imagem, 15, 11, 11)

    down= np.array([75, 133, 107])
    upper= np.array([239, 160, 123])

    mascara= cv2.inRange(preprocessada, down, upper)

    mascara= cv2.morphologyEx(mascara, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    mascara= cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

    cv2.imwrite('Segmentado/'+str(sofa)+'_mao.jpg', mascara)
    print(sofa)

for cadeiraMesa in range(30, 40):
    imagem= cv2.imread(str(cadeiraMesa)+'.jpg.jpg')
    imagem= cv2.resize(imagem, (int(imagem.shape[1]/3), int(imagem.shape[0]/3)))
    imagem= cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    preprocessada= cv2.bilateralFilter(imagem, 15, 11, 11)

    down= np.array([98, 141, 88])
    upper= np.array([244, 178, 138])

    mascara= cv2.inRange(preprocessada, down, upper)

    mascara= cv2.morphologyEx(mascara, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mascara= cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, np.ones((5, 5), np.uint8))

    cv2.imwrite('Segmentado/'+str(cadeiraMesa)+'_mao.jpg', mascara)
    print(cadeiraMesa)
    
for parede in range(40, 53):
    imagem= cv2.imread(str(parede)+'.jpg.jpg')
    imagem= cv2.resize(imagem, (int(imagem.shape[1]/3), int(imagem.shape[0]/3)))
    imagem= cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    preprocessada= cv2.bilateralFilter(imagem, 15, 11, 11)

    down= np.array([89, 141, 86])
    upper= np.array([227, 186, 134])

    mascara= cv2.inRange(preprocessada, down, upper)

    mascara= cv2.morphologyEx(mascara, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    mascara= cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, np.ones((11, 11), np.uint8))

    cv2.imwrite('Segmentado/'+str(parede)+'_mao.jpg', mascara)
    print(parede)

for parede in range(53, 64):
    imagem= cv2.imread(str(parede)+'.jpg.jpg')
    imagem= cv2.resize(imagem, (int(imagem.shape[1]/3), int(imagem.shape[0]/3)))
    imagem= cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    preprocessada= cv2.bilateralFilter(imagem, 15, 11, 11)

    down= np.array([188, 98, 91])
    upper= np.array([255, 169, 139])

    mascara= cv2.inRange(preprocessada, down, upper)

    mascara= cv2.morphologyEx(mascara, cv2.MORPH_OPEN, np.ones((9, 9), np.uint8))
    mascara= cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, np.ones((7, 7), np.uint8))

    cv2.imwrite('Segmentado/'+str(parede)+'_mao.jpg', mascara)
    print(parede)
