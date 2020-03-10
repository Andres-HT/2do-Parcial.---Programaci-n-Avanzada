from tkinter import *
ventana = Tk()
ventana.title("CUADRO MÁGICO")
ventana.geometry("100x100")

global c, r
c=2
r=2

def m():
    for i in [0,1,2,3,4]:
        for j in [0,1,2,3,4]:
            B=Button(ventana, text=" ", bg="black", height=4, width=8)
            B.grid(column=i, row=j)

def up():
    global c, r
    r=r-1
    if r<0:
        r=4
    B.grid(column=c, row=r)
    B.config(bg="yellow")

def left():
    global c, r
    c-=1
    if c<0:
        c=4
    B.grid(column=c, row=r)
    B.config(bg="pink")
def right():
    global c, r
    c=c+1
    if c>4:
        c=0
    B.grid(column=c, row=r)
    B.config(bg="purple")

def down():
    global c, r
    r=r+1
    if r>4:
        r=0
    B.grid(column=c, row=r)
    B.config(bg="orange")

m()
B=Button(ventana, text=" ﻖ ", bg="yellow", fg="black", font=("Algerian 9 "), height=4, width=8)
B.grid(column=c,row=r)
B1=Button(ventana,text=" ↑ ",bg="lightblue",fg="black", font=("Algerian 12 "),height=3,width=6, command=up)
B1.grid(column=10,row=2)
B2=Button(ventana,text=" ← ",bg="lightblue", fg="black",font=("Algerian 12 "),height=3,width=6, command=left)
B2.grid(column=9,row=3)
B3=Button(ventana,text=" → ",bg="lightblue",fg="black", font=("Algerian 12 "),height=3,width=6, command=right)
B3.grid(column=11,row=3)
B4=Button(ventana,text=" ↓ ",bg="lightblue",fg="black",font=("Algerian 12"),height=3,width=6,command=down)
B4.grid(column=10,row=4)

ventana.mainloop()