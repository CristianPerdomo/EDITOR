from tkinter import ttk
from tkinter import *
from  tkinter import filedialog as FileDialog
#from block import *

def menuprincipal(T,vent,barraMenu):
    def nuevo():
        global ruta
        mensaje.set("Nuevo fichero")
        ruta = ""
        T.delete(1.0, "end")
        vent.title("Mi editor")
    def abrir():
        global ruta
        mensaje.set("Abrir fichero")
        ruta = FileDialog.askopenfilename(
            initialdir='.', 
            filetypes=(("Ficheros de texto", "*.txt"),
            ("archivo de python", "*.py"),
            ("archivo de C++", "*.cpp"),
            ("archivo de C", "*.c"),),
            title="Abrir un fichero de texto")
        if ruta != "":
            fichero = open(ruta, 'r')
            contenido = fichero.read()
            T.delete(1.0,'end')
            T.insert('insert', contenido)
            fichero.close()
            vent.title(ruta + " - Mi editor")
    def guardar():
        mensaje.set("Guardar fichero")
        if ruta != "":
            contenido = T.get(1.0,'end-1c')
            fichero = open(ruta, 'w+')
            fichero.write(contenido)
            fichero.close()
            mensaje.set("Fichero guardado correctamente")
        else:
            guardar_como()
    def guardar_como():
        global ruta
        mensaje.set("Guardar como")
        fichero = FileDialog.asksaveasfile(title="Guardar fichero", 
        mode="w", defaultextension=".py")
        if fichero is not None:
            ruta = fichero.name
            contenido = T.get(1.0,'end-1c')
            fichero = open(ruta, 'w+')
            fichero.write(contenido)
            fichero.close()
            mensaje.set("Fichero guardado correctamente")
        else:
            mensaje.set("Guardado cancelado")
            ruta = ""
    #--------------------------------------------------------------------
    #-----Menu de ARCHIVO_________________________________
    #--------------------------------------------------------------------
    archivomenu=Menu(vent,barraMenu,tearoff=0)
    archivomenu.config(fg="#03f943",bg="#191a19")
    archivomenu.add_command(label="Nuevo",command=nuevo)
    archivomenu.add_command(label="Guardar",command=guardar)
    archivomenu.add_command(label="Abrir archivo",command=abrir)
    archivomenu.add_command(label="")
    archivomenu.add_command(label="Guardar como...",command=guardar_como)
    archivomenu.add_command(label="Salir")
    barraMenu.add_cascade(label="Archivo",menu=archivomenu)
    #--------------------------------------------------------------------
    #-----Menu de CONFIGURACION____________________________
    #--------------------------------------------------------------------
    def Temas():
        ventana2=Toplevel()
        ventana2.title("---Temas---")
        ventana2.resizable(width=1, height=1)
        ventana2.geometry("545x150")
        radioValue = IntVar() 
        ventana2.config(bg="#AB7AF6")
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        rdio1=Radiobutton(ventana2,variable=radioValue, value=1)
        rdio1.place(relx = 0.08, rely = 0.08,relwidth=0.15, relheight=0.22)
        eti1=Label(ventana2,text="tema 1",font="24",fg="#03f943",bg="#340351")
        eti1.place(relx = 0.2, rely = 0.08,relwidth=0.24, relheight=0.22)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$  

        rdio2=Radiobutton(ventana2,variable=radioValue, value=2)
        rdio2.place(relx = 0.08, rely = 0.38,relwidth=0.15, relheight=0.22)
        eti2=Label(ventana2,text="tema 2",font="24",fg="#03f943",bg="#340351")
        eti2.place(relx = 0.2, rely = 0.38,relwidth=0.24, relheight=0.22)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        rdio3=Radiobutton(ventana2,variable=radioValue, value=3)
        rdio3.place(relx = 0.08, rely = 0.68,relwidth=0.15, relheight=0.22)
        eti3=Label(ventana2,text="tema 3",font="24",fg="#03f943",bg="#340351")
        eti3.place(relx = 0.2, rely = 0.68,relwidth=0.24, relheight=0.22)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$...........................
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$...........................
        rdio4=Radiobutton(ventana2,variable=radioValue, value=4)
        rdio4.place(relx = 0.52, rely = 0.08,relwidth=0.15, relheight=0.22)
        eti4=Label(ventana2,text="tema 4",font="24",fg="#03f943",bg="#340351")
        eti4.place(relx = 0.64, rely = 0.08,relwidth=0.24, relheight=0.22)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        rdio5=Radiobutton(ventana2,variable=radioValue, value=5)
        rdio5.place(relx = 0.52, rely = 0.38,relwidth=0.15, relheight=0.22)
        eti5=Label(ventana2,text="tema 5",font="24",fg="#03f943",bg="#340351")
        eti5.place(relx = 0.64, rely = 0.38,relwidth=0.24, relheight=0.22)
        #$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        rdio6=Radiobutton(ventana2,variable=radioValue, value=6)
        rdio6.place(relx = 0.52, rely = 0.68,relwidth=0.15, relheight=0.22)
        eti6=Label(ventana2,text="tema 6",font="24",fg="#03f943",bg="#340351")
        eti6.place(relx = 0.64, rely = 0.68,relwidth=0.24, relheight=0.22)
        ventana2.mainloop()
        #=================================================================
        #=================================================================
    def personalizar ():
        ventana3=Toplevel()
        ventana3.title("---Personalizar---")
        ventana3.config(bg="#9C5EFC")
        Boton=Button(ventana3,bg="red").grid(row=4,column=4)
        boton=Button(ventana3,bg="red").grid(row=1,column=1)

        ventana3.mainloop()
    editormenu=Menu(vent,barraMenu,tearoff=0)
    editormenu.config(fg="#03f943",bg="#191a19")
    editormenu.add_command(label="Temas",command=Temas)
    editormenu.add_command(label="Personalizar",command=personalizar)
    editormenu.add_command(label="Tipo de fuente")
    barraMenu.add_cascade(label="Configuracion",menu=editormenu)
    #-----Menu de Ayuda____________________________
    ayudamenu=Menu(vent,barraMenu,tearoff=0)
    ayudamenu.config(fg="#03f943",bg="#191a19")
    ayudamenu.add_command(label="About (master editor) ")
    ayudamenu.add_command(label="Reference code")
    ayudamenu.add_command(label="¿Que puede hacer?")
    barraMenu.add_cascade(label="Help",menu=ayudamenu)
    mensaje = StringVar()
    mensaje.set("Bienvenido a tu Editor")
    monitor = Label(vent, textvar=mensaje, justify='left',bg="#AB7AF6",fg="black",font="Lucida 8")
    monitor.place(relx = 0.001, rely = 0.955,relwidth=0.125, relheight=0.04)
# esto es muy impresionante
