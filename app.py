from tkinter import  *
import random
import tkinter

window = Tk()
window.title("Password Generator App") #Window Title
window.geometry('500x500')  #Window Size

Label(window, font=('bold', 10), text='PASSWORD GENERATOR').pack()    #Giving Label to Window

password_label = Label(window, text = '', font = ('bold', 20)) #displaying password
password_label.place(x=190, y=25)

def password_generator(leng):
    valid_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_' #characters of password

    password = ''.join(random.sample(valid_char, leng)) #generating random password
    password_label.config(text=password)    # Update the label to display the generated password and to prevent overlaps
    

password_length = tkinter.IntVar(value=6)

Radiobutton(window, text='4 Characters', variable=password_length, value=4).place(x=200, y=150)
Radiobutton(window, text='6 Characters', variable=password_length, value=6).place(x=200, y=170)
Radiobutton(window, text='8 Characters', variable=password_length, value=8).place(x=200, y=190)
Radiobutton(window, text='12 Characters', variable=password_length, value=12).place(x=200, y=210)
Radiobutton(window, text='16 Characters', variable=password_length, value=16).place(x=200, y=230)

def generate_password():
    length = password_length.get()
    password_generator(length)

Button(window, text="Generate", font=('normal', 10), bg = 'yellow', command=generate_password).place(x=200, y=100)

window.mainloop()   #run the window