import tkinter as tk

win = tk.Tk()
canvas = tk.Canvas(win)
canvas.pack()

canvas.create_rectangle(50, 50, 100, 150, fill="red", tag="one")
canvas.delete("one")

win.mainloop()