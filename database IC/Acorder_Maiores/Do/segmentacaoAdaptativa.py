import cv2
import numpy as np

for i in range(0, 63):

    def nothing(x):
        pass

    cv2.namedWindow("Trackbar")
    cv2.createTrackbar("preproc", "Trackbar", 1, 25, nothing)
    cv2.createTrackbar("preproc2", "Trackbar", 1, 25, nothing)
    cv2.createTrackbar("mascara", "Trackbar", 3, 25, nothing)
    cv2.createTrackbar("ultimo", "Trackbar", 3, 25, nothing)
    cv2.createTrackbar("open", "Trackbar", 1, 25, nothing)
    cv2.createTrackbar("close", "Trackbar", 1, 25, nothing)

    while True:
        imagem= cv2.imread(str(i)+'.jpg.jpg')
        imagem= cv2.resize(imagem, (int(imagem.shape[1]/ 3), int(imagem.shape[0]/ 3)))
        imagem= cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

        l1= cv2.getTrackbarPos("preproc", "Trackbar")
        l4= cv2.getTrackbarPos("mascara", "Trackbar")
        l5= cv2.getTrackbarPos("ultimo", "Trackbar")
        l6= cv2.getTrackbarPos("open", "Trackbar")
        l7= cv2.getTrackbarPos("close", "Trackbar")
        l8= cv2.getTrackbarPos("preproc2", "Trackbar")

        if l8%2!= 0:
            imagem= cv2.bilateralFilter(imagem, l1, l8, l8)
            
        if l4%2!= 0:
            imagem= cv2.adaptiveThreshold(imagem, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, l4, l5)

        if l6%2!= 0:
            imagem= cv2.morphologyEx(imagem, cv2.MORPH_OPEN, np.ones((l6, l6), np.uint8))

        if l7%2!= 0:
            imagem= cv2.morphologyEx(imagem, cv2.MORPH_CLOSE, np.ones((l7, l7), np.uint8))
        


        cv2.namedWindow(str(i)+' imagem', cv2.WINDOW_NORMAL)
        cv2.imshow(str(i)+' imagem', imagem)

        key= cv2.waitKey(1)
        if key== 27:
            break
        
    print(str(i)+' feito')
    cv2.imwrite('Segmentado/'+str(i)+'_mao.jpg', imagem)
    cv2.destroyAllWindows()
