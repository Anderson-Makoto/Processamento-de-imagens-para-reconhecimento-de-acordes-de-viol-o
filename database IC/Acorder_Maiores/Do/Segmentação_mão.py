import numpy as np
import cv2


for i in range(0, 64):
    
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
    
    imagem= cv2.imread(str(i)+'.jpg.jpg')
    imagem= cv2.resize(imagem, (int(imagem.shape[1]/ 3), int(imagem.shape[0]/ 3)))
    imagem= cv2.cvtColor(imagem, cv2.COLOR_BGR2YCrCb)
    preprocessada= cv2.bilateralFilter(imagem, 15, 11, 11)
    print(str(i))


    while True:
        l1= cv2.getTrackbarPos("1", "Trackbar")
        l2= cv2.getTrackbarPos("2", "Trackbar")
        l3= cv2.getTrackbarPos("3", "Trackbar")
        l4= cv2.getTrackbarPos("4", "Trackbar")
        l5= cv2.getTrackbarPos("5", "Trackbar")
        l6= cv2.getTrackbarPos("6", "Trackbar")
        l7= cv2.getTrackbarPos("7", "Trackbar")
        l8= cv2.getTrackbarPos("8", "Trackbar")
        print(str(i))

        down= np.array([l1, l2, l3])
        upper= np.array([l4, l5, l6])

        mascara= cv2.inRange(preprocessada, down, upper)
        print(str(i))
        
        if l7%2!= 0:
            mascara= cv2.morphologyEx(mascara, cv2.MORPH_OPEN, np.ones((l7, l7), np.uint8))

        if l8%2!= 0:
            mascara= cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, np.ones((l8, l8), np.uint8))
    
        cv2.namedWindow('imagem '+str(i), cv2.WINDOW_NORMAL)
        cv2.imshow('imagem '+str(i), mascara)

        key= cv2.waitKey(1)
        if key== 27:
            break
    print(str(i)+' feito')
    cv2.imwrite('Segmentado/'+str(i)+'_mao.jpg', mascara)
    cv2.destroyAllWindows()
