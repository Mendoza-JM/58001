#Construct a GUI and create the Python programs (using Pycharm/ Tkinter module in creating widgets) that allow you to type in your Given Name, Middle Name, and Last Name inside the three consecutive Entry widgets and display the full name inside the last Entry widget by clicking "Show Full Name" button. (Note: The output window must be exactly the same as below image)
from tkinter import *
class MyWindow:
    def __init__(self,win):
        self.lbl0 = Label(win,text="My Full name")
        self.lbl0.place(x=250, y=10)
        self.lbl1 = Label(win,text="Enter Given Name:")
        self.lbl1.place(x=100,y=50)
        self.lbl2 = Label(win, text="Enter Middle Name:")
        self.lbl2.place(x=100,y=100)
        self.lbl3 = Label(win, text="Enter Last Name:")
        self.lbl3.place(x=100,y=150)
        self.lbl4 = Label(win, text="My Full Name is:")
        self.lbl4.place(x=100, y=225)
        self.txt1 = Entry(win,bd=1)
        self.txt1.place(x=325,y=50)
        self.txt2 = Entry(win,bd=1)
        self.txt2.place(x=325,y=100)
        self.txt3 = Entry(win,bd=3)
        self.txt3.place(x=325,y=150)
        self.txt4 = Entry(win, bd=3)
        self.txt4.place(x=325, y=225)
        self.btn = Button(win, text="Show Full Name")
        self.btn.place(x=250, y=300)
        self.btn.bind('<Button-1>', self.show)

    def show(self,show):
        self.txt4.delete(0, 'end')
        first = str(self.txt1.get())
        middle = str(self.txt2.get())
        last = str(self.txt3.get())
        Fullname = first + ' ' + middle + ' ' +last
        self.txt4.insert(END,str(Fullname))



window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Simple Calculator")
window.mainloop()







