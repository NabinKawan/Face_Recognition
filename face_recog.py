import cv2
import sqlite3
recognizer=cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trained_data/trained_data.yml')
# print(help(cv2.face.LBPHFaceRecognizer_create()))
face_cascade = cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml')
vid=cv2.VideoCapture(0)
# fourcc=cv2.VideoWriter_fourcc(*'XVID')
# out=cv2.VideoWriter('out.avi',fourcc,20.0,(640,480))
def getInfo(id):
    profile=None
    conn=sqlite3.connect('database.db')
    cmd='SELECT * FROM Person WHERE ID='+str(id)
    datas=conn.execute(cmd)
    for data in datas:
        profile=data
    conn.close()
    return profile
font = cv2.FONT_HERSHEY_SIMPLEX
while vid.isOpened():
    re,img=vid.read()
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for x,y,w,h in faces:
        id,config=recognizer.predict(gray[y:y+h,x:x+w])
        img=cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        profile=getInfo(id)
        if profile!=None:
            cv2.putText(img, str(profile[1]),(x, y + h), font, 1.1, (0, 255, 0),2)
        else:
            cv2.putText(img,"No Data", (x, y + h), font, 1.1, (0, 255, 0),2)
        # out.write(img)
        cv2.imshow('Face Recognition',img)
    if cv2.waitKey(1) & 0xFF==27:
        break
vid.release()
# out.release()
cv2.destroyAllWindows()