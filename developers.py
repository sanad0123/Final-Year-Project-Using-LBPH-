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
index = []


class Developers :  #defining class
    def __init__(self, root) :    #defining constructor
        self.root = root
        self.screen_width = self.root.winfo_screenwidth() #get the screen width
        self.screen_width_str = str(self.screen_width) #get the screen width in string
        self.screen_height = self.root.winfo_screenheight()-60 #get the screen height and we subtract 70 to eliminate the height of taskbar
        self.screen_height_str = str(self.screen_height) #get the screen height in string
        self.root.geometry(self.screen_width_str + "x" + self.screen_height_str + "+0" + "+0")  #setting up areaofwindow + xorigin + yorigin of window
        self.root.title("Developers")   #setting title of the window

        img_path = IMG_DIR + "/meet_our_team.png"  #path to header image
        width = self.screen_width
        height = self.screen_height
        img = Image.open(img_path)       #opens image of the given path; path is the argument 
        img = img.resize((width,height),Image.Resampling.LANCZOS)   #resize image in lowerlevel i.e. antialias
        self.img = ImageTk.PhotoImage(img)         #setting image as header

        img_lbl = Label(self.root,image=self.img)  #setting label to place image in window
        img_lbl.place(x=0,y=0,width=width,height=height)   #setting position and size of the image to be placed

if __name__ == "__main__":
    root = Tk()  #initializing tk object
    obj = Developers(root)  #initializing Face_Recognition_System object
    root.mainloop()  #calling mainloop fuction of root class