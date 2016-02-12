#without loop

from tkinter import * # Import tkinter
    
class MainGUI:
    def __init__(self):
        window = Tk() # Create a window
        window.title("tic-tac-toe") # Set title
        
        
        
        self.canvas = Canvas(window, width = 200, height = 200, bg = "white")
        self.canvas.pack()
        
        frame = Frame(window)
        frame.pack()
   
       # self.canvas.create_line(10, 10, 190, 10, fill = "red")
        self.canvas.create_line(10, 30, 190, 30, fill = "red")
        self.canvas.create_line(10, 50, 190, 50, fill = "red")
        self.canvas.create_line(10, 70, 190, 70, fill = "red")
        self.canvas.create_line(10, 90, 190, 90, fill = "red")
        self.canvas.create_line(10, 110, 190, 110, fill = "red")
        self.canvas.create_line(10, 130, 190, 130, fill = "red")
        self.canvas.create_line(10, 150, 190, 150, fill = "red")
        self.canvas.create_line(10, 170, 190, 170, fill = "red")
        

        self.canvas.create_line(30, 10, 30, 190, fill = "blue")
        self.canvas.create_line(50, 10, 50, 190, fill = "blue")
        self.canvas.create_line(70, 10, 70, 190, fill = "blue")
        self.canvas.create_line(90, 10, 90, 190, fill = "blue")
        self.canvas.create_line(110, 10, 110, 190, fill = "blue")
        self.canvas.create_line(130, 10, 130, 190, fill = "blue")
        self.canvas.create_line(150, 10, 150, 190, fill = "blue")
        self.canvas.create_line(170, 10, 170, 190, fill = "blue")
        
        #self.canvas.create_line(10, 10, 190, 10, fill = "blue")
    
        
           
MainGUI() # Create GUI 


