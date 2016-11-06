from Tkinter import *

factor = 0
master = Tk()


# Classe utilizada par alancar popup para o usuario inserir o parametro t
def popup(master):
    global e

    l=Label(master,text="Please, insert \"t\"")
    l.pack()
    e=Entry(master)
    e.pack()
    b=Button(master,text='Ok',command=clean)
    b.pack()


def clean():
    global factor
    global master 
    factor = e.get()
    factor = float(factor) 
    master.destroy()


def start():
    global master
    popup(master)
    master.mainloop()
