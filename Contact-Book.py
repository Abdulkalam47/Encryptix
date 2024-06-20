from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry('700x550')
root.config(bg = '#d3f3f5')
root.title('PythonGeeks Contact Book')
root.resizable(0, 0)

contactlist = []

Name = StringVar()
Number = StringVar()
Email = StringVar()

frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, font=('Times new roman', 16), bg="#f0fffc", width=20, height=20, borderwidth=3, relief="groove")
scroll.config(command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT, fill=BOTH, expand=1)

def Selected():
    if len(select.curselection()) == 0:
        messagebox.showerror("Error", "Please Select the Name")
        return None
    else:
        return int(select.curselection()[0])

def AddContact():
    if Name.get() and Number.get() and Email.get():
        contactlist.append([Name.get(), Number.get(), Email.get()])
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmation", "Successfully Added New Contact")
    else:
        messagebox.showerror("Error", "Please fill all the information")

def UpdateDetail():
    if Selected() is not None:
        if Name.get() and Number.get() and Email.get():
            contactlist[Selected()] = [Name.get(), Number.get(), Email.get()]
            messagebox.showinfo("Confirmation", "Successfully Updated Contact")
            EntryReset()
            Select_set()
        else:
            messagebox.showerror("Error", "Please fill all the information")
    else:
        messagebox.showerror("Error", "Please Select the Name and press Load button")

def EntryReset():
    Name.set('')
    Number.set('')
    Email.set('')

def Delete_Entry():
    if Selected() is not None:
        result = messagebox.askyesno('Confirmation', 'Do you want to delete the selected contact?')
        if result:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')

def VIEW():
    if Selected() is not None:
        NAME, PHONE, EMAIL = contactlist[Selected()]
        Name.set(NAME)
        Number.set(PHONE)
        Email.set(EMAIL)

def EXIT():
    root.destroy()

def Select_set():
    contactlist.sort()
    select.delete(0, END)
    for name, phone, email in contactlist:
        select.insert(END, name)

Select_set()

Label(root, text='Name', font=("Times new roman", 25, "bold"), bg='SlateGray3').place(x=30, y=20)
Entry(root, textvariable=Name, width=30).place(x=200, y=30)
Label(root, text='Contact No.', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=70)
Entry(root, textvariable=Number, width=30).place(x=200, y=80)
Label(root, text='Email', font=("Times new roman", 22, "bold"), bg='SlateGray3').place(x=30, y=120)
Entry(root, textvariable=Email, width=30).place(x=200, y=130)

button_frame = Frame(root, bg='#d3f3f5')
button_frame.place(x=50, y=200)

Button(button_frame, text="ADD", font='Helvetica 18 bold', bg='#e8c1c7', command=AddContact, padx=20).grid(row=0, column=0)
Button(button_frame, text="EDIT", font='Helvetica 18 bold', bg='#e8c1c7', command=UpdateDetail, padx=20).grid(row=0, column=1)
Button(button_frame, text="DELETE", font='Helvetica 18 bold', bg='#e8c1c7', command=Delete_Entry, padx=20).grid(row=1, column=1,padx=10, pady=10)
Button(button_frame, text="VIEW", font='Helvetica 18 bold', bg='#e8c1c7', command=VIEW).grid(row=0, column=2)
Button(button_frame, text="RESET", font='Helvetica 18 bold', bg='#e8c1c7', command=EntryReset).grid(row=1, column=0,padx=10, pady=10)
Button(button_frame, text="EXIT", font='Helvetica 24 bold', bg='tomato', command=EXIT).grid(row=3, column=1)

root.mainloop()
