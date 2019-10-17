import os
import cv2
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create();
path = 'DataSet'

def getImagesWithID(path):
    imagePath = [os.path.join(path,f) for f in os.listdir(path)]
    faces = []
    IDs = []
    for ImagePath in imagePath:
        faceImg = Image.open(ImagePath).convert('L');
        faceNp = np.array(faceImg,'uint8')
        ID = int(os.path.split(ImagePath)[-1].split('.')[1])
        faces.append(faceNp)
        IDs.append(ID)
        cv2.imshow("traing",faceNp)
        cv2.waitKey(10)
    return np.array(IDs),faces

Ids,faces = getImagesWithID(path)
recognizer.train(faces,Ids)
recognizer.save('recognizer/trainigData.yml')
cv2.destroyAllWindows()
