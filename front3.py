from tkinter import * 
win = Tk()
f = Frame(win)
b1 = Button(f, "One")
b2 = Button(f, "Two")
b3 = Button(f, "Three")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(win, text="This label is over all buttons")
l.pack()
f.pack()