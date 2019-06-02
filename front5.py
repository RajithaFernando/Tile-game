import tkinter as tk

root = tk.Tk()

canvas = tk.Canvas(root, background="white")
button_frame = tk.Frame(root)

button_frame.pack(side="bottom", fill="x", expand=False)
canvas.pack(side="top", fill="both", expand=True)

# <button code will be added here...>


root.geometry("600x400")
root.mainloop()