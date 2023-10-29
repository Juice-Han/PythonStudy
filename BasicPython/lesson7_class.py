import tkinter as tk

class Ball:
    def __init__(self,x,y,dx,dy,color):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.color = color

    def move(self, canvas):
        self.erase(canvas)
        self.x += self.dx
        self.y += self.dy
        self.draw(canvas)
        
        if self.x > canvas.winfo_width() :
            self.dx = -1
        if self.x <= 0:
            self.dx = 1
        if self.y > canvas.winfo_height():
            self.dy = -1
        if self.y <= 0:
            self.y = 1

    def erase(self, canvas):
        canvas.create_oval(self.x - 21, self.y - 21, self.x + 21, self.y +21, width=0, fill="white")
    def draw(self, canvas):
        canvas.create_oval(self.x - 20, self.y - 20, self.x + 20, self.y + 20, width=0, fill=self.color)

class Rectangle(Ball):
    def erase(self, canvas):
        canvas.create_rectangle(self.x - 21, self.y - 21, self.x + 21, self.y +21, width=0, fill="white")
    def draw(self, canvas):
        canvas.create_rectangle(self.x - 21, self.y - 21, self.x + 21, self.y +21, width=0, fill=self.color)

b = Ball(400, 300, 1, 1, "red")
c = Ball(500,200,-1,1,"Blue")
d = Rectangle(600, 500, -1, -1, "green")

def loop():
    b.move(canvas)
    c.move(canvas)
    d.move(canvas)
    root.after(10, loop)

root = tk.Tk()
root.geometry("800x600")

canvas = tk.Canvas(root, width=800, height=600, bg = "white")
canvas.place(x=0,y=0)

root.after(10, loop)
root.mainloop()