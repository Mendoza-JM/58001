from tkinter import *
window = Tk()

window.geometry("500x400+10+10")
window.title("My First GUI")
btn1 = Button(window, text="Click me", fg="red", bg="yellow")
btn1.place(x=200, y=200)

txtfld = Entry(window, border=2.50)
txtfld.place(x=180, y=150)

lbl = Label(window, text="My First Demo", font="Verdana")
lbl.place(x=180,y=50)

window.mainloop()