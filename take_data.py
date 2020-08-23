import cv2
import sqlite3
import time
face_cascade = cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml')
def insert(id,name):
    isEmpty=True
    conn=sqlite3.connect("database.db")
    cmd='SELECT * FROM Person WHERE ID='+id
    datas=conn.execute(cmd)
    # fetched_data=data.fetchall()
    # print(fetched_data)
    for data in datas:
        isEmpty=False
    # if not isEmpty:
    #     cmd='UPDATE Person SET NAME='+name
    if isEmpty:
        #cmd='INSERT INTO Person(ID,NAME) Values('+id+','+name+')'
        cmd = "INSERT INTO Person(ID,Name) Values(" + id + ",' " + name + " ' )"
    else:
        cmd = "UPDATE Person SET Name=' " + name + " ' WHERE ID=" + id
    conn.execute(cmd)
    conn.commit()
    conn.close()
cv2.namedWindow('Taking Data')
id=input("Enter id: ")
name=input("Enter name: ")
vid=cv2.VideoCapture(0)
sampleCount=0
time.sleep(4)
while vid.isOpened():
    re,img=vid.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        sampleCount+=1
        cv2.imwrite('dataset/user'+'.'+id+'.'+str(sampleCount)+'.jpg',gray[y:y+h,x:x+w])
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow('Taking Data',img)
        cv2.waitKey(10)
    if sampleCount>49:
        break
insert(id,name)
vid.release()
cv2.destroyAllWindows()