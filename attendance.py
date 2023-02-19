from tkinter import*
from tkinter import ttk  #importing tkinter package
from PIL import Image, ImageTk  #importing Pillow package
import os #importing os package
import math
import project_standard as ps
from student import Student
from tkinter import messagebox
import train
from time import strftime
from datetime import datetime
import cv2
import csv
from tkinter import filedialog
import mysql.connector
import face_recognition as f_r



ROOT_DIR = str(os.path.abspath(os.curdir))  #finding and converting root directory path into string
IMG_DIR = ROOT_DIR + "/images"      #path of image directory

mydata = []


class Attendance :  #defining class
    def __init__(self, root) :    #defining constructor
        self.root = root
        self.screen_width = self.root.winfo_screenwidth() #get the screen width
        self.screen_width_str = str(self.screen_width) #get the screen width in string
        self.screen_height = self.root.winfo_screenheight()-60 #get the screen height and we subtract 70 to eliminate the height of taskbar
        self.screen_height_str = str(self.screen_height) #get the screen height in string
        self.root.geometry(self.screen_width_str + "x" + self.screen_height_str + "+0" + "+0")  #setting up areaofwindow + xorigin + yorigin of window
        self.root.title("Attendance System")   #setting title of the window
        self.root.rowconfigure(index=0, weight=2)
        self.root.rowconfigure(index=1, weight=8)
        self.root.columnconfigure(index=0, weight=1)

        # for responsive design
        self.one_tenth_screen_height = int(self.screen_height/10)    #1/10 of screen height
        self.one_hundredth_screen_width = math.floor(self.screen_width/100)     #1/100 of screen width


        # header section

        header_img_path = IMG_DIR + "/header.png"  #path to header image
        header_width = self.screen_width
        header_height = self.one_tenth_screen_height*2
        header = Image.open(header_img_path)       #opens image of the given path; path is the argument 
        header = header.resize((header_width,header_height),Image.Resampling.LANCZOS)   #resize image in lowerlevel i.e. antialias
        self.header = ImageTk.PhotoImage(header)         #setting image as header

        h_lbl = Label(self.root,image=self.header)  #setting label to place image in window
        h_lbl.grid(row=0,column=0,sticky=N)   #setting position and size of the image to be placed in window

        #body section

        

        background_img_path = IMG_DIR + "/background.png"  #path to background image
        background_width = self.screen_width
        background_height = self.one_tenth_screen_height*8
        background = Image.open(background_img_path)       #opens image of the given path; path is the argument 
        background = background.resize((background_width,background_height),Image.Resampling.LANCZOS)   #resize image in lowerlevel i.e. antialias
        self.background = ImageTk.PhotoImage(background)         #setting image as background

        

        b_lbl = Label(self.root,image=self.background,borderwidth=5,border=5)  #setting label to place image in window
        b_lbl.grid(row=1,column=0,sticky=N)   #setting position and size of the image to be placed in window

        self.one_hundredth_background_height = math.floor(background_height/100)
       
        

        
        

        # left label frame

        

        xpos_left_frame = self.one_hundredth_screen_width*2
        ypos_left_frame = self.one_hundredth_background_height*2
        left_frame_width = self.one_hundredth_screen_width*48
        left_frame_height = self.one_hundredth_background_height*78

        left_frame = LabelFrame(b_lbl,bd=5,relief=RIDGE,text="Edit Attendance",font=("times new roman",16,"bold"),bg=ps.theme_color)
        left_frame.place(x=xpos_left_frame,y=ypos_left_frame,width=left_frame_width,height=left_frame_height)

        one_seventeenth_left_frame_width = math.floor(left_frame_width/17) #1/17
        one_thirteenth_left_frame_height = math.floor(left_frame_height/13) #1/13

        # lables or entry width and height

        widget_width = one_seventeenth_left_frame_width*3
        widget_height = one_thirteenth_left_frame_height*2

        # x positions
        row_first_pos = one_seventeenth_left_frame_width
        row_second_pos = one_seventeenth_left_frame_width*4
        row_third_pos = one_seventeenth_left_frame_width*8
        row_fourth_pos = one_seventeenth_left_frame_width*12

        # y positions
        column_first_pos = one_thirteenth_left_frame_height
        column_second_pos = one_thirteenth_left_frame_height*4
        column_third_pos = one_thirteenth_left_frame_height*7
        column_fourth_pos = one_thirteenth_left_frame_height*10

        #Id label
        
        
        id_label = Label(left_frame,text="Student ID : ",font=("times new roman",12,"bold"),bg=ps.theme_color)
        id_label.place(x=row_first_pos,y=column_first_pos,width=widget_width)

        id_entry = ttk.Entry(left_frame,font=("times new roman",12,"bold"))
        id_entry.place(x=row_second_pos,y=column_first_pos,width=widget_width)

        #Roll label
        
        
        roll_label = Label(left_frame,text="Roll : ",font=("times new roman",12,"bold"),bg=ps.theme_color)
        roll_label.place(x=row_third_pos,y=column_first_pos,width=widget_width)

        roll_entry = ttk.Entry(left_frame,font=("times new roman",12,"bold"))
        roll_entry.place(x=row_fourth_pos,y=column_first_pos,width=widget_width)

        #Name label
        
        
        name_label = Label(left_frame,text="Name : ",font=("times new roman",12,"bold"),bg=ps.theme_color)
        name_label.place(x=row_first_pos,y=column_second_pos,width=widget_width)

        name_entry = ttk.Entry(left_frame,font=("times new roman",12,"bold"))
        name_entry.place(x=row_second_pos,y=column_second_pos,width=widget_width)

        #Department label
        
        
        dep_label = Label(left_frame,text="Department : ",font=("times new roman",12,"bold"),bg=ps.theme_color)
        dep_label.place(x=row_third_pos,y=column_second_pos,width=widget_width)

        dep_entry = ttk.Entry(left_frame,font=("times new roman",12,"bold"))
        dep_entry.place(x=row_fourth_pos,y=column_second_pos,width=widget_width)

        #Time label
        
        
        time_label = Label(left_frame,text="Time : ",font=("times new roman",12,"bold"),bg=ps.theme_color)
        time_label.place(x=row_first_pos,y=column_third_pos,width=widget_width)

        time_entry = ttk.Entry(left_frame,font=("times new roman",12,"bold"))
        time_entry.place(x=row_second_pos,y=column_third_pos,width=widget_width)

        #Date label
        
        
        date_label = Label(left_frame,text="Date : ",font=("times new roman",12,"bold"),bg=ps.theme_color)
        date_label.place(x=row_third_pos,y=column_third_pos,width=widget_width)

        date_entry = ttk.Entry(left_frame,font=("times new roman",12,"bold"))
        date_entry.place(x=row_fourth_pos,y=column_third_pos,width=widget_width)

        #Subject label
        
        
        course_label = Label(left_frame,text="Course : ",font=("times new roman",12,"bold"),bg=ps.theme_color)
        course_label.place(x=row_first_pos,y=column_fourth_pos,width=widget_width)

        course_entry = ttk.Entry(left_frame,font=("times new roman",12,"bold"))
        course_entry.place(x=row_second_pos,y=column_fourth_pos,width=widget_width)

        #Date label
        
        
        attendance_label = Label(left_frame,text="Attendance Status: ",font=("times new roman",12,"bold"),bg=ps.theme_color)
        attendance_label.place(x=row_third_pos,y=column_fourth_pos,width=widget_width)

        attendance_combo = ttk.Combobox(left_frame,font=("times new roman",12,"bold"),state="readonly")
        attendance_combo["values"] = ("Status","Present","Absent")
        attendance_combo.current(0)
        attendance_combo.place(x=row_fourth_pos,y=column_fourth_pos,width=widget_width)

        


        # right label frame

        

        xpos_right_frame = self.one_hundredth_screen_width*52
        ypos_right_frame = self.one_hundredth_background_height*2
        right_frame_width = self.one_hundredth_screen_width*48
        right_frame_height = self.one_hundredth_background_height*78

        right_frame = LabelFrame(b_lbl,bd=5,relief=RIDGE,text="Attendance Report",font=("times new roman",16,"bold"),bg=ps.theme_color)
        right_frame.place(x=xpos_right_frame,y=ypos_right_frame,width=right_frame_width,height=right_frame_height)

        one_hundredth_right_frame_height = math.floor(right_frame_height/100)

        # table 

        scroll_x = ttk.Scrollbar(right_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(right_frame,orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(right_frame,column=("ID","Roll","Name","Dep","Time","Date","Course","Attendance"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("ID",text="Student ID")
        self.AttendanceReportTable.heading("Roll",text="Roll")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Dep",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Course",text="Course")
        self.AttendanceReportTable.heading("Attendance",text="Attendance")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("ID",width=100)
        self.AttendanceReportTable.column("Roll",width=100)
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Dep",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Course",width=100)
        self.AttendanceReportTable.column("Attendance",width=100)

        self.AttendanceReportTable.pack(fill=BOTH,expand=1)

        #button size
        self.one_sixteenth_screen_width = math.floor(self.screen_width/16)
        button_width = self.one_sixteenth_screen_width*2
        button_height = self.one_hundredth_background_height*16

        #button_1
        button1_img_path = IMG_DIR + "/save.png"
        button1 = Image.open(button1_img_path)
        button1 = button1.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button1 = ImageTk.PhotoImage(button1)

        button_label_1 = Button(b_lbl,command=self.take_attendance,image=self.button1,cursor="hand2",bd=0)
        button1_xpos = self.one_sixteenth_screen_width
        button1_ypos = self.one_hundredth_background_height*85
        button_label_1.place(x=button1_xpos,y=button1_ypos,width=button_width,height=button_height)

        #button_2
        button2_img_path = IMG_DIR + "/update.png"
        button2 = Image.open(button2_img_path)
        button2 = button2.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button2 = ImageTk.PhotoImage(button2)

        button_label_2 = Button(b_lbl,image=self.button2,cursor="hand2",bd=0)
        button2_xpos = self.one_sixteenth_screen_width*4
        button2_ypos = self.one_hundredth_background_height*85
        button_label_2.place(x=button2_xpos,y=button2_ypos,width=button_width,height=button_height)

        #button_3
        button3_img_path = IMG_DIR + "/reset.png"
        button3 = Image.open(button3_img_path)
        button3 = button3.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button3 = ImageTk.PhotoImage(button3)

        button_label_3 = Button(b_lbl,image=self.button3,cursor="hand2",bd=0)
        button3_xpos = self.one_sixteenth_screen_width*7
        button3_ypos = self.one_hundredth_background_height*85
        button_label_3.place(x=button3_xpos,y=button3_ypos,width=button_width,height=button_height)

        #button_4
        button4_img_path = IMG_DIR + "/reset.png"
        button4 = Image.open(button4_img_path)
        button4 = button4.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button4 = ImageTk.PhotoImage(button4)

        button_label_4 = Button(b_lbl,command=self.importCsv,image=self.button4,cursor="hand2",bd=0)
        button4_xpos = self.one_sixteenth_screen_width*10
        button4_ypos = self.one_hundredth_background_height*85
        button_label_4.place(x=button4_xpos,y=button4_ypos,width=button_width,height=button_height)

        
        #button_5
        button5_img_path = IMG_DIR + "/addphotosample.png"
        button5 = Image.open(button5_img_path)
        button5 = button5.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button5 = ImageTk.PhotoImage(button5)

        button_label_5 = Button(b_lbl,image=self.button5,cursor="hand2",bd=0)
        button1_xpos = self.one_sixteenth_screen_width*13
        button1_ypos = self.one_hundredth_background_height*85
        button_label_5.place(x=button1_xpos,y=button1_ypos,width=button_width,height=button_height)

    # function for taking attendance
    def take_attendance(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,clf):
            gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord = []

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict = clf.predict(gray_image[y:y+h,x:x+w])
                confidence = int((100*(1-predict/300)))

                conn = mysql.connector.connect(host="localhost",username=ps.username,password=ps.password,database=ps.db)
                my_cursor = conn.cursor()

                my_cursor.execute("select Name from student where ID = "+str(id))
                n = my_cursor.fetchone()
                n = "+".join(n)

                
                i = str(id)
                i = "+".join(i)

                my_cursor.execute("select Roll from student where ID = "+str(id))
                r = my_cursor.fetchone()
                r = "+".join(r)

                my_cursor.execute("select Course from student where ID = "+str(id))
                c = my_cursor.fetchone()
                c = "+".join(c)

                my_cursor.execute("select Dep from student where ID = "+str(id))
                d = my_cursor.fetchone()
                d = "+".join(d)

                if confidence > 77 :
                    cv2.putText(img,f"Course:{c}",(x,y-100),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"ID:{i}",(x,y-80),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(n,i,r,c,d)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord = [x,y,w,h]

            return coord
        
        def recognize(img,clf,faceCascade):
            coord = draw_boundary(img,faceCascade,1.1,10,clf)
            return img
        
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")

        cap = cv2.VideoCapture(0)

        while True:
            ret,img = cap.read()
            img = recognize(img,clf,faceCascade)
            cv2.imshow("Taking Attendance & press e to exit",img)
            if cv2.waitKey(1) == 101: #value of e; enter e to exit
                break
        cap.release()
        cv2.destroyAllWindows()
        self.todayCsv()
        messagebox.showinfo("Success","Attendance Taken Successfully",parent=self.root)

    # ================== attendance ====================
    def mark_attendance(self,n,i,r,c,d):
        now = datetime.now()
        today = now.strftime("%d-%b-%Y")
        file_name = "attendance/"+today+".csv"
        with open(file_name,"w+",newline="\n") as f:
            myDataList = f.readlines()
            name_list = []
            for line in myDataList:
                entry = line.split((",")) #[[id],[name]] where line is id,name
                name_list.append(entry[0]) #name_list = [id]
            if(i not in name_list):
                
                date = now.strftime("%d/%m/%Y")
                time = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{time},{date},{c},Present")

    # ============== fetch data =========================
    def fetch_data(self,rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows :
            self.AttendanceReportTable.insert("",END,values=i)

    def importCsv(self):
        global mydata
        fln = filedialog.askopenfilename(initialdir="attendance/",title="Open CSV",filetypes=(("CSV File","*.csv"),("ALL File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread  = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            mydata.pop(0)  # this done cause first line 
            self.fetch_data(mydata)

    def todayCsv(self):
        global mydata
        now = datetime.now()
        today = now.strftime("%d-%b-%Y")
        file_name = "attendance/"+today+".csv"
        with open(file_name) as myfile:
            csvread  = csv.reader(myfile,delimiter=",")
            for i in csvread:
                mydata.append(i)
            mydata.pop(0)  # this done cause first line 
            self.fetch_data(mydata)




        

        




if __name__ == "__main__":
    root = Tk()  #initializing tk object
    obj = Attendance(root)  #initializing Face_Recognition_System object
    root.mainloop()  #calling mainloop fuction of root class