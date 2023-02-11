from tkinter import*
from tkinter import ttk  #importing tkinter package
from tkinter import messagebox
import os
from PIL import Image, ImageTk
import numpy as np
import cv2



def train_classifier():
    data_dir = ("data")
    path = [os.path.join(data_dir,file) for file in os.listdir(data_dir) ]

    faces = []
    ids = []

    for image in path :
        img = Image.open(image).convert('L') #Grayscale iamge
        imageNp = np.array(img,'uint8')
        id = int(os.path.split(image)[1].split('.')[1])

        faces.append(imageNp)
        ids.append(id)
        cv2.imshow("Training data sets and enter e to exit",imageNp)
        cv2.waitKey(1) == 101 #value of e; enter e to exit

    ids = np.array(ids)


    # =============== Train the classifier and save ================
            
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces,ids)
    clf.write("classifier.xml")
    cv2.destroyAllWindows()

    

            

        
        










    

    