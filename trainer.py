import cv2,os
import numpy as np
from PIL import Image

recognizer = cv2.face.LBPHFaceRecognizer_create()
face_cascade = cv2.CascadeClassifier('classifier/haarcascade_frontalface_default.xml')
path='dataset'

def getImageWithID(path):
     imagePaths = [os.path.join(path, f) for f in os.listdir(path)]
     # print(imagePaths)
     faces = []
     IDs = []
     for imagePath in imagePaths:
         faceImg = Image.open(imagePath).convert('L')
         # Convert the image format into numpy array
         faceNp = np.array(faceImg, 'uint8')
         # Get the label of the image
         ID = int(os.path.split(imagePath)[-1].split(".")[1])
         # Detect the face in the image
         faces.append(faceNp)
         IDs.append(ID)
         cv2.imshow('Training',faceNp)
         cv2.waitKey(10)
     return IDs,faces

IDs,faces= getImageWithID(path)
recognizer.train(faces, np.array(IDs))
recognizer.save('trained_data/trained_data.yml')
cv2.destroyAllWindows()