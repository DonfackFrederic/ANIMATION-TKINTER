from tkinter import Tk, Canvas, Scale

def rayon(r):
    cnv, side, old=data
    r=int(r)
    m=side/2
    cnv.delete(old)
    data[2]=cnv.create_oval(m-r,m-r,m+r, m+r, fill='purple')
def demo(side):
    global data
    root = Tk()
    cnv = Canvas(root, width=side, height=side)
    cnv.pack()
    old=None
    curseur = Scale(root, orient = "horizontal",
    command=rayon, from_=0, to=200)
    curseur.pack()
    data=[cnv, side, old]
    root.mainloop()

side=400
demo(side)