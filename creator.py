import cv2
import numpy as np
import time

faceDetect = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
cam = cv2.VideoCapture(0)

id = input("Enter user id:")
samplenum = 0
while(True):
    ret,img = cam.read()
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray,1.3,5)
    for (x,y,w,h) in faces:
        samplenum += 1
        if samplenum > 6:
            cv2.imwrite("DataSet/User."+str(id)+"."+str(samplenum)+".jpg",gray[y:y+h,x:x+w])
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.waitKey(100)
    cv2.imshow("face",img)
    cv2.waitKey(1)
    if samplenum > 100:
        break
cam.release()
cv2.destroyAllWindows()
