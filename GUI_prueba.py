import tkinter as tk
from chemsificar import main as Start

def VentanaPrincipal(): 
  def TextoCaja():
    texto= cajaTexto .get() +" "
    Start(texto)
  #contenedor principal
  ventana= tk.Tk()
  ventana. geometry("300x300")
  #contenedortexto
  cajaTexto= tk.Entry(ventana)
  cajaTexto.pack()
  #boton de envio
  botonEnviar= tk.Button(ventana, text="Chemsificar texto", command=TextoCaja)
  botonEnviar.pack()
  return ventana

def main():
  #salida de todo
  VentanaPrincipal().mainloop()
  
if __name__== "__main__":
  main()