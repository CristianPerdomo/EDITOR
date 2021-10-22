def funciones(T,vent):
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
    