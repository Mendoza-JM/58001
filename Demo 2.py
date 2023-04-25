from tkinter import *
win = Tk()

win.geometry("400x200+10+10")
win.title("Grid Manager")

#put your widget here

txt1 = Entry(win, bd=2)
txt1.grid(row=0, column=0)
txt1.insert(0, "row 0"+" "+" "+"column 0")

txt2 = Entry(win, bd=2,)
txt2.grid(row=0, column=1)
txt2.insert(0, "row 0"+" "+" "+"column 1")

txt3 = Entry(win, bd=2,)
txt3.grid(row=0, column=2)
txt3.insert(0, "row 0"+" "+" "+"column 2")

txt4 = Entry(win, bd=2)
txt4.grid(row=2, column=0)
txt4.insert(0, "row 2"+" "+" "+"column 0")

txt5 = Entry(win, bd=2)
txt5.grid(row=2, column=1)
txt5.insert(0, "row 2"+" "+" "+"column 1")

txt6 = Entry(win, bd=2,)
txt6.grid(row=2, column=2)
txt6.insert(0, "row 2"+" "+" "+"column 2")

txt6 = Entry(win, bd=2,)
txt6.grid(row=3, column=0)
txt6.insert(0, "row 3"+" "+" "+"column 0")

txt7 = Entry(win, bd=2,)
txt7.grid(row=3, column=1)
txt7.insert(0, "row 3"+" "+" "+"column 1")

txt8 = Entry(win, bd=2,)
txt8.grid(row=3, column=2)
txt8.insert(0, "row 3"+" "+" "+"column 2")

txt9 = Entry(win, bd=2,)
txt9.grid(row=4, column=0)
txt9.insert(0, "row 4"+" "+" "+"column 0")

txt10 = Entry(win, bd=2,)
txt10.grid(row=4, column=1)
txt10.insert(0, "row 4"+" "+" "+"column 1")

txt10 = Entry(win, bd=2,)
txt10.grid(row=4, column=2)
txt10.insert(0, "row 4"+" "+" "+"column 2")
win.mainloop()