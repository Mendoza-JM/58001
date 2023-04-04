#Create a class DistanceConversion with attribute distance
#Create different methods to convert meter to centimeter, meter to kilometer, and meter to inch
#Use mangling for encapsulation
#The program will accept user input and by showing the three consecutive outputs
#(meter to centimeter, meter to kilometer, and meter to inch)

#centimeter = meter * 100
#kilometer = meter / 1000
#inches = meter *39.37

from tkinter import *
class MyWindow:
    def __init__(self,win):
        self.lbl1 = Label(win, text="Input Meters.")
        self.lbl1.place(x=100, y=50)
        self.lbl2 = Label(win, text="In centimeters:")
        self.lbl2.place(x=100, y=100)
        self.lbl3 = Label(win, text="In kilometers:")
        self.lbl3.place(x=100, y=150)
        self.lbl4 = Label(win, text="In Inches")
        self.lbl4.place(x=100, y=200)
        self.txt1 = Entry(win, bd=3)
        self.txt1.place(x=200, y=50)
        self.txt2 = Entry(win, bd=3)
        self.txt2.place(x=200, y=100)
        self.txt3 = Entry(win, bd=3)
        self.txt3.place(x=200, y=150)
        self.txt4 = Entry(win, bd=3)
        self.txt4.place(x=200, y=200)

        self.btnsolve = Button(win, text="Solve")
        self.btnsolve.place(x=100, y=300)
        self.btnsolve.bind('<Button-1>', self.__con__)

        self.btnclr = Button(win, text="Clear")
        self.btnclr.place(x=100, y=350)
        self.btnclr.bind('<Button-1>', self.clr)

    def __con__(self, con):
        self.txt2.delete(0, 'end')
        meter = int(self.txt1.get())
        result = meter * 100
        self.txt2.insert(END, str(result))
        self.txt3.delete(0, 'end')
        meter = int(self.txt1.get())
        result = meter / 100
        self.txt3.insert(END, str(result))
        self.txt4.delete(0, 'end')
        meter = int(self.txt1.get())
        result = meter * 38.37
        self.txt4.insert(END, str(result))

    def clr(self,clr):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')
        self.txt4.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.geometry("600x400+10+10")
window.title("Meter Converter")
window.mainloop()
