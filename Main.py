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
        if key not in myAddressBook.keys():
            book_list.insert(END,key)
        myAddressBook[key]=(address.get(),mobile.get(),email.get(),birthday.get())
        clear_all()

def edit():
    clear_all()
    index = book_list.curselection()
    if index:
        name.insert(0,book_list.get(index))
        details=myAddressBook[name.get()]
        address.insert(0,details[0])
        mobile.insert(0,details[1])
        email.insert(0,details[2])
        birthday.insert(0,details[3])
    else:
        messagebox.showinfo("Error", "Select a name.")

def delete():
    index = book_list.curselection()
    if index:
        del myAddressBook[book_list.get(index)]
        book_list.delete(index)
        clear_all()
    else:
        messagebox.showinfo("Error", "Select a name.")

def display(event):
    newWindow = Toplevel(mainWin)
    index = book_list.curselection()
    contact=""
    if index:
        key=book_list.get(index)
        contact= "NAME     : "+key+"\n\n"
        details=myAddressBook[key]
        contact+="ADDRESS  : "+details[0]+"\n"
        contact+="MOBILE   : "+details[1]+"\n"
        contact+="E-MAIL   : "+details[2]+"\n"
        contact+="BIRTHDAY : "+details[3]+"\n"

    lbl=label(newWindow)
    lbl.grid(row=0,column=0)
    lbl.configure(text=contact)

def reset():
    clear_all()
    book_list.delete(0,END)
    myAddressBook.clear()
    bookName.configure(text='My Address Book')

def save():
    fout=asksaveasfile(defaultextention=".txt")
    if fout:
        print(myAddressBook,file=fout)
        reset()
    else:
        messagebox.showinfo("Warning", "Address Book not saved")

def openFile():
    global myAddressBook
    reset()
    fin=askopenfile(title='Open File')
    if fin:
        myAddressBook=eval(fin.read())
        for key in myAddressBook.keys():
            book_list.insert(END,key)
        bookName.configure(text=os.path.basename(fin.name))
    else:
        messagebox.showinfo("Warning", "No address book opened.")

bookName = Label(mainWin, text='My Address Book',width=35)
bookName.grid(row = 0, column = 1,pady = 10,columnspan=3)

open_button = Button(mainWin, text='Open',command=openFile)
open_button.grid(row = 0, column = 3,pady = 10)

book_list =Listbox(mainWin,height=15,width=30)
book_list.grid(row= 2, column = 0,columnspan=3, rowspan = 5)
booklist.bind('<<ListboxSelect>>',display)

name_label =Label(mainWin, text = 'Name:')¢›
