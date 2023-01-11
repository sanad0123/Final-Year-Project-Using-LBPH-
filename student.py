from tkinter import*
from tkinter import ttk  #importing tkinter package
from PIL import Image, ImageTk  #importing Pillow package
import os #importing os package
import math




ROOT_DIR = str(os.path.abspath(os.curdir))  #finding and converting root directory path into string
IMG_DIR = ROOT_DIR + "/images"      #path of image directory


class Student :  #defining class
    def __init__(self, root) :    #defining constructor
        self.root = root
        self.screen_width = self.root.winfo_screenwidth() #get the screen width
        self.screen_width_str = str(self.screen_width) #get the screen width in string
        self.screen_height = self.root.winfo_screenheight()-60 #get the screen height
        self.screen_height_str = str(self.screen_height) #get the screen height in string
        self.root.geometry(self.screen_width_str + "x" + self.screen_height_str + "+0" + "+0")  #setting up areaofwindow + xorigin + yorigin of window
        self.root.title("Smart Attendance System")   #setting title of the window

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
        h_lbl.place(x=0,y=0,width=header_width,height=header_height)   #setting position and size of the image to be placed in window

        #body section

        background_img_path = IMG_DIR + "/background.png"  #path to background image
        background_width = self.screen_width
        background_height = self.one_tenth_screen_height*8
        background = Image.open(background_img_path)       #opens image of the given path; path is the argument 
        background = background.resize((background_width,background_height),Image.Resampling.LANCZOS)   #resize image in lowerlevel i.e. antialias
        self.background = ImageTk.PhotoImage(background)         #setting image as background

        b_lbl = Label(self.root,image=self.background)  #setting label to place image in window
        b_lbl.place(x=0,y=header_height,width=background_width,height=background_height)   #setting position and size of the image to be placed in window


        # left label frame

        self.one_hundredth_background_height = math.floor(background_height/100)

        xpos_left_frame = self.one_hundredth_screen_width*2
        ypos_left_frame = self.one_hundredth_background_height*2
        left_frame_width = self.one_hundredth_screen_width*48
        left_frame_height = self.one_hundredth_background_height*98

        left_frame = LabelFrame(b_lbl,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",16,"bold"))
        left_frame.place(x=xpos_left_frame,y=ypos_left_frame,width=left_frame_width,height=left_frame_height)

        #Course info

        one_hundredth_left_frame_width = math.floor(left_frame_width/100)
        one_hundredth_left_frame_height = math.floor(left_frame_height/100)

        course_frame_width = one_hundredth_left_frame_width*98
        course_frame_height = one_hundredth_left_frame_height*30
        xpos_course_frame = one_hundredth_left_frame_width*2
        ypos_course_frame = one_hundredth_left_frame_height*20
        course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Course Details",font=("times new roman",12,"bold"))
        course_frame.place(x=xpos_course_frame,y=ypos_course_frame,width=course_frame_width,height=course_frame_height)


        # right label frame

        

        xpos_right_frame = self.one_hundredth_screen_width*52
        ypos_right_frame = self.one_hundredth_background_height*2
        right_frame_width = self.one_hundredth_screen_width*48
        right_frame_height = self.one_hundredth_background_height*98

        right_frame = LabelFrame(b_lbl,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",16,"bold"))
        right_frame.place(x=xpos_right_frame,y=ypos_right_frame,width=right_frame_width,height=right_frame_height)

        #



if __name__ == "__main__":
    root = Tk()  #initializing tk object
    obj = Student(root)  #initializing Face_Recognition_System object
    root.mainloop()  #calling mainloop fuction of root class
