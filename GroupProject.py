import tkinter as tk

class MyGUI:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Boy Buying Flowers")

        self.canvas = tk.Canvas(self.main_window, width=380, height=320)
        self.canvas.pack()

        self.current_picture_index = 0 
        self.pictures = [self.maryam_picture1, self.zarmina_picture2, self.eshaal_picture3]

        #button 
        self.next_button = tk.Button(self.main_window, text="Next", command=self.next_picture)
        self.next_button.pack()


        tk.mainloop()

    def next_picture(self):
        #clean canvas
        self.canvas.delete("all")

        #next picture
        self.current_picture_index = (self.current_picture_index + 1) % len(self.pictures)
        self.pictures[self.current_picture_index]()

    def maryam_picture1(self):
        # Car
        self.canvas.create_polygon(60, 135, 90, 100, 210, 100, 240, 135, fill = "cyan")
        self.canvas.create_rectangle(30, 135, 275, 180, width = 0, fill = "yellow")
        self.canvas.create_rectangle(123, 100, 160, 135, width = 0, fill = "yellow")
        self.canvas.create_rectangle(80, 95, 210, 100, width = 0, fill = "yellow")
        self.canvas.create_line(60, 135, 90, 97, width = 5, fill = "yellow")
        self.canvas.create_line(160, 145, 175, 145, width = 5, fill = "grey")
        self.canvas.create_rectangle(263, 140, 275, 150, width = 0, fill = "orange")
        self.canvas.create_rectangle(30, 140, 42, 150, width = 0, fill = "orange")
        self.canvas.create_oval(60, 170, 100, 210, width = 0, fill = "black")
        self.canvas.create_oval(67, 177, 93, 203,width = 0, fill = "grey")
        self.canvas.create_oval(200, 170, 240, 210, width = 0, fill = "black")
        self.canvas.create_oval(207, 177, 233, 203, width = 0, fill = "grey")

        # Boy
        self.canvas.create_line(340, 100, 340, 180, width = 2, fill = "blue")
        self.canvas.create_line(340, 180, 315, 225, width = 2, fill = "blue")
        self.canvas.create_line(340, 180, 365, 225, width = 2, fill = "blue")
        self.canvas.create_line(340, 130, 315, 160, width = 2, fill = "blue")
        self.canvas.create_line(340, 130, 365, 160, width = 2, fill = "blue")
        self.canvas.create_oval(316, 80, 364, 128, fill= "purple" )


    def zarmina_picture2(self):
        # Draw a simple store
        self.canvas.create_rectangle(300, 150, 350, 250, fill="brown")
        self.canvas.create_polygon(300, 150, 325, 100, 350, 150, fill="red")

        # Draw a car
        self.canvas.create_rectangle(50, 180, 100, 220, fill="yellow")
        self.canvas.create_oval(60, 220, 70, 230, fill="black")
        self.canvas.create_oval(80, 220, 90, 230, fill="black")

        # Draw a stick figure (the boy) in the car
        self.canvas.create_oval(72, 160, 82, 170, fill="purple")
        self.canvas.create_line(77, 170, 77, 190, fill="blue")
        self.canvas.create_line(67, 180, 87, 180, fill="blue")
        self.canvas.create_line(77, 190, 72, 200, fill="blue")
        self.canvas.create_line(77, 190, 82, 200, fill="blue")

    def eshaal_picture3(self):
        #boy
        self.canvas.create_oval(50, 150, 100, 200, fill="purple")
        self.canvas.create_line(75, 200, 75, 250, fill="blue")
        self.canvas.create_line(75, 250, 50, 300, fill="blue")
        self.canvas.create_line(75, 250, 100, 300, fill="blue")
        self.canvas.create_line(75, 210, 50, 225, fill="blue")
        self.canvas.create_line(75, 210, 100, 225, fill="blue")

        #flower
        self.canvas.create_oval(80, 180, 100, 200, fill="pink")
        self.canvas.create_oval(90, 170, 110, 190, fill="pink")
        self.canvas.create_oval(100, 180, 120, 200, fill="pink")  
        self.canvas.create_oval(90, 190, 110, 210, fill="pink")

        self.canvas.create_oval(95, 185, 105, 195, fill="yellow")

        self.canvas.create_line(90, 200, 90, 230, fill="green")

        self.canvas.create_rectangle(300, 150, 350, 250, fill="brown")
        self.canvas.create_polygon(300, 150, 325, 100, 350, 150, fill="red")

if __name__ == '__main__':
    my_gui = MyGUI()
