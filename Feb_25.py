##File Operations

##file_obj = open("netzwerk.txt","w")  Open file
##file_obj.write("hello in the form")  Write in a file
##file_obj.close()                     Close the file

##file_obj = open("devi.txt", "w")
##file_obj.write("hello")
##file_obj.close()

##file_obj = open("C:\Users\gunja\OneDrive\Desktop\Python\devi.txt", "w")
##file_obj.write("hello")
##file_obj.close()

import tkinter #GUI, Forms, Frames, Buttons, Labels
from tkinter import filedialog
import os

root = tkinter.Tk()
root.withdraw()
folder = filedialog.askdirectory()
print(folder)

file = os.path.join(folder,"devi.txt")
file_obj = open(file, "a")
file_obj.write("\n")
file_obj.write("india")
file_obj.close()

#Context manager

##with open("netzwerk.txt","r") as file_obj:
##    file_content = file_obj.read(5)
##    print(file_content)
##    file_content1 = file_obj.read()
##    print(file_content1)
##
##with open("netzwerk.txt","r") as file_obj:
##    file_content = file_obj.readline()
##    print(file_content)
##    file_content1 = file_obj.readline()
##    print(file_content1)

##with open("netzwerk.txt","r") as file_obj:
##    file_content = file_obj.readlines()
##    print(file_content)

##with open("netzwerk.txt","w+") as file_obj:
##    file_obj.write("welcome to india")
##    file_obj.seek(0)
##    file_content = file_obj.read()
##    print(file_content)

##with open("netzwerk.txt","a+") as file_obj:
##    file_obj.write("welcome to india")
##    file_obj.seek(0)
##    file_content = file_obj.read()
##    print(file_content)

##with open("netzwerk.txt","r+") as file_obj:
##    file_content = file_obj.read()
##    print(file_content)
##    file_obj.write("welcome to india")
##

with open("netzwerk1.txt","x") as file_obj:
    file_obj.write("welcome to india")
