from tkinter import *
ventana=Tk()
ventana.title("*GATO*GAME*")
ventana.geometry("100x100")


global w,i
w=0
i=0
global m, t
m=[[" "," "," "],[" "," "," " ],[" "," "," "]]
t=[[0,0,0],[0,0,0],[0,0,0]]

def a00():
    global w
    w=w+1
    bx()


def a01():
    global w
    w = w + 1
    bx1()


def a02():
    global w
    w = w + 1
    bx2()


def a10():
    global w
    w = w + 1
    bx3()


def a11():
    global w
    w = w + 1
    bx4()


def a12():
    global w
    w = w + 1
    bx5()


def a20():
    global w
    w = w + 1
    bx6()


def a21():
    global w
    w = w + 1
    bx7()


def a22():
    global w
    w = w + 1
    bx8()


def bx():
     global w, m, t, i
     if w%2 == 0:
         B1 = Button(ventana, text="O", bg="pink", fg="black", font=("Corbel 12 "), height=3,width=6)
         B1.grid(column=0, row=0)
         B1.config( state = "disabled")
         m[0][0]= "O"
         t[0][0]= 1


     else:
         B1 = Button(ventana, text="X", bg="orchid", fg="black", font=("Corbel 12 "), height=3,width=6)
         B1.grid(column=0, row=0)
         B1.config(state= "disabled")
         m[0][0] = "X"
         t[0][0] = 2
     i+=1
     winner()



def bx1():
    global w, m, t, i
    if w % 2 == 0:
        B2 = Button(ventana, text="O", bg="pink", fg="black", font=("Corbel 12 "), height=3,width=6)
        B2.grid(column=1, row=0)
        B2.config(state="disabled")
        m[0][1] = "O"
        t[0][1] = 1
    else:
        B2 = Button(ventana, text="X", bg="orchid", fg="black", font=("Corbel 12 "), height=3,width=6)
        B2.grid(column=1, row=0)
        B2.config(state="disabled")
        m[0][1] = "X"
        t[0][1] = 2
    i += 1
    winner()

def bx2():
    global w, m, t, i
    if w % 2 == 0:
        B3 = Button(ventana, text="O", bg="pink", fg="black", font=("Corbel 12 "), height=3,width=6)
        B3.grid(column=2, row=0)
        B3.config(state="disabled")
        m[0][2] = "O"
        t[0][2] = 1
    else:
        B3 = Button(ventana, text="X", bg="orchid", fg="black", font=("Corbel 12 "), height=3,width=6)
        B3.grid(column=2, row=0)
        B3.config(state="disabled")
        m[0][2] = "X"
        t[0][2] = 2
    i += 1
    winner()

def bx3():
    global w, m, t, i
    if w % 2 == 0:
        B4 = Button(ventana, text="O", bg="pink", fg="black", font=("Corbel 12 "), height=3,width=6)
        B4.grid(column=0, row=1)
        B4.config(state="disabled")
        m[1][0] = "O"
        t[1][0] = 1
    else:
        B4 = Button(ventana, text="X", bg="orchid", fg="black", font=("Corbel 12 "), height=3,width=6)
        B4.grid(column=0, row=1)
        B4.config(state="disabled")
        m[1][0] = "X"
        t[1][0] = 2
    i += 1
    winner()

def bx4():
    global w, m, t, i
    if w % 2 == 0:
        B5 = Button(ventana, text="O", bg="pink", fg="black", font=("Corbel 12 "), height=3,width=6)
        B5.grid(column=1, row=1)
        B5.config(state="disabled")
        m[1][1] = "O"
        t[1][1] = 1
    else:
        B5 = Button(ventana, text="X", bg="orchid", fg="black", font=("Corbel 12 "), height=3,width=6)
        B5.grid(column=1, row=1)
        B5.config(state="disabled")
        m[1][1] = "X"
        t[1][1] = 2
    i += 1
    winner()

def bx5():
    global w, m, t, i
    if w % 2 == 0:
        B6 = Button(ventana, text="O", bg="pink", fg="black", font=("Corbel 12 "), height=3,width=6)
        B6.grid(column=2, row=1)
        B6.config(state="disabled")
        m[1][2] = "O"
        t[1][2] = 1
    else:
        B6 = Button(ventana, text="X", bg="orchid", fg="black", font=("Corbel 12 "), height=3,width=6)
        B6.grid(column=2, row=1)
        B6.config(state="disabled")
        m[1][2] = "X"
        t[1][2] = 2
    i += 1
    winner()

def bx6():
    global w, m, t, i
    if w % 2 == 0:
        B7 = Button(ventana, text="O", bg="pink", fg="black", font=("Corbel 12 "), height=3,width=6)
        B7.grid(column=0, row=2)
        B7.config(state="disabled")
        m[2][0] = "O"
        t[2][0] = 1
    else:
        B7 = Button(ventana, text="X", bg="orchid", fg="black", font=("Corbel 12 "), height=3,width=6)
        B7.grid(column=0, row=2)
        B7.config(state="disabled")
        m[2][0] = "X"
        t[2][0] = 2
    i += 1
    winner()

def bx7():
    global w, m, t, i
    if w % 2 == 0:
        B8 = Button(ventana, text="O", bg="pink", fg="black", font=("Corbel 12 "), height=3,width=6)
        B8.grid(column=1, row=2)
        B8.config(state="disabled")
        m[2][1] = "O"
        t[2][1] = 1
    else:
        B8 = Button(ventana, text="X", bg="orchid", fg="black", font=("Corbel 12 "), height=3,width=6)
        B8.grid(column=1, row=2)
        B8.config(state="disabled")
        m[2][1] = "X"
        t[2][1] = 2
    i += 1
    winner()


def bx8():
    global w, m, t, i
    if w % 2 == 0:
        B9 = Button(ventana, text="O", bg="pink", fg="black", font=("Corbel 12 "), height=3,width=6)
        B9.grid(column=2, row=2)
        B9.config(state="disabled")
        m[2][2] = "O"
        t[2][2]= 1
    else:
        B9 = Button(ventana, text="X", bg="orchid", fg="black", font=("Corbel 12 "), height=3,width=6)
        B9.grid(column=2, row=2)
        B9.config(state="disabled")
        m[2][2] = "X"
        t[2][2] = 2
    i += 1
    winner()

def winner():
    global w, m, t, i

    if      ((t[0][0]==1 and t[0][1] == 1 and t[0][2]==1) or
            (t[1][0]== 1 and t[1][1] == 1 and t[1][2]==1) or
            (t[2][0]== 1 and t[2][1] == 1 and t[2][2]==1) or
            (t[0][0]== 1 and t[1][0] == 1 and t[2][0]==1) or
            (t[0][1]== 1 and t[1][1] == 1 and t[2][1]==1) or
            (t[0][2]== 1 and t[1][2] == 1 and t[2][2]==1) or
            (t[0][0]== 1 and t[1][1] == 1 and t[2][2]==1) or
            (t[2][0]== 1 and t[1][1] == 1 and t[0][2]==1)):
                l=Label(ventana, text ="GANO EL JUDADOR 'O' ", bg="blue", fg="white", font=("Corbel 42 ")).grid(column=3,row=0)
                B1.config(state="disabled")
                B2.config(state="disabled")
                B3.config(state="disabled")
                B4.config(state="disabled")
                B5.config(state="disabled")
                B6.config(state="disabled")
                B7.config(state="disabled")
                B8.config(state="disabled")
                B9.config(state="disabled")


    elif    ((t[0][0] == 2 and t[0][1]==2 and t[0][2]==2) or
            (t[1][0] == 2 and t[1][1] == 2 and t[1][2] == 2) or
            (t[2][0] == 2 and t[2][1] == 2 and t[2][2] == 2) or
            (t[0][0] == 2 and t[1][0] == 2 and t[2][0] == 2) or
            (t[0][1] == 2 and t[1][1] == 2 and t[2][1] == 2) or
            (t[0][2] == 2 and t[1][2] == 2 and t[2][2] == 2) or
            (t[0][0] == 2 and t[1][1] == 2 and t[2][2] == 2) or
            (t[2][0] == 2 and t[1][1] == 2 and t[0][2] == 2)):
            l = Label(ventana, text="GANO EL JUDADOR 'X' ", bg="blue", fg="white", font=("Corbel 24 ")).grid(column=3, row=0)
            B1.config(state="disabled")
            B2.config(state="disabled")
            B3.config(state="disabled")
            B4.config(state="disabled")
            B5.config(state="disabled")
            B6.config(state="disabled")
            B7.config(state="disabled")
            B8.config(state="disabled")
            B9.config(state="disabled")

    else:
        if (i == 9):
              l=Label(ventana, text = "EMPATE ",bg="blue", fg="white", font=("Corbel 42 ")).grid(column=3,row=0)



B1=Button(ventana,text="  ",bg="lightblue", fg="black", font=("Corbel 12 "), height=3,width=6, command=a00)
B1.grid(column=0,row=0)
B2=Button(ventana,text="  ",bg="lightblue", fg="black", font=("Corbel 12 "),height=3,width=6, command=a01)
B2.grid(column=1,row=0)
B3=Button(ventana,text="  ",bg="lightblue", fg="black", font=("Corbel 12 "),height=3,width=6, command=a02)
B3.grid(column=2,row=0)
B4=Button(ventana,text="  ",bg="lightblue", fg="black", font=("Corbel 12 "),height=3,width=6,command=a10)
B4.grid(column=0,row=1)
B5=Button(ventana,text="  ",bg="lightblue", fg="black", font=("Corbel 12 "),height=3,width=6,command=a11)
B5.grid(column=1,row=1)
B6=Button(ventana,text="  ",bg="lightblue", fg="black", font=("Corbel 12 "),height=3,width=6,command=a12)
B6.grid(column=2,row=1)
B7=Button(ventana,text="  ",bg="lightblue", fg="black", font=("Corbel 12 "),height=3,width=6,command=a20)
B7.grid(column=0,row=2)
B8=Button(ventana,text="  ",bg="lightblue", fg="black", font=("Corbel 12 "),height=3,width=6,command=a21)
B8.grid(column=1,row=2)
B9=Button(ventana,text="  ",bg="lightblue", fg="black", font=("Corbel 12 "),height=3,width=6,command=a22)
B9.grid(column=2,row=2)


ventana.mainloop()