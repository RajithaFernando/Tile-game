from tkinter import *

class Window(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)                 
        self.master = master
        self.init_window()

    #Creation of init_window
    def init_window(self):

        # changing the title of our master widget      
        self.master.title("Tile Game")

        # allowing the widget to take the full space of the root window
        self.pack(fill=BOTH, expand=1)

        # creating a button instance
        # placing the button on my window

        tile = Button(self, text="Quit", height = 5, width = 10)
        tile.pack(side=LEFT)

        tile2 = Button(self, text="Quit2")
        tile2.place(x=10, y=10)
        

        # Button(self.root, text = "Brighten").grid(row=2, column=0)
        # Button(self.root, text = "Darken").grid(row=2, column=1)
        # Button(self.root, text = "Warm").grid(row=2, column=2)
        # Button(self.root, text = "Cool").grid(row=2, column=3)
root = Tk()
# f = Frame(win)
# b1 = Button(f, "One")
# b2 = Button(f, "Two")
# b3 = Button(f, "Three")
# b1.pack(side=LEFT)
# b2.pack(side=LEFT)
# b3.pack(side=LEFT)
# l = Label(win, text="This label is over all buttons")
# l.pack()
# f.pack()

#size of the window
root.geometry("600x400")

app = Window(root)
root.mainloop()  