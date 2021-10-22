from tkinter import *
from  tkinter import filedialog as FileDialog
from tkinter import ttk
from menu_principal import *
def Block(vent):
    barramenu=Menu(vent)
    vent.config(menu=barramenu,width=1300,height=805)#,bg="black")#23060B
    framaTex=Frame(vent,bg="blue").place(relx = 0.001, rely = 0.07,relwidth=0.815, relheight=0.85)
    T = Text(vent,bg="black",fg="#03f943",font="13")
    T.configure(insertbackground='white')
    T.configure(insertbackground='white')#color del puntero del texto
    
    horscroll=Scrollbar(framaTex,orient=HORIZONTAL)
    horscroll.config(command=T.xview)
    verscroll=Scrollbar(framaTex, orient=VERTICAL,command=T.yview)
    #------------PESTAÑAS_________________________________
    barra_pestañas=Frame(framaTex,bg="red")
    barra_pestañas.place(relx = 0.001, rely = 0.003,relwidth=0.815, relheight=0.06) 
    s = ttk.Style()
    s.configure("Peligro.TButton", foreground="#ff0000",activebackground="#F50743",relief="groove")
    s.map("C.TButton",
            foreground=[('pressed', 'black'), ('active', 'black')],
            background=[('pressed', '!disabled', 'blue'), ('active', 'gray')])
    #botones de pestaña
    pestaña1= ttk.Button(barra_pestañas,text="hola")
    pestaña1.place(relx=0.01,rely=0.18,relwidth=0.1, relheight=0.65)
    X1= Button(pestaña1,text="X",bg="red",font="impack 7")
    X1.place(relx=0.84,rely=0.065,relwidth=0.15, relheight=0.5)
    #_________CONFIGURACIÓN DE Text------------
    T.config(yscrollcommand=verscroll.set, wrap="none")
    T.place(in_=framaTex,relx = 0.001, rely = 0.07,relwidth=0.75, relheight=0.8)
    horscroll.place(relx = 0.001, rely = 0.9,relwidth=0.8, height=20)
    verscroll.place(relx = 0.8, rely = 0.08,width=19, relheight=0.85)
    menuprincipal(T,vent,barramenu)