from  tkinter import*

def avance(dh,dv):
    global x1,y1
    x1,y1= x1+dh, y1+dv
    can.coords(oval1, x1,y1,x1+30,y1+30)

def gauche():
    avance(-10,0)
def droite():
    avance(10,0)
def haut():
    avance(0,-10)
def bas():
    avance(0,10)
x1=10
y1=10
fen=Tk()
fen.title("deplacement")
can=Canvas(fen, width=200, height=200, bg='purple')
oval1 = can.create_oval(x1,y1,x1+30,y1+30, fill='yellow')
can.pack(side=LEFT)
bout1=Button(fen, text=" quiter ",command=quit).pack(side=BOTTOM)
bout2=Button(fen, text="gauche", command=gauche).pack()
bout3=Button(fen, text="droite ", command=droite).pack()
bout4=Button(fen, text="  haut  ", command=haut).pack()
bout5=Button(fen, text=" bas    ", command=bas).pack()
fen.mainloop()