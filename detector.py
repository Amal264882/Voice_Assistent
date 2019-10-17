import cv2
import numpy as np

def faceReg():
    faceDetect = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
    cam = cv2.VideoCapture(0)
    rec = cv2.face.LBPHFaceRecognizer_create();
    rec.read('recognizer/trainigData.yml')
    id = 0
    font = cv2.FONT_HERSHEY_SIMPLEX
    color = (255, 255, 255)
    while(True):
        ret,img = cam.read()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces = faceDetect.detectMultiScale(gray,1.3,5)

        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
            id,conf = rec.predict(gray[y:y+h,x:x+w])
            print(conf)
            if (conf < 40 ):
                return True
        
        #        cv2.putText(img,str(id),(x,y+h),font,1,color,2,cv2.LINE_AA);
            else :
                print("Login Fail") 
        #cv2.imshow("face",img)
        if(cv2.waitKey(1) == ord('q')):
            break
    cam.release()
    cv2.destroyAllWindows()

faceReg()

