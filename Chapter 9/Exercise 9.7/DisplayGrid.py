#used loops

import tkinter

root = tkinter.Tk()
root.title("Display a Grid")
canvas = tkinter.Canvas(root)
canvas.pack()

for i in range(8):
    canvas.create_line(50 * i, 0, 50 * i, 400, fill = "red") 
    canvas.create_line(0, 50 * i, 400, 50 * i, fill = "blue")

root.mainloop()
