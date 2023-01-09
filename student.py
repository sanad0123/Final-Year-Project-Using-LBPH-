from tkinter import*
from tkinter import ttk  #importing tkinter package
from PIL import Image, ImageTk  #importing Pillow package
import os #importing os package



ROOT_DIR = str(os.path.abspath(os.curdir))  #finding and converting root directory path into string
IMG_DIR = ROOT_DIR + "/images"      #path of image directory


class Student :  #defining class
    def __init__(self, root) :    #defining constructor
        self.root = root
        self.screen_width = self.root.winfo_screenwidth() #get the screen width
        self.screen_width_str = str(self.root.winfo_screenwidth()) #get the screen width in string
        self.screen_height = self.root.winfo_screenheight() #get the screen height
        self.screen_height_str = str(self.root.winfo_screenheight()) #get the screen height in string
        self.root.geometry(self.screen_width_str + "x" + self.screen_height_str + "+0" + "+0")  #setting up areaofwindow + xorigin + yorigin of window
        self.root.title("Smart Attendance System")   #setting title of the window

        # for responsive design
        self.one_tenth_screen_height = int(self.screen_height/10)    #1/10 of screen height
        self.one_tenth_screen_width = int(self.screen_width/10)     #1/10 of screen width

        # header section

        header_img_path = IMG_DIR + "/nav_bar.png"  #path to header image
        header_width = self.screen_width
        header_height = self.one_tenth_screen_height*2
        header = Image.open(header_img_path)       #opens image of the given path; path is the argument 
        header = header.resize((header_width,header_height),Image.Resampling.LANCZOS)   #resize image in lowerlevel i.e. antialias
        self.header = ImageTk.PhotoImage(header)         #setting image as header

        h_lbl = Label(self.root,image=self.header)  #setting label to place image in window
        h_lbl.place(x=0,y=0,width=header_width,height=header_height)   #setting position and size of the image to be placed in window



if __name__ == "__main__":
    root = Tk()  #initializing tk object
    obj = Student(root)  #initializing Face_Recognition_System object
    root.mainloop()  #calling mainloop fuction of root class
