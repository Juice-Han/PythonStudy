import tkinter as tk

root = tk.Tk()
root.geometry("600x400")

x = 300
y = 200
dx = 5
dy = 5
#도형을 그릴 수 있는 캔버스를 만든다.
canvas = tk.Canvas(root,width=600,height=400,bg="white")
canvas.place(x=0, y=0)

#캔버스에 원을 그린다.

#마우스로 캔버스를 클릭했을 때 원이 생기게 하는 메서드
# def click(event):
#     global x,y
#     canvas.create_oval(x-21,y-21,x+21,y+21,width=0, fill="white")
#     x = event.x
#     y = event.y
#     canvas.create_oval(event.x-20, event.y-20, event.x+20, event.y+20, width=0, fill="red")
# canvas.bind("<Button-1>", click)

#캔버스에서 원이 이동하는 것처럼 보이게 하는 메서드
def move():
    global x,y,dx,dy
    canvas.create_oval(x-21,y-21,x+21,y+21,width=0,fill="white")
    x = x + dx
    y = y + dy
    canvas.create_oval(x-20,y-20,x+20,y+20,width=0,fill="red")
    if x >= canvas.winfo_width(): #고정된 값을 사용하지 않고 메서드를 통해 값을 얻으면 나중에 canvas 크기를 수정할 때 if문 안을 수정하지 않아도 된다.
        dx = -5
    if x < 0:
        dx = 5
    if y >= canvas.winfo_height():
        dy = -5
    if y < 0:
        dy = 5
    root.after(10, move)

root.after(10,move)
root.mainloop()