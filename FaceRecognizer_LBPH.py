import cv2,os
import numpy as np
from PIL import Image
import pickle
import sqlite3


recognizer = cv2.face.LBPHFaceRecognizer_create()

recognizer.read('trainner/trainner.yml')
cascadePath = "Classifiers/face.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
path='dataSet'


def getProfile(id):
    conn=sqlite3.connect("FaceHub.db")
    cmd = "SELECT * FROM People WHERE ID='{}'".format(str(id))
    cursor=conn.execute(cmd)
    profile=None
    for row in cursor:
        profile=row
    conn.close()
    return profile



cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX #Creates a font
while True:
    ret, img =cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces=faceCascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(100, 100), flags=cv2.CASCADE_SCALE_IMAGE)
    for(x,y,w,h) in faces:
        id, conf=recognizer.predict(gray[y:y+h,x:x+w])
        print(conf)
        cv2.rectangle(img,(x,y),(x+w,y+h),(225,0,0),2)

        profile=getProfile(id)
        if(profile!=None):
            cv2.rectangle(img, (x - 22, y - 90), (x + w + 22, y - 22), (255, 0, 0), -1)
            cv2.putText(img, str(profile[1]), (x, y - 40), font, 1, (255, 255, 255), 3)

        #     cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[1]),[x,y+h+30],font,255)
        #     cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[2]),[x,y+h+60],font,255)
        #     cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[3]),[x,y+h+90],font,255)
        #     cv2.cv.PutText(cv2.cv.fromarray(img),str(profile[4]),[x,y+h+120],font,255)

    cv2.imshow('Recognizer', img)
    if cv2.waitKey(100) & 0xFF == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
