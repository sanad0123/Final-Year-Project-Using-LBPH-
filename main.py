from tkinter import*
from tkinter import ttk  #importing tkinter package
from PIL import Image, ImageTk  #importing Pillow package


class Face_Recognition_System :  #defining class
    def __init__(self, root) :    #defining constructor
        self.root = root
        self.root.geometry("1920x1080+0+0")  #setting up areaofwindow + xorigin + yorigin of window
        self.root.title("Smart Attendance System")   #setting title of the window





if __name__ == "__main__":
    root = Tk()  #initializing tk object
    obj = Face_Recognition_System(root)  #initializing Face_Recognition_System object
    root.mainloop()  #calling mainloop fuction of root class