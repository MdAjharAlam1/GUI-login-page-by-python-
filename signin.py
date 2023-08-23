#import tkinter module
from tkinter import *
# form pillow add image in tkinter jpg image 
from PIL import ImageTk
# functionality part 

# these function is used to when click on password eye button then show the password and again click on close eye hide the password 
def hide():
    open_eye.config(file="closeye.png")
    password_Entry.config(show="*")
    eye_button.config(command=show)

def show():
    open_eye.config(file="openeye.png")
    password_Entry.config(show='')
    eye_button.config(command=hide)




# this function is used to when click on username then delter username text 
def user_enter(event):
    if username_Entry.get()=="username":
        username_Entry.delete(0,END)

def password_enter(event):
    if password_Entry.get()=="Password":
        password_Entry.delete(0,END)



# GUI part
login_window =Tk()
login_window.geometry("990x660+50+50")
# cannot resize the width and height of tkinter
login_window.resizable(False,False)
# title of tkinter 
login_window.title("Login Page ")
# set background_image 
background_image = ImageTk.PhotoImage(file='bg.jpg')
# set background_image label 
background_image_label = Label(login_window,image=background_image)
# In grid  or pack no need to set dimension or gemotery of tkinter
# always taking automatic width and height by the size of image 
# background_image_label.grid(row=0,column=0)
# background_image_label.pack()
background_image_label.place(x=0 ,y=0)
# create heading 
# bg :- background color of text 
# fg :- font color of text 
heading =Label(login_window, text="USER LOGIN",font=("poppins",18,"bold"),bg="white",fg="red")
# set position 
heading.place(x=605,y=120)
# bd:- border 
# make input 
username_Entry = Entry(login_window,width=30,font=("poppins",12,"bold"),bd=0,fg="red")
username_Entry.place(x=580,y=200)
username_Entry.insert(0,"username")
# <FocusIN> :- click on usrename input
username_Entry.bind("<FocusIn>",user_enter)

frame_1 = Frame(login_window,width=250, height=2,bg="red")
frame_1.place(x=580, y=222)

password_Entry = Entry(login_window,width=30,font=("poppins",12,"bold"),bd=0,fg="red")
password_Entry.place(x=580,y=260)
password_Entry.insert(0,"Password")
# <FocusIN> :- click on usrename input
password_Entry.bind("<FocusIn>",password_enter)

frame_2 = Frame(login_window,width=250, height=2,bg="red")
frame_2.place(x=580, y=282)
#set eye image on password
open_eye = PhotoImage(file="openeye.png")
eye_button = Button(login_window,image=open_eye,bd=0,bg="white",activebackground="white",cursor="hand2",command=hide)
eye_button.place(x=800,y=255)

# create forget button 
forget_button = Button(login_window,text="Forget Password?",bd=0,bg="white",activebackground="white",cursor="hand2",font=("poppins",11,"bold"),fg="red",activeforeground="red")
forget_button.place(x=700,y=295)

# create login button 
login_button = Button(login_window,text="Login",bg="firebrick1",activebackground="white" ,cursor="hand2",font=("poppins",16,"bold"),bd=0 ,fg="white", width=19)
login_button.place(x=578,y=350)

# create OR label
orlabel = Label(login_window,text="-------------- OR --------------",font=("poppins",16),fg="firebrick1",bg="white")
orlabel.place(x=583,y=400)

# add image facebook 
facebook_logo = PhotoImage(file="facebook.png")
facebook_label= Label(login_window,image=facebook_logo,bg="white")
facebook_label.place(x=640,y=440)

# add image google
google_logo = PhotoImage(file="google.png")
google_label= Label(login_window,image=google_logo,bg="white")
google_label.place(x=690,y=440)

# add image google
twitter_logo = PhotoImage(file="twitter.png")
twitter_label= Label(login_window,image=twitter_logo,bg="white")
twitter_label.place(x=740,y=440)

# create forget button 
sinuplabel = Label(login_window,text="Don't have an account",bd=0,bg="white",activebackground="white",cursor="hand2",font=("open Sans",9,"bold"),fg="red",activeforeground="red")
sinuplabel.place(x=590,y=500)

# create new account button 
newaccount_button = Button(login_window,text="Create new acount",bg="white",activebackground="white" ,cursor="hand2",font=("open Sans",9,"bold underline"),bd=0 ,fg="blue" ,activeforeground="blue")
newaccount_button.place(x=727,y=500)







login_window.mainloop()
