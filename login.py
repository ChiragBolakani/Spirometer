from tkinter import *
import csv
from tkinter.ttk import Progressbar
import numpy as np
import os
import sys
# import readSpo2
import threading

#Creating object 'root' of Tk()
root = Tk()

#Providing Geometry to the form
root.geometry("500x500")

root.configure(background = 'lightblue')

#Providing title to the form
root.title('Registration form')


def progress():
    # pb1.pack()
    for i in range(11):
        if(i == 10):
            pb1.place_forget()
            break
        pb1["value"] += 10
        root.after(1000)


def startSpo2():
    threading.Thread(target=progress).start()
    threading.Thread(target=readSpo2.startSpo2).start()

def saveData():
    names = ["Name", "Age", "Height", "Gender"]
    gender = ""
    name = entry_1.get()
    age = entry_3.get()
    height = entry_height.get()
    genderInt = var.get()

    if(genderInt==1):
        gender = "male"
    if(genderInt==2):
        gender="female"

    values = [name, age, height, gender]
    print(name)
    print(age)
    print(height)
    print(gender)
    with open('userData.csv', 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(names)

        # write the data
        writer.writerow(values)

        f.close()

        # os.system("python main.py")
        sys.exit()

#this creates 'Label' widget for Registration Form and uses place() method.
label_0 =Label(root,text="Patient Details", width=20,font=("bold",20), background = 'lightblue')
#place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
label_0.place(x=90,y=60)

#this creates 'Label' widget for Fullname and uses place() method.
label_1 =Label(root,text="Full Name", width=20,font=("bold",10), background = 'lightblue')
label_1.place(x=80,y=130)

#this will accept the input string text from the user.
entry_1=Entry(root)
entry_1.place(x=240,y=130)

#this creates 'Label' widget for Email and uses place() method.
label_3 =Label(root,text="Age", width=20,font=("bold",10), background = 'lightblue')
label_3.place(x=68,y=180)

entry_3=Entry(root)
entry_3.place(x=240,y=180)

#this creates 'Label' widget for Gender and uses place() method.
label_4 =Label(root,text="Gender", width=20,font=("bold",10),background = 'lightblue')
label_4.place(x=70,y=230)

label_height =Label(root,text="Height (in cm)", width=20,font=("bold",10), background = 'lightblue')
label_height.place(x=70,y=280)

entry_height=Entry(root)
entry_height.place(x=240,y=280)

#the variable 'var' mentioned here holds Integer Value, by deault 0
var=IntVar()

#this creates 'Radio button' widget and uses place() method
Radiobutton(root,text="Male",padx= 5, variable= var, value=1, background = 'lightblue').place(x=235,y=230)
Radiobutton(root,text="Female",padx= 20, variable= var, value=2,background = 'lightblue').place(x=290,y=230)

#this creates button for submitting the details provides by the user
Button(root, text='Read Spo2' , width=20,bg="black",fg='white', command=startSpo2).place(x=180,y=340)

pb1 = Progressbar(root, orient=HORIZONTAL, length=100, mode='determinate')
pb1.place(x=200,y=370)

Button(root, text='Save and Exit' , width=20,bg="black",fg='white', command=saveData).place(x=180,y=430)


#this will run the mainloop.
root.mainloop()