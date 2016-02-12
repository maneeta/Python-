from tkinter import * # Import tkinter
    
class RadioAndCheckbutton:
    def __init__(self):
        window = Tk() # Create a window
        window.title("Radio and Checkbutton") # Set title
        
        # Place self.canvas in the window
        self.canvas = Canvas(window, width = 200, height = 100, 
            bg = "white")
        self.canvas.pack()
        
        # Add a check button, and radio button to frame1
        frame1 = Frame(window) # Create and add a frame to window
        frame1.pack()
       
        self.v1 = IntVar()
        cbtFill = Checkbutton(frame1, text = "Filled", variable = self.v1, command = self.optionChanged) 
            
        self.v2 = IntVar()
        rbRect = Radiobutton(frame1, text = "Rectangle", bg = "white", variable = self.v2, value = 1,  command =  self.optionChanged)
                 
                
        rbOval = Radiobutton(frame1, text = "Oval", bg = "white", variable = self.v2, value = 2, command =  self.optionChanged)
                 
               
        cbtFill.grid(row = 1, column = 3)
        rbRect.grid(row = 1, column = 1)
        rbOval.grid(row = 1, column = 2)

        self.v1.set(0) 
    
        window.mainloop() # Create an event loop

    # Fill the color
    def optionChanged(self):
        self.canvas.delete("rect", "oval")
        #color = "white" if self.v1.get() == "0" else "red"
        if self.v1.get() != 0:
            if self.v2.get() == 1:
                self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect", fill = "red")
            elif self.v2.get() == 2:
                self.canvas.create_oval(10, 10, 190, 90, tags = "oval", fill = "green")
        elif self.v1.get() == 0:
            if self.v2.get() == 1:
                self.canvas.create_rectangle(10, 10, 190, 90, tags = "rect", fill = "white")
            elif self.v2.get() == 2:
                self.canvas.create_oval(10, 10, 190, 90, tags = "oval", fill = "white")
        
        
    
RadioAndCheckbutton() # Create GUI 


