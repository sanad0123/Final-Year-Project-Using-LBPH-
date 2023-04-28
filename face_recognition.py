import numpy as np
import lbph_algo as la
import cv2
import mysql.connector
import project_standard as ps








def face_recog():
    myObj = la.LBPHFaceRecognizer(1,8,8,8)
    myObj.histograms = np.load('histograms.npy')
    myObj.labels = np.load('labels.npy')
    def draw_boundary(img,classifier,scaleFactor,minNeighbors):
        gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

        

        for (x,y,w,h) in features:
            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
            id,pred = myObj.predict(gray_image[y:y+h,x:x+w])
            confidence = int((1000*(pred)))

            conn = mysql.connector.connect(host="localhost",username=ps.username,password=ps.password,database=ps.db)
            my_cursor = conn.cursor()

            my_cursor.execute("select Name from student where ID = "+str(id))
            n = my_cursor.fetchone()
            n = "+".join(n)

            my_cursor.execute("select Roll from student where ID = "+str(id))
            r = my_cursor.fetchone()
            r = "+".join(r)
            

            

            i = str(id)
            #i = "+".join(i)

            my_cursor.execute("select Dep from student where ID = "+str(id))
            d = my_cursor.fetchone()
            d = "+".join(d)

            

            
            if confidence > 90 :
                cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
            else:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                
    def recognize(img,faceCascade):
        draw_boundary(img,faceCascade,1.1,10)
        return img
    
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    

    cap = cv2.VideoCapture(0)

    while True:
        ret,img = cap.read()
        img = recognize(img,faceCascade)
        cv2.imshow("Welcome to face recognition & press e to exit",img)
        if cv2.waitKey(1) == 101: #value of e; enter e to exit
            break
    cap.release()
    cv2.destroyAllWindows()

#face_recog()
