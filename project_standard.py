from tkinter import*
from tkinter import ttk
import math

theme_color = "#dde6e9"

root = Tk()
root.mainloop

# layout size definition

#screen section
screen_width = root.winfo_screenwidth() #get the screen width
screen_width_str = str(screen_width) #get the screen width in string
screen_height = root.winfo_screenheight()-60 #get the screen height and we subtract 70 to eliminate the height of taskbar
screen_height_str = str(screen_height) #get the screen height in string

one_tenth_screen_height = math.floor(screen_height/10)  #1/10 of screen height
one_tenth_screen_width = math.floor(screen_width/10)   #1/10 of screen weidth
one_hundredth_screen_width = math.floor(screen_width/100)     #1/100 of screen width


#header section
header_width = screen_width
header_height = one_tenth_screen_height*2

#body section
background_width = screen_width
background_height = one_tenth_screen_height*8
one_hundredth_background_height = math.floor(background_height/100)


# button section of main.py
button_width = int(one_tenth_screen_width*2)
button_height = int((background_height/11))

# button1


#left frame student.py
xpos_left_frame = one_hundredth_screen_width*2
ypos_left_frame = one_hundredth_background_height*2
left_frame_width = one_hundredth_screen_width*48
left_frame_height = one_hundredth_background_height*98

one_hundredth_left_frame_width = math.floor(left_frame_width/100)
one_hundredth_left_frame_height = math.floor(left_frame_height/100)

#course frame student.py
course_frame_width = one_hundredth_left_frame_width*98
course_frame_height = one_hundredth_left_frame_height*30
xpos_course_frame = one_hundredth_left_frame_width*2
ypos_course_frame = one_hundredth_left_frame_height*20


#right frame student.py
xpos_right_frame = one_hundredth_screen_width*52
ypos_right_frame = one_hundredth_background_height*2
right_frame_width = one_hundredth_screen_width*48
right_frame_height = one_hundredth_background_height*98

one_hundredth_right_frame_width = math.floor(right_frame_width/100)
one_hundredth_right_frame_height = math.floor(right_frame_height/100)








