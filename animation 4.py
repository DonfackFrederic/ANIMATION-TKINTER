from tkinter import Label,Canvas,mainloop,Tk

def pointeur(event):
    chaine.configure(text="clic detecter a X="+str(event.x) + "Y="+str(event.y))
    cadre.create_oval(str(event.x),str(event.y), str(event.x +10 ) , str(event.y +10),fill='red')
fen=Tk()
cadre=Canvas(fen, width=200, height=200, bg='orange')
cadre.bind("<Button-1>", pointeur)
cadre.pack()
chaine=Label(fen)

chaine.pack()
mainloop()