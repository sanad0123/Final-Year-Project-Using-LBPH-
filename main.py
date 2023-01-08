from tkinter import*
from tkinter import ttk  #importing tkinter package
from PIL import Image, ImageTk  #importing Pillow package
import os #importing os package

#main theme color used  #81b622

ROOT_DIR = str(os.path.abspath(os.curdir))  #finding and converting root directory path into string
IMG_DIR = ROOT_DIR + "/images"      #path of image directory


class Face_Recognition_System :  #defining class
    def __init__(self, root) :    #defining constructor
        self.root = root
        self.root.geometry("1920x1080+0+0")  #setting up areaofwindow + xorigin + yorigin of window
        self.root.title("Smart Attendance System")   #setting title of the window

        # header section

        header_img_path = IMG_DIR + "/nav_bar.png"  #path to header image
        header = Image.open(header_img_path)       #opens image of the given path; path is the argument 
        header = header.resize((1540,200),Image.ANTIALIAS)   #resize image in lowerlevel i.e. antialias
        self.header = ImageTk.PhotoImage(header)         #setting image as header

        h_lbl = Label(self.root,image=self.header)  #setting label to place image in window
        h_lbl.place(x=0,y=0,width=1540,height=200)   #setting position and size of the image to be placed in window

        # body section

        background_img_path = IMG_DIR + "/background.png"  #path to background image
        background = Image.open(background_img_path)       #opens image of the given path; path is the argument 
        background = background.resize((1540,600),Image.ANTIALIAS)   #resize image in lowerlevel i.e. antialias
        self.background = ImageTk.PhotoImage(background)         #setting image as background

        b_lbl = Label(self.root,image=self.background)  #setting label to place image in window
        b_lbl.place(x=0,y=200,width=1540,height=600)   #setting position and size of the image to be placed in window

        # button section


        #button_1
        button1_img_path = IMG_DIR + "/button.png"
        button1 = Image.open(button1_img_path)
        button1 = button1.resize((310,120),Image.ANTIALIAS)
        self.button1 = ImageTk.PhotoImage(button1)

        button_label_1 = Button(b_lbl,image=self.button1,cursor="hand2")
        button_label_1.place(x=155,y=120,width=310,height=120)

        # button_2

        button2_img_path = IMG_DIR + "/button.png"
        button2 = Image.open(button2_img_path)
        button2 = button2.resize((310,120),Image.ANTIALIAS)
        self.button2 = ImageTk.PhotoImage(button2)

        button_label_2 = Button(b_lbl,image=self.button2,cursor="hand2")
        button_label_2.place(x=620,y=120,width=310,height=120)

        # button_3

        button3_img_path = IMG_DIR + "/button.png"
        button3 = Image.open(button2_img_path)
        button3 = button3.resize((310,120),Image.ANTIALIAS)
        self.button3 = ImageTk.PhotoImage(button3)

        button_label_3 = Button(b_lbl,image=self.button3,cursor="hand2")
        button_label_3.place(x=1085,y=120,width=310,height=120)





if __name__ == "__main__":
    root = Tk()  #initializing tk object
    obj = Face_Recognition_System(root)  #initializing Face_Recognition_System object
    root.mainloop()  #calling mainloop fuction of root class