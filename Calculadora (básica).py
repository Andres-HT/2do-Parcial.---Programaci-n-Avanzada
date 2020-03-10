from tkinter import *

global a
a=0
global b
b=0
global c
c=0


def acu():
    global c
    c=(10*c)
    l=Label(ventana, text=c).grid(column=0,row=0)


def acu1():
    global c
    c=(10*c)+ 1
    l=Label(ventana, text=c).grid(column=0,row=0)

def acu2():
    global c
    c=(10*c)+ 2
    l=Label(ventana, text=c).grid(column=0,row=0)


def acu3():
    global c
    c=(10*c)+ 3
    l=Label(ventana, text=c).grid(column=0,row=0)

def acu4():
    global c
    c=(10*c)+ 4
    l=Label(ventana, text=c).grid(column=0,row=0)

def acu5():
    global c
    c=(10*c)+ 5
    l=Label(ventana, text=c).grid(column=0,row=0)

def acu6():
    global c
    c=(10*c)+6
    l=Label(ventana, text=c).grid(column=0,row=0)

def acu7():
    global c
    c=(10*c)+7
    l=Label(ventana, text=c).grid(column=0,row=0)

def acu8():
    global c
    c=(10*c)+8
    l=Label(ventana, text=c).grid(column=0,row=0)

def acu9():
    global c
    c=(10*c)+9
    l=Label(ventana, text=c).grid(column=0,row=0)

def sum():
    global a
    global b
    global c
    a=1
    if b==0:
        b=c
        c=0
        l=Label(ventana, text="            ").grid(column=0,row=0)

def rest():
    global a
    global b
    global c
    a=2
    if b == 0:
        b = c
        c = 0
        l = Label(ventana, text="        ").grid(column=0, row=0)

def mult():
    global a
    global b
    global c
    a=3
    if b == 0:
        b = c
        c = 0
        l = Label(ventana, text="          ").grid(column=0, row=0)

def div():
    global a
    global b
    global c
    a=4
    if b == 0:
        b = c
        c = 0
        l = Label(ventana, text="          ").grid(column=0, row=0)

def ecua():
    global a
    global b
    global c

    if a==1:
        l=Label(ventana, text=c+b).grid(column=0,row=0)

    if a==2:
        l=Label(ventana, text=c-b).grid(column=0,row=0)

    if a==3:
        l=Label(ventana, text=c*b).grid(column=0,row=0)

    if a==4:
        try:
          w=b/c
        except:
            w="Indefinido"
        l=Label(ventana, text=w).grid(column=0,row=0)


def ac():
    global a
    global b
    global c
    a=0
    b=0
    c=0
    if b == 0:
        b = c
        c = 0
        l = Label(ventana, text="                          ").grid(column=0, row=0)



ventana=Tk()
ventana.title("Acumulador")
ventana.geometry("200x150")

B1=Button(ventana,text="0",bg="white", fg="black", font=("Corbel 12 "),height=4, width=8,command=acu).grid(column=4,row=3)
B1=Button(ventana,text="1",bg="white", fg="black", font=("Corbel 12 "),height=4, width=8,command=acu1).grid(column=3,row=2)
B2=Button(ventana,text="2",bg="white", fg="black", font=("Corbel 12 "),height=4, width=8,command=acu2).grid(column=4,row=2)
B3=Button(ventana,text="3",bg="white", fg="black", font=("Corbel 12 "),height=4, width=8,command=acu3).grid(column=5,row=2)
B4=Button(ventana,text="4",bg="white", fg="black", font=("Corbel 12 "),height=4, width=8,command=acu4).grid(column=3,row=1)
B5=Button(ventana,text="5",bg="white", fg="black", font=("Corbel 12 "),height=4, width=8,command=acu5).grid(column=4,row=1)
B6=Button(ventana,text="6",bg="white", fg="black", font=("Corbel 12 "),height=4, width=8,command=acu6).grid(column=5,row=1)
B7=Button(ventana,text="7",bg="white", fg="black", font=("Corbel 12 "),height=4, width=8,command=acu7).grid(column=3,row=0)
B8=Button(ventana,text="8",bg="white", fg="black", font=("Corbel 12 "),height=4, width=8,command=acu8).grid(column=4,row=0)
B9=Button(ventana,text="9",bg="white", fg="black", font=("Corbel 12"),height=4, width=8,command=acu9).grid(column=5,row=0)
B10=Button(ventana,text="+",bg="blue", fg="black", font=("Corbel 12 "),height=4, width=8,command=sum).grid(column=6,row=0)
B11=Button(ventana,text="-",bg="blue", fg="black", font=("Corbel 12 "),height=4, width=8,command=rest).grid(column=6,row=1)
B12=Button(ventana,text="*",bg="blue", fg="black", font=("Corbel 12 "),height=4, width=8,command=mult).grid(column=6,row=2)
B13=Button(ventana,text="/",bg="blue", fg="black", font=("Corbel 12 "),height=4, width=8,command=div).grid(column=6,row=3)
B14=Button(ventana,text="=",bg="red", fg="black", font=("Corbel 12"),height=4, width=8,command=ecua).grid(column=3,row=3)
B14=Button(ventana,text="AC",bg="orange", fg="black", font=("Corbel 12 "),height=4, width=8,command=ac).grid(column=5,row=3)


ventana.mainloop()