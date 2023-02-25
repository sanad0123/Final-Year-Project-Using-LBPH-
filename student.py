from tkinter import*
from tkinter import ttk  #importing tkinter package
from PIL import Image, ImageTk  #importing Pillow package
import os #importing os package
import math
import project_standard as ps
from tkinter import messagebox
import mysql.connector
import cv2




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
        self.root.title("Student Management System")   #setting title of the window

        #====================variables===========================
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_sec = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()

        self.var_option = StringVar()
        self.var_search_text = StringVar()
        

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

        dep_combo = ttk.Combobox(course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly")
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

        course_combo = ttk.Combobox(course_frame,textvariable=self.var_course,font=("times new roman",12,"bold"),state="readonly")
        course_combo["values"] = ("Select Course","Data mining","IR","Java")
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

        year_combo = ttk.Combobox(course_frame,textvariable=self.var_year,font=("times new roman",12,"bold"),state="readonly")
        year_combo["values"] = ("Select Year","2075","2076")
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

        sem_combo = ttk.Combobox(course_frame,textvariable=self.var_semester,font=("times new roman",12,"bold"),state="readonly")
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

        stu_id_entry = ttk.Entry(stuinfo_frame,textvariable=self.var_std_id,width=20,font=("times new roman",12,"bold"))
        stu_id_entry.grid(row=0,column=1,sticky=W)

        stu_name_label = Label(stuinfo_frame,text="Student Name : ",font=("times new roman",12,"bold"))
        stu_name_label.grid(row=0,column=2,sticky=EW)

        stu_name_entry = ttk.Entry(stuinfo_frame,textvariable=self.var_std_name,width=20,font=("times new roman",12,"bold"))
        stu_name_entry.grid(row=0,column=3,sticky=W)

        stu_section_label = Label(stuinfo_frame,text="Sections : ",font=("times new roman",12,"bold"))
        stu_section_label.grid(row=1,column=0,sticky=EW)

        stu_section_combo = ttk.Combobox(stuinfo_frame,textvariable=self.var_sec,font=("times new roman",12,"bold"),state="readonly")
        stu_section_combo["values"] = ("Select Section","A","B","C")
        stu_section_combo.current(0)
        stu_section_combo.grid(row=1,column=1,sticky=W)

        stu_roll_label = Label(stuinfo_frame,text="Roll No. : ",font=("times new roman",12,"bold"))
        stu_roll_label.grid(row=1,column=2,sticky=EW)

        stu_roll_entry = ttk.Entry(stuinfo_frame,textvariable=self.var_roll,width=20,font=("times new roman",12,"bold"))
        stu_roll_entry.grid(row=1,column=3,sticky=W)

        stu_gender_label = Label(stuinfo_frame,text="Gender : ",font=("times new roman",12,"bold"))
        stu_gender_label.grid(row=2,column=0)

        stu_gender_combo = ttk.Combobox(stuinfo_frame,textvariable=self.var_gender,font=("times new roman",12,"bold"),state="readonly")
        stu_gender_combo["values"] = ("Select Gender","Male","Female")
        stu_gender_combo.current(0)
        stu_gender_combo.grid(row=2,column=1,sticky=W)

        stu_dob_label = Label(stuinfo_frame,text="DOB : ",font=("times new roman",12,"bold"))
        stu_dob_label.grid(row=2,column=2,sticky=EW)

        stu_dob_entry = ttk.Entry(stuinfo_frame,textvariable=self.var_dob,width=20,font=("times new roman",12,"bold"))
        stu_dob_entry.grid(row=2,column=3,sticky=W)

        stu_email_label = Label(stuinfo_frame,text="Email : ",font=("times new roman",12,"bold"))
        stu_email_label.grid(row=3,column=0,sticky=EW)

        stu_email_entry = ttk.Entry(stuinfo_frame,textvariable=self.var_email,width=20,font=("times new roman",12,"bold"))
        stu_email_entry.grid(row=3,column=1,sticky=W)

        stu_phone_label = Label(stuinfo_frame,text="Phone : ",font=("times new roman",12,"bold"))
        stu_phone_label.grid(row=3,column=2,sticky=EW)

        stu_phone_entry = ttk.Entry(stuinfo_frame,textvariable=self.var_phone,width=20,font=("times new roman",12,"bold"))
        stu_phone_entry.grid(row=3,column=3,sticky=W)

        stu_address_label = Label(stuinfo_frame,text="Address : ",font=("times new roman",12,"bold"))
        stu_address_label.grid(row=4,column=0,sticky=EW)

        stu_address_entry = ttk.Entry(stuinfo_frame,textvariable=self.var_address,width=20,font=("times new roman",12,"bold"))
        stu_address_entry.grid(row=4,column=1,sticky=W)

        stu_teacher_label = Label(stuinfo_frame,text="Teacher Name : ",font=("times new roman",12,"bold"))
        stu_teacher_label.grid(row=4,column=2,sticky=EW)

        stu_teacher_entry = ttk.Entry(stuinfo_frame,textvariable=self.var_teacher,width=20,font=("times new roman",12,"bold"))
        stu_teacher_entry.grid(row=4,column=3,sticky=W)


        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(stuinfo_frame,variable=self.var_radio1,text="Take photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0,columnspan=2)

        
        radiobtn2 = ttk.Radiobutton(stuinfo_frame,variable=self.var_radio1,text="No photo Sample",value="No")
        radiobtn2.grid(row=5,column=2,columnspan=2)




       
        
        



        #Button section of left frame

        button_width = one_hundredth_left_frame_width*20
        button_height = one_hundredth_left_frame_height*9

        #button_1
        button1_img_path = IMG_DIR + "/save.png"
        button1 = Image.open(button1_img_path)
        button1 = button1.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button1 = ImageTk.PhotoImage(button1)

        button_label_1 = Button(left_frame,command=self.add_data,image=self.button1,cursor="hand2",bd=0)
        button1_xpos = one_hundredth_left_frame_width*12
        button1_ypos = one_hundredth_left_frame_height*92
        button_label_1.place(x=button1_xpos,y=button1_ypos,width=button_width,height=button_height)

        #button_2
        button2_img_path = IMG_DIR + "/update.png"
        button2 = Image.open(button2_img_path)
        button2 = button2.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button2 = ImageTk.PhotoImage(button2)

        button_label_2 = Button(left_frame,command=self.update_data,image=self.button2,cursor="hand2",bd=0)
        button2_xpos = one_hundredth_left_frame_width*42
        button2_ypos = one_hundredth_left_frame_height*92
        button_label_2.place(x=button2_xpos,y=button2_ypos,width=button_width,height=button_height)

        #button_3
        button3_img_path = IMG_DIR + "/delete.png"
        button3 = Image.open(button3_img_path)
        button3 = button3.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button3 = ImageTk.PhotoImage(button3)

        button_label_3 = Button(left_frame,command=self.delete_data,image=self.button3,cursor="hand2",bd=0)
        button3_xpos = one_hundredth_left_frame_width*72
        button3_ypos = one_hundredth_left_frame_height*92
        button_label_3.place(x=button3_xpos,y=button3_ypos,width=button_width,height=button_height)

        #button_4
        button4_img_path = IMG_DIR + "/reset.png"
        button4 = Image.open(button4_img_path)
        button4 = button4.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button4 = ImageTk.PhotoImage(button4)

        button_label_4 = Button(left_frame,command=self.reset_data,image=self.button4,cursor="hand2",bd=0)
        button4_xpos = one_hundredth_left_frame_width*12
        button4_ypos = one_hundredth_left_frame_height*102
        button_label_4.place(x=button4_xpos,y=button4_ypos,width=button_width,height=button_height)

        
        #button_5
        button5_img_path = IMG_DIR + "/addphotosample.png"
        button5 = Image.open(button5_img_path)
        button5 = button5.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button5 = ImageTk.PhotoImage(button5)

        button_label_5 = Button(left_frame,command=self.generate_dataset,image=self.button5,cursor="hand2",bd=0)
        button1_xpos = one_hundredth_left_frame_width*42
        button1_ypos = one_hundredth_left_frame_height*102
        button_label_5.place(x=button1_xpos,y=button1_ypos,width=button_width,height=button_height)

        #button_6
        button6_img_path = IMG_DIR + "/updatephotosample.png"
        button6 = Image.open(button6_img_path)
        button6 = button6.resize((button_width,button_height),Image.Resampling.LANCZOS)
        self.button6 = ImageTk.PhotoImage(button6)

        button_label_6 = Button(left_frame,command=self.update_dataset,image=self.button6,cursor="hand2",bd=0)
        button6_xpos = one_hundredth_left_frame_width*72
        button6_ypos = one_hundredth_left_frame_height*102
        button_label_6.place(x=button6_xpos,y=button6_ypos,width=button_width,height=button_height)







        # right label frame

        

        xpos_right_frame = self.one_hundredth_screen_width*52
        ypos_right_frame = self.one_hundredth_background_height*2
        right_frame_width = self.one_hundredth_screen_width*48
        right_frame_height = self.one_hundredth_background_height*98

        right_frame = LabelFrame(b_lbl,bd=5,relief=RIDGE,text="Search For Students",font=("times new roman",16,"bold"),bg=ps.theme_color)
        right_frame.place(x=xpos_right_frame,y=ypos_right_frame,width=right_frame_width,height=right_frame_height)
        right_frame.rowconfigure(index=0,weight=1)
        right_frame.rowconfigure(index=1,weight=9)
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
        search_combo = ttk.Combobox(right_frame,textvariable=self.var_option,font=("times new roman",12,"bold"),state="readonly")
        search_combo["values"] = ("Select Options","Roll No.","Student ID no.","Student name","Department","Year","Semester","Course")
        search_combo.current(0)
        search_combo.grid(row=0,column=1)

        #search entry field
        stu_search_entry = ttk.Entry(right_frame,textvariable=self.var_search_text,width=18,font=("times new roman",12,"bold"))
        stu_search_entry.grid(row=0,column=2)

        #Search button
        search_img_path = IMG_DIR + "/search.png"
        search_button = Image.open(search_img_path)
        search_button_height = one_hundredth_right_frame_height*5
        search_button_width = one_hundredth_right_frame_width*20
        search_button = search_button.resize((search_button_width,search_button_height),Image.Resampling.LANCZOS)
        self.search_button = ImageTk.PhotoImage(search_button)

        search_button_label = Button(right_frame,command=self.search,image=self.search_button,cursor="hand2",bd=0)
        search_button_label.grid(row=0,column=3)


        #Show all button
        show_img_path = IMG_DIR + "/showall.png"
        show_button = Image.open(show_img_path)
        show_button_height = one_hundredth_right_frame_height*5
        show_button_width = one_hundredth_right_frame_width*20
        show_button = show_button.resize((show_button_width,show_button_height),Image.Resampling.LANCZOS)
        self.show_button = ImageTk.PhotoImage(show_button)

        show_button_label = Button(right_frame,command=self.fetch_data,image=self.show_button,cursor="hand2",bd=0)
        show_button_label.grid(row=0,column=4)

        #search table frame
        search_table_frame_width = one_hundredth_right_frame_width*98
        search_table_frame_height = one_hundredth_right_frame_height*100
        search_table_frame = Frame(right_frame,bd=2,relief=RIDGE,width=search_table_frame_width,height=search_table_frame_height)
        search_table_frame.grid(row=1,column=0,columnspan=5,sticky=W+E+N+S)

        scroll_x = ttk.Scrollbar(search_table_frame,orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(search_table_frame,orient=VERTICAL)

        self.search_table = ttk.Treeview(search_table_frame,column=("Dep","Course","Year","Sem","ID","Name","Sec","Roll","Gender","DOB","Email","Phone","Address","Teacher","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.search_table.xview)
        scroll_y.config(command=self.search_table.yview)

        self.search_table.heading("Dep",text="Department")
        self.search_table.heading("Course",text="Course")
        self.search_table.heading("Year",text="Year")
        self.search_table.heading("Sem",text="Semester")
        self.search_table.heading("ID",text="StudentID")
        self.search_table.heading("Name",text="Name")
        self.search_table.heading("Sec",text="Section")
        self.search_table.heading("Roll",text="Roll No")
        self.search_table.heading("Gender",text="Gender")
        self.search_table.heading("DOB",text="D.O.B")
        self.search_table.heading("Email",text="Email")
        self.search_table.heading("Phone",text="Phone")
        self.search_table.heading("Address",text="Address")
        self.search_table.heading("Teacher",text="Teacher")
        self.search_table.heading("Photo",text="PhotoSampleStatus")
        self.search_table["show"] = "headings"

        self.search_table.column("Dep",width=100)
        self.search_table.column("Course",width=100)
        self.search_table.column("Year",width=100)
        self.search_table.column("Sem",width=100)
        self.search_table.column("ID",width=100)
        self.search_table.column("Name",width=100)
        self.search_table.column("Sec",width=100)
        self.search_table.column("Roll",width=100)
        self.search_table.column("Gender",width=100)
        self.search_table.column("DOB",width=100)
        self.search_table.column("Email",width=100)
        self.search_table.column("Phone",width=100)
        self.search_table.column("Address",width=100)
        self.search_table.column("Teacher",width=100)
        self.search_table.column("Photo",width=150)

        self.search_table.pack(fill=BOTH,expand=1)
        self.search_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()

    # ========================Function Declaration ===============================
    def add_data(self):

        if self.var_dep.get() ==  "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error","Department,Student Name or Student ID  fields are required",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost",username=ps.username,password=ps.password,database=ps.db)
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
                    self.var_sec.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get()
                ))
                conn.commit()
                self.fetch_data()
                if self.var_radio1.get() == "Yes" :
                    self.create_dataset()
                conn.close()
                messagebox.showinfo("Success","Data Entered Successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #================= fetch data ==========================
    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost",username=ps.username,password=ps.password,database=ps.db)
        my_cursor = conn.cursor()
        my_cursor.execute("select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.search_table.delete(*self.search_table.get_children())
            for i in data:
                self.search_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #====================== get data from the table on click of row to update ================
    def get_cursor(self,event=""):
        cursor_focus = self.search_table.focus()
        content = self.search_table.item(cursor_focus)
        data = content["values"]

        self.var_dep.set(data[0])
        self.var_course.set(data[1])
        self.var_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_sec.set(data[6])
        self.var_roll.set(data[7])
        self.var_gender.set(data[8])
        self.var_dob.set(data[9])
        self.var_email.set(data[10])
        self.var_phone.set(data[11])
        self.var_address.set(data[12])
        self.var_teacher.set(data[13])
        self.var_radio1.set(data[14])

    #======================= update function =============================
    def update_data(self):
        if self.var_dep.get() ==  "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error","Department,Student Name or Student ID  fields are required",parent=self.root)

        else:
            try:
                update = messagebox.askyesno("Update","Do you want to update this student details ?",parent=self.root)
                if update > 0 :
                    conn = mysql.connector.connect(host="localhost",username=ps.username,password=ps.password,database=ps.db)
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Sec=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_sec.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        self.var_radio1.get(),
                        self.var_std_id.get()

                    ))

                else:
                    if not update:
                        return

                messagebox.showinfo("Success","Students details updated successfully.",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    # =========================delete function ==========================================
    def delete_data(self):
        if self.var_std_id.get() == "" :
            messagebox.showerror("Error","Student id must be required",parent=self.root)

        else :
            try :
                delete = messagebox.askyesno("Delete","Do you want to delete the details of this student ?",parent=self.root)
                if delete > 0 :
                    conn = mysql.connector.connect(host="localhost",username=ps.username,password=ps.password,database=ps.db)
                    my_cursor = conn.cursor()
                    sql = "delete from student where ID=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql,val)

                else :
                    if not delete :
                        return

                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Successfully deleted",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #================== Reset function ==================================
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_sec.set("Select Section")
        self.var_roll.set("")
        self.var_gender.set("Select Gender")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")

    #========================= Generate data set or take a photo sample ======================
    def generate_dataset(self):
        if self.var_dep.get() ==  "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "" or self.var_radio1.get() == "Yes":
            messagebox.showerror("Error","Department,Student Name or Student ID  fields are required or No photo sample should be ticked",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost",username=ps.username,password=ps.password,database=ps.db)
                my_cursor = conn.cursor()
                
                
                id = self.var_std_id.get()
                

                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Sec=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_sec.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        "Yes",
                        self.var_std_id.get()

                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ============ load predefined model to detect face for capturing images of face ===============
                face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img) :
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_detector.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimum neighbor = 5

                    for (x,y,w,h) in faces :
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100 : # this is ENTER key code
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Added data set successfully !!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    # ============================== function for creating dataset during save ===================
    def create_dataset(self):
            try:
                
                
                
                id = self.var_std_id.get()
                

                
                
                # ============ load predefined model to detect face for capturing images of face ===============
                face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img) :
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_detector.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimum neighbor = 5

                    for (x,y,w,h) in faces :
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100 : # this is ENTER key code
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Created data set successfully !!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)

    #========================= Update data set or function for update photos button ======================
    def update_dataset(self):
        if self.var_dep.get() ==  "Select Department" or self.var_std_name.get() == "" or self.var_std_id.get() == "" or self.var_radio1.get() == "No":
            messagebox.showerror("Error","Department,Student Name or Student ID  fields are required or Take photo sample should be ticked",parent=self.root)

        else:
            try:
                conn = mysql.connector.connect(host="localhost",username=ps.username,password=ps.password,database=ps.db)
                my_cursor = conn.cursor()
                
                
                id = self.var_std_id.get()
                

                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Sem=%s,Name=%s,Sec=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,Photo=%s where ID=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_semester.get(),
                        self.var_std_name.get(),
                        self.var_sec.get(),
                        self.var_roll.get(),
                        self.var_gender.get(),
                        self.var_dob.get(),
                        self.var_email.get(),
                        self.var_phone.get(),
                        self.var_address.get(),
                        self.var_teacher.get(),
                        "Yes",
                        self.var_std_id.get()

                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ============ load predefined model to detect face for capturing images of face ===============
                face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img) :
                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces = face_detector.detectMultiScale(gray,1.3,5)
                    #scaling factor = 1.3
                    #minimum neighbor = 5

                    for (x,y,w,h) in faces :
                        face_cropped = img[y:y+h,x:x+w]
                        return face_cropped

                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret,my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id += 1
                        face = cv2.resize(face_cropped(my_frame),(450,450))
                        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path = "data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100 : # this is ENTER key code
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Updated data set successfully !!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to : {str(es)}",parent=self.root)


    # =============== function for search ===================================
    def search(self):
        option = self.var_option.get()
        #print(self.var_option.get())
        search_text = self.var_search_text.get()
        #print(self.var_search_text.get())
        if (option == "Select Options" and search_text == ""):
            messagebox.showerror("Error",f"Enter both fields",parent=self.root)
        elif (option != "Select Options" and search_text == ""):
            messagebox.showerror("Error",f"Enter second field",parent=self.root)
        elif (option == "Select Options" and search_text != ""):
            messagebox.showerror("Error",f"Enter first field",parent=self.root)
        else :
            conn = mysql.connector.connect(host="localhost",username=ps.username,password=ps.password,database=ps.db)
            my_cursor = conn.cursor()
            if (option == "Student ID no."):
                my_cursor.execute("select * from student where ID = " + search_text )
                data = my_cursor.fetchall()
            elif (option == "Roll No."):
                my_cursor.execute("select * from student where Roll = " + search_text )
                data = my_cursor.fetchall()
            elif (option == "Student name"):
                my_cursor.execute(f"select * from student where Name like '%{search_text}%'")
                data = my_cursor.fetchall()
            elif (option == "Department"):
                my_cursor.execute(f"select * from student where Dep like '%{search_text}%'")
                data = my_cursor.fetchall()
            elif (option == "Year"):
                my_cursor.execute("select * from student where Year = " + search_text )
                data = my_cursor.fetchall()
            
            elif (option == "Course"):
                my_cursor.execute(f"select * from student where Course like '%{search_text}%'")
                data = my_cursor.fetchall()
            elif (option == "Semester"):
                my_cursor.execute("select * from student where Sem = %s", [search_text] )
                data = my_cursor.fetchall()

            if len(data) != 0:
                self.search_table.delete(*self.search_table.get_children())
                for i in data:
                    self.search_table.insert("",END,values=i)
                conn.commit()
            else:
                messagebox.showerror("Error",f"No data found",parent=self.root)
                self.search_table.delete(*self.search_table.get_children())
            conn.close()




            


                
                    







            




            

        


        
        



if __name__ == "__main__":
    root = Tk()  #initializing tk object
    obj = Student(root)  #initializing Face_Recognition_System object
    root.mainloop()  #calling mainloop fuction of root class
