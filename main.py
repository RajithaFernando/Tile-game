import tkinter as tk

def create_window():
    
    import game2
    window = tk.Toplevel(root)
root = tk.Tk()
b = tk.Button(root, text="Create new window", command=create_window)
b.pack()

root.mainloop()