from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from tkinter.filedialog import *

mainWin=Tk()
mainWin.title('Address Book')

myAddressBook={}

def clear_all():
    name.delete(0,END)
    address.delete(0,END)
    mobile.delete(0,END)
    email.delete(0,END)
    birthday.delete(0,END)

def update():
    key=name.get()
    if key=="":
        messagebox.showinfo("Error", "Name cannot be empty")
    else:
        if key not in myAddressBook.keys()
