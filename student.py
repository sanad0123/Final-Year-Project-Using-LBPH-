from tkinter import*
from tkinter import ttk  #importing tkinter package
from PIL import Image, ImageTk  #importing Pillow package
import os #importing os package
import math
import project_standard as ps




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

        left_frame = LabelFrame(b_lbl,bd=5,relief=RIDGE,text="Student Details",font=("times new roman",16,"bold"),bg=ps.theme_color)
        left_frame.place(x=xpos_left_frame,y=ypos_left_frame,width=left_frame_width,height=left_frame_height)

        #Course info

        one_hundredth_left_frame_width = math.floor(left_frame_width/100)
        one_hundredth_left_frame_height = math.floor(left_frame_height/100)

        course_frame_width = one_hundredth_left_frame_width*98
        course_frame_height = one_hundredth_left_frame_height*29
        xpos_course_frame = one_hundredth_left_frame_width*2
        ypos_course_frame = one_hundredth_left_frame_height
        course_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Course Details",font=("times new roman",12,"bold"))
        course_frame.place(x=xpos_course_frame,y=ypos_course_frame,width=course_frame_width,height=course_frame_height)

        
        one_hundredth_course_width = math.floor(course_frame_width/100)
        one_hundredth_course_height = math.floor(course_frame_height/100)

        #Department label
        xpos_dep_label = one_hundredth_course_width
        ypos_dep_label = one_hundredth_course_height*10
        dep_label_height = one_hundredth_course_height*40
        dep_label_width = one_hundredth_course_width*24
        dep_label = Label(course_frame,text="Department : ",font=("times new roman",12,"bold"))
        dep_label.place(x=xpos_dep_label,y=ypos_dep_label,width=dep_label_width,height=dep_label_height)

        #Department select box
        xpos_dep_combo = dep_label_width+xpos_dep_label
        ypos_dep_combo = one_hundredth_course_height*10
        dep_combo_height = one_hundredth_course_height*40
        dep_combo_width = one_hundredth_course_width*25

        dep_combo = ttk.Combobox(course_frame,font=("times new roman",12,"bold"),state="readonly")
        dep_combo["values"] = ("Select Department","CSIT","BCA")
        dep_combo.current(0)
        dep_combo.place(x=xpos_dep_combo,y=ypos_dep_combo,width=dep_combo_width, height=dep_combo_height)

        #Course label
        xpos_course_label = one_hundredth_course_width*51
        ypos_course_label = one_hundredth_course_height*10
        course_label_height = one_hundredth_course_height*40
        course_label_width = one_hundredth_course_width*24
        course_label = Label(course_frame,text="Courses : ",font=("times new roman",12,"bold"))
        course_label.place(x=xpos_course_label,y=ypos_course_label,width=course_label_width,height=course_label_height)

        #Course select box
        xpos_course_combo = one_hundredth_course_width*76
        ypos_course_combo = one_hundredth_course_height*10
        course_combo_height = one_hundredth_course_height*40
        course_combo_width = one_hundredth_course_width*24

        course_combo = ttk.Combobox(course_frame,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"] = ("Select Courses","Data mining","IR","Java")
        course_combo.current(0)
        course_combo.place(x=xpos_course_combo,y=ypos_course_combo,width=course_combo_width, height=course_combo_height)

        #Year label
        xpos_year_label = one_hundredth_course_width
        ypos_year_label = one_hundredth_course_height*60
        year_label_height = one_hundredth_course_height*40
        year_label_width = one_hundredth_course_width*24
        year_label = Label(course_frame,text="Years : ",font=("times new roman",12,"bold"))
        year_label.place(x=xpos_year_label,y=ypos_year_label,width=year_label_width,height=year_label_height)

        #Year select box
        xpos_year_combo = year_label_width+xpos_year_label
        ypos_year_combo = one_hundredth_course_height*60
        year_combo_height = one_hundredth_course_height*40
        year_combo_width = one_hundredth_course_width*25

        year_combo = ttk.Combobox(course_frame,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"] = ("Select Years","2075","2076")
        year_combo.current(0)
        year_combo.place(x=xpos_year_combo,y=ypos_year_combo,width=year_combo_width, height=year_combo_height)


        #Semester label
        xpos_sem_label = one_hundredth_course_width*51
        ypos_sem_label = one_hundredth_course_height*60
        sem_label_height = one_hundredth_course_height*40
        sem_label_width = one_hundredth_course_width*24
        sem_label = Label(course_frame,text="Semester : ",font=("times new roman",12,"bold"))
        sem_label.place(x=xpos_sem_label,y=ypos_sem_label,width=sem_label_width,height=sem_label_height)

        #Semester select box
        xpos_sem_combo = one_hundredth_course_width*76
        ypos_sem_combo = one_hundredth_course_height*60
        sem_combo_height = one_hundredth_course_height*40
        sem_combo_width = one_hundredth_course_width*24

        sem_combo = ttk.Combobox(course_frame,font=("times new roman",12,"bold"),state="readonly")
        sem_combo["values"] = ("Select Semester","First","Second","Third","Fourth","Sixth","Seventh","Eighth")
        sem_combo.current(0)
        sem_combo.place(x=xpos_sem_combo,y=ypos_sem_combo,width=sem_combo_width, height=sem_combo_height)


        #Student info

        stuinfo_frame_width = one_hundredth_left_frame_width*98
        stuinfo_frame_height = one_hundredth_left_frame_height*60
        xpos_stuinfo_frame = one_hundredth_left_frame_width*2
        ypos_stuinfo_frame = one_hundredth_left_frame_height*31
        stuinfo_frame = LabelFrame(left_frame,bd=2,relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        stuinfo_frame.place(x=xpos_stuinfo_frame,y=ypos_stuinfo_frame,width=stuinfo_frame_width,height=stuinfo_frame_height)
        stuinfo_frame.columnconfigure(index=0,weight=1)
        stuinfo_frame.columnconfigure(index=1,weight=1)
        stuinfo_frame.columnconfigure(index=2,weight=1)
        stuinfo_frame.columnconfigure(index=3,weight=1)
        stuinfo_frame.rowconfigure(index=0,weight=1)
        stuinfo_frame.rowconfigure(index=1,weight=1)
        stuinfo_frame.rowconfigure(index=2,weight=1)
        stuinfo_frame.rowconfigure(index=3,weight=1)
        stuinfo_frame.rowconfigure(index=4,weight=1)
        stuinfo_frame.rowconfigure(index=5,weight=1)

        
        one_hundredth_stuinfo_width = math.floor(stuinfo_frame_width/100)
        one_hundredth_stuinfo_height = math.floor(stuinfo_frame_height/100)

        


        #student id label
        stu_entry_width = one_hundredth_stuinfo_width*25
        stu_id_label = Label(stuinfo_frame,text="Student ID No. : ",font=("times new roman",12,"bold"))
        stu_id_label.grid(row=0,column=0,sticky=EW)

        stu_id_entry = ttk.Entry(stuinfo_frame,width=20,font=("times new roman",12,"bold"))
        stu_id_entry.grid(row=0,column=1,sticky=W)

        stu_name_label = Label(stuinfo_frame,text="Student Name : ",font=("times new roman",12,"bold"))
        stu_name_label.grid(row=0,column=2,sticky=EW)

        stu_name_entry = ttk.Entry(stuinfo_frame,width=20,font=("times new roman",12,"bold"))
        stu_name_entry.grid(row=0,column=3,sticky=W)

        stu_section_label = Label(stuinfo_frame,text="Sections : ",font=("times new roman",12,"bold"))
        stu_section_label.grid(row=1,column=0,sticky=EW)

        stu_section_combo = ttk.Combobox(stuinfo_frame,font=("times new roman",12,"bold"),state="readonly")
        stu_section_combo["values"] = ("Select Sections","A","B","C")
        stu_section_combo.current(0)
        stu_section_combo.grid(row=1,column=1,sticky=W)

        stu_roll_label = Label(stuinfo_frame,text="Roll No. : ",font=("times new roman",12,"bold"))
        stu_roll_label.grid(row=1,column=2,sticky=EW)

        stu_roll_entry = ttk.Entry(stuinfo_frame,width=20,font=("times new roman",12,"bold"))
        stu_roll_entry.grid(row=1,column=3,sticky=W)

        stu_gender_label = Label(stuinfo_frame,text="Gender : ",font=("times new roman",12,"bold"))
        stu_gender_label.grid(row=2,column=0)

        stu_gender_combo = ttk.Combobox(stuinfo_frame,font=("times new roman",12,"bold"),state="readonly")
        stu_gender_combo["values"] = ("Select Gender","Male","Female")
        stu_gender_combo.current(0)
        stu_gender_combo.grid(row=2,column=1,sticky=W)

        stu_dob_label = Label(stuinfo_frame,text="DOB : ",font=("times new roman",12,"bold"))
        stu_dob_label.grid(row=2,column=2,sticky=EW)

        stu_dob_entry = ttk.Entry(stuinfo_frame,width=20,font=("times new roman",12,"bold"))
        stu_dob_entry.grid(row=2,column=3,sticky=W)

        stu_email_label = Label(stuinfo_frame,text="Email : ",font=("times new roman",12,"bold"))
        stu_email_label.grid(row=3,column=0,sticky=EW)

        stu_email_entry = ttk.Entry(stuinfo_frame,width=20,font=("times new roman",12,"bold"))
        stu_email_entry.grid(row=3,column=1,sticky=W)

        stu_phone_label = Label(stuinfo_frame,text="Phone : ",font=("times new roman",12,"bold"))
        stu_phone_label.grid(row=3,column=2,sticky=EW)

        stu_phone_entry = ttk.Entry(stuinfo_frame,width=20,font=("times new roman",12,"bold"))
        stu_phone_entry.grid(row=3,column=3,sticky=W)

        stu_address_label = Label(stuinfo_frame,text="Address : ",font=("times new roman",12,"bold"))
        stu_address_label.grid(row=4,column=0,sticky=EW)

        stu_address_entry = ttk.Entry(stuinfo_frame,width=20,font=("times new roman",12,"bold"))
        stu_address_entry.grid(row=4,column=1,sticky=W)

        stu_teacher_label = Label(stuinfo_frame,text="Teacher Name : ",font=("times new roman",12,"bold"))
        stu_teacher_label.grid(row=4,column=2,sticky=EW)

        stu_teacher_entry = ttk.Entry(stuinfo_frame,width=20,font=("times new roman",12,"bold"))
        stu_teacher_entry.grid(row=4,column=3,sticky=W)

        radiobtn1 = ttk.Radiobutton(stuinfo_frame,text="Take photo Sample",value=1)
        radiobtn1.grid(row=5,column=0,columnspan=2)

        radiobtn2 = ttk.Radiobutton(stuinfo_frame,text="No photo Sample",value=0)
        radiobtn2.grid(row=5,column=2,columnspan=2)




       
        
        



        #Button section of left frame

        button_width = one_hundredth_left_frame_width*23
        button_height = one_hundredth_left_frame_height*9

        #button_1
        button1_img_path = IMG_DIR + "/button.png"
        button1 = Image.open(button1_img_path)
        button1 = button1.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button1 = ImageTk.PhotoImage(button1)

        button_label_1 = Button(left_frame,image=self.button1,cursor="hand2",bd=0)
        button1_xpos = one_hundredth_left_frame_width*2
        button1_ypos = one_hundredth_left_frame_height*92
        button_label_1.place(x=button1_xpos,y=button1_ypos,width=button_width,height=button_height)

        #button_2
        button2_img_path = IMG_DIR + "/button.png"
        button2 = Image.open(button2_img_path)
        button2 = button2.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button2 = ImageTk.PhotoImage(button2)

        button_label_2 = Button(left_frame,image=self.button2,cursor="hand2",bd=0)
        button2_xpos = one_hundredth_left_frame_width*27
        button2_ypos = one_hundredth_left_frame_height*92
        button_label_2.place(x=button2_xpos,y=button2_ypos,width=button_width,height=button_height)

        #button_3
        button3_img_path = IMG_DIR + "/button.png"
        button3 = Image.open(button3_img_path)
        button3 = button3.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button3 = ImageTk.PhotoImage(button3)

        button_label_3 = Button(left_frame,image=self.button3,cursor="hand2",bd=0)
        button3_xpos = one_hundredth_left_frame_width*52
        button3_ypos = one_hundredth_left_frame_height*92
        button_label_3.place(x=button3_xpos,y=button3_ypos,width=button_width,height=button_height)

        #button_4
        button4_img_path = IMG_DIR + "/button.png"
        button4 = Image.open(button4_img_path)
        button4 = button4.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button4 = ImageTk.PhotoImage(button4)

        button_label_4 = Button(left_frame,image=self.button4,cursor="hand2",bd=0)
        button4_xpos = one_hundredth_left_frame_width*77
        button4_ypos = one_hundredth_left_frame_height*92
        button_label_4.place(x=button4_xpos,y=button4_ypos,width=button_width,height=button_height)

        #width of button 5 and button 6
        lower_button_width =one_hundredth_left_frame_width*49

        #button_5
        button5_img_path = IMG_DIR + "/button.png"
        button5 = Image.open(button5_img_path)
        button5 = button5.resize((lower_button_width,button_height),Image.Resampling.LANCZOS)
        self.button5 = ImageTk.PhotoImage(button5)

        button_label_5 = Button(left_frame,image=self.button5,cursor="hand2",bd=0)
        button1_xpos = one_hundredth_left_frame_width*2
        button1_ypos = one_hundredth_left_frame_height*102
        button_label_5.place(x=button1_xpos,y=button1_ypos,width=lower_button_width,height=button_height)

        #button_6
        button6_img_path = IMG_DIR + "/button.png"
        button6 = Image.open(button6_img_path)
        button6 = button6.resize((lower_button_width,button_height),Image.Resampling.LANCZOS)
        self.button6 = ImageTk.PhotoImage(button6)

        button_label_6 = Button(left_frame,image=self.button6,cursor="hand2",bd=0)
        button6_xpos = one_hundredth_left_frame_width*51
        button6_ypos = one_hundredth_left_frame_height*102
        button_label_6.place(x=button6_xpos,y=button6_ypos,width=lower_button_width,height=button_height)







        # right label frame

        

        xpos_right_frame = self.one_hundredth_screen_width*52
        ypos_right_frame = self.one_hundredth_background_height*2
        right_frame_width = self.one_hundredth_screen_width*48
        right_frame_height = self.one_hundredth_background_height*98

        right_frame = LabelFrame(b_lbl,bd=5,relief=RIDGE,text="Search For Students",font=("times new roman",16,"bold"),bg=ps.theme_color)
        right_frame.place(x=xpos_right_frame,y=ypos_right_frame,width=right_frame_width,height=right_frame_height)
        right_frame.rowconfigure(index=0,weight=1)
        right_frame.rowconfigure(index=1,weight=1)
        right_frame.rowconfigure(index=2,weight=8)
        right_frame.columnconfigure(index=0,weight=1)
        right_frame.columnconfigure(index=1,weight=1)
        right_frame.columnconfigure(index=2,weight=1)
        right_frame.columnconfigure(index=3,weight=1)
        right_frame.columnconfigure(index=4,weight=1)

        one_hundredth_right_frame_height = math.floor(right_frame_height/100)
        one_hundredth_right_frame_width = math.floor(right_frame_width/100)

        #search by label
        search_by_label = Label(right_frame,text="Search By ",font=("times new roman",12,"bold"),background=ps.theme_color)
        search_by_label.grid(row=0,column=0,sticky=EW)

        #search option
        search_combo = ttk.Combobox(right_frame,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"] = ("Select Options","Roll No.","Student ID no.","Student name")
        search_combo.current(0)
        search_combo.grid(row=0,column=1)

        #search entry field
        stu_search_entry = ttk.Entry(right_frame,width=18,font=("times new roman",12,"bold"))
        stu_search_entry.grid(row=0,column=2)

        #Search button
        search_img_path = IMG_DIR + "/button.png"
        search_button = Image.open(search_img_path)
        search_button_height = one_hundredth_right_frame_height*5
        search_button_width = one_hundredth_right_frame_width*20
        search_button = search_button.resize((search_button_width,search_button_height),Image.Resampling.LANCZOS)
        self.search_button = ImageTk.PhotoImage(search_button)

        search_button_label = Button(right_frame,image=self.search_button,cursor="hand2",bd=0)
        search_button_label.grid(row=0,column=3)


        #Show all button
        show_img_path = IMG_DIR + "/button.png"
        show_button = Image.open(show_img_path)
        show_button_height = one_hundredth_right_frame_height*5
        show_button_width = one_hundredth_right_frame_width*20
        show_button = show_button.resize((show_button_width,show_button_height),Image.Resampling.LANCZOS)
        self.show_button = ImageTk.PhotoImage(show_button)

        show_button_label = Button(right_frame,image=self.show_button,cursor="hand2",bd=0)
        show_button_label.grid(row=0,column=4)
        



if __name__ == "__main__":
    root = Tk()  #initializing tk object
    obj = Student(root)  #initializing Face_Recognition_System object
    root.mainloop()  #calling mainloop fuction of root class
