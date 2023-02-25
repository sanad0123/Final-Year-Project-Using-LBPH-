from tkinter import*
from tkinter import ttk  #importing tkinter package
from PIL import Image, ImageTk  #importing Pillow package
import os #importing os package
import math
from student import Student
from attendance import Attendance
from developers import Developers
from tkinter import messagebox
import train
import face_recognition as f_r



ROOT_DIR = str(os.path.abspath(os.curdir))  #finding and converting root directory path into string
IMG_DIR = ROOT_DIR + "/images"      #path of image directory


class Face_Recognition_System :  #defining class
    def __init__(self, root) :    #defining constructor
        self.root = root
        self.screen_width = self.root.winfo_screenwidth() #get the screen width
        self.screen_width_str = str(self.screen_width) #get the screen width in string
        self.screen_height = self.root.winfo_screenheight()-60 #get the screen height and we subtract 70 to eliminate the height of taskbar
        self.screen_height_str = str(self.screen_height) #get the screen height in string
        self.root.geometry(self.screen_width_str + "x" + self.screen_height_str + "+0" + "+0")  #setting up areaofwindow + xorigin + yorigin of window
        self.root.title("Smart Attendance System")   #setting title of the window

        # for responsive design
        self.one_tenth_screen_height = math.floor(self.screen_height/10)  #1/10 of screen height
        self.one_tenth_screen_width = math.floor(self.screen_width/10)   #1/10 of screen weidth

        # header section

        header_img_path = IMG_DIR + "/header.png"  #path to header image
        header_width = self.screen_width
        header_height = self.one_tenth_screen_height*2
        header = Image.open(header_img_path)       #opens image of the given path; path is the argument 
        header = header.resize((header_width,header_height),Image.Resampling.LANCZOS)   #resize image in lowerlevel i.e. antialias
        self.header = ImageTk.PhotoImage(header)         #setting image as header

        h_lbl = Label(self.root,image=self.header)  #setting label to place image in window
        h_lbl.place(x=0,y=0,width=header_width,height=header_height)   #setting position and size of the image to be placed in window

        # body section

        background_img_path = IMG_DIR + "/background.png"  #path to background image
        background_width = self.screen_width
        background_height = self.one_tenth_screen_height*8
        background = Image.open(background_img_path)       #opens image of the given path; path is the argument 
        background = background.resize((background_width,background_height),Image.Resampling.LANCZOS)   #resize image in lowerlevel i.e. antialias
        self.background = ImageTk.PhotoImage(background)         #setting image as background

        b_lbl = Label(self.root,image=self.background)  #setting label to place image in window
        b_lbl.place(x=0,y=header_height,width=background_width,height=background_height)   #setting position and size of the image to be placed in window

        # button section
        button_width = int(self.one_tenth_screen_width*2)
        button_height = int((background_height/11))

        #button_1
        button1_img_path = IMG_DIR + "/attendance.png"
        button1 = Image.open(button1_img_path)
        button1 = button1.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button1 = ImageTk.PhotoImage(button1)

        button_label_1 = Button(b_lbl,command=self.attendance,image=self.button1,cursor="hand2",bd=0)
        button1_xpos = self.one_tenth_screen_width
        button1_ypos = (background_height/11)*2
        button_label_1.place(x=button1_xpos,y=button1_ypos,width=button_width,height=button_height)

        # button_2

        button2_img_path = IMG_DIR + "/facedetector.png"
        button2 = Image.open(button2_img_path)
        button2 = button2.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button2 = ImageTk.PhotoImage(button2)

        button_label_2 = Button(b_lbl,command=f_r.face_recog,image=self.button2,cursor="hand2",bd=0)
        button2_xpos = (self.one_tenth_screen_width)*4
        button2_ypos = (background_height/11)*2
        button_label_2.place(x=button2_xpos,y=button2_ypos,width=button_width,height=button_height)

        # button_3

        button3_img_path = IMG_DIR + "/traindata.png"
        button3 = Image.open(button3_img_path)
        button3 = button3.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button3 = ImageTk.PhotoImage(button3)

        button_label_3 = Button(b_lbl,command=self.train_data,image=self.button3,cursor="hand2",bd=0)
        button3_xpos = (self.one_tenth_screen_width)*7
        button3_ypos = (background_height/11)*2
        button_label_3.place(x=button3_xpos,y=button3_ypos,width=button_width,height=button_height)

        # button_4

        button4_img_path = IMG_DIR + "/photos.png"
        button4 = Image.open(button4_img_path)
        button4 = button4.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button4 = ImageTk.PhotoImage(button4)

        button_label_4 = Button(b_lbl,command=self.open_img,image=self.button4,cursor="hand2",bd=0)
        button4_xpos = (self.one_tenth_screen_width)*2
        button4_ypos = (background_height/11)*5
        button_label_4.place(x=button4_xpos,y=button4_ypos,width=button_width,height=button_height)


        # button_5

        button5_img_path = IMG_DIR + "/studentdetails.png"
        button5 = Image.open(button5_img_path)
        button5 = button5.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button5 = ImageTk.PhotoImage(button5)

        button_label_5 = Button(b_lbl,command=self.student_details,image=self.button5,cursor="hand2",bd=0)
        button5_xpos = (self.one_tenth_screen_width)*6
        button5_ypos = (background_height/11)*5
        button_label_5.place(x=button5_xpos,y=button5_ypos,width=button_width,height=button_height)

        # button_6

        button6_img_path = IMG_DIR + "/developers.png"
        button6 = Image.open(button6_img_path)
        button6 = button6.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button6 = ImageTk.PhotoImage(button6)

        button_label_6 = Button(b_lbl,command=self.developers,image=self.button6,cursor="hand2",bd=0)
        button6_xpos = (self.one_tenth_screen_width)
        button6_ypos = (background_height/11)*8
        button_label_6.place(x=button6_xpos,y=button6_ypos,width=button_width,height=button_height)

        # button_7

        button7_img_path = IMG_DIR + "/helpdesk.png"
        button7 = Image.open(button7_img_path)
        button7 = button7.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button7 = ImageTk.PhotoImage(button7)

        button_label_7 = Button(b_lbl,image=self.button7,cursor="hand2",bd=0)
        button7_xpos = (self.one_tenth_screen_width)*4
        button7_ypos = (background_height/11)*8
        button_label_7.place(x=button7_xpos,y=button7_ypos,width=button_width,height=button_height)

        # button_8

        button8_img_path = IMG_DIR + "/exit.png"
        button8 = Image.open(button8_img_path)
        button8 = button8.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button8 = ImageTk.PhotoImage(button8)

        button_label_8 = Button(b_lbl,command=self.exit,image=self.button8,cursor="hand2",bd=0)
        button8_xpos = (self.one_tenth_screen_width)*7
        button8_ypos = (background_height/11)*8
        button_label_8.place(x=button8_xpos,y=button8_ypos,width=button_width,height=button_height)


    # ================= Functions Button ==============================
    #Function for creating new window from main window buttons
    def student_details(self):
            self.new_window = Toplevel(self.root)
            self.app = Student(self.new_window)


    #Function for creating new window from main window buttons
    def attendance(self):
            self.new_window = Toplevel(self.root)
            self.app = Attendance(self.new_window)

    #Function for creating new window from main window buttons
    def developers(self):
            self.new_window = Toplevel(self.root)
            self.app = Developers(self.new_window)

    #Function for creating new window from train data window buttons
    def train_data(self):
        train.train_classifier()
        messagebox.showinfo("Result","Training datasets completed !!",parent=self.root)
             


    # ====================== Function for photos button ===================
    def open_img(self):
         os.startfile("data")


    # ===================== Function for exit ====================
    def exit(self):
        self.iexit = messagebox.askyesno("Exit","Are you sure you want to exit?",parent=self.root)
        if self.iexit > 0:
            self.root.destroy()
        else :
            return
           

        










if __name__ == "__main__":
    root = Tk()  #initializing tk object
    obj = Face_Recognition_System(root)  #initializing Face_Recognition_System object
    root.mainloop()  #calling mainloop fuction of root class

    