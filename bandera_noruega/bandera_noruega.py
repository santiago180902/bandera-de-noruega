from tkinter import *
# ---------------------------

ventana_principal = Tk()

ventana_principal.title("Bandera de Noruega")

ventana_principal.geometry("800x500")

ventana_principal.resizable(0,0)

ventana_principal.config(bg="white")
#----------------------------------
# frame entrada de datos
#----------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="maroon", width=200, height=200)
frame_entrada.place(x=0, y=300)
#----------------------------------
frame_operacion = Frame(ventana_principal)
frame_operacion.config(bg="maroon", width=200, height=200)
frame_operacion.place(x=0, y=0)
#----------------------------------
frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg="maroon", width=700, height=200)
frame_resultado.place(x=300, y=300)
#--------------------------------------------------------
frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg="maroon", width=700, height=200)
frame_resultado.place(x=300, y=0)
#--------------------------------------------------------
frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg="blue4", width=50, height=500)
frame_resultado.place(x=225, y=0)
#----------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="blue4", width=1000, height=50)
frame_entrada.place(x=0, y=225)
#etiqueta para el titulo de la app
titulo = Label(frame_entrada, text= "Bandera de noruega")



ventana_principal.mainloop()