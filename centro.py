from tkinter import ttk
from tkinter import *
from  tkinter import filedialog as FileDialog
#from menu_principal import *
from block import *

boton = ""
operacion=""
resultado=0
#------------ventana
ventana= Tk()
ventana.title("</master EDITOR>")
ventana.config(bg="green")
ventana.geometry("1315x620")
ventana.state('zoomed')

'''def data():
    for i in range(50):
       Et1=Button(frame,text=i,bg="blue").grid(row=i,column=0)
       Et2=Label(frame,text="my text"+str(i),bg="blue").grid(row=i,column=1)
       Et3=Label(frame,text="..........",bg="blue").grid(row=i,column=2)
       
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=200,height=200)

myframe=Frame(ventana,relief=GROOVE,width=50,height=100)
myframe.place(x=10,y=10)

canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set,bg="red")

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)
data()

ventana.config(width=1300,height=800)
#barramenu=Menu(ventana)
#ventana.config(menu=barramenu,width=1300,height=805)#,bg="black")#23060B
ventana.config(bg="#8F52EE")

#------------Menu Principal__________________'''
Block(ventana)
#
ventana.mainloop()