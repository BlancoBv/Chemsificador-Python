import tkinter as tk
import pyperclip
from chemsificar import main as Chemsificar

def VentanaPrincipal(): 
  def TextoCaja():
    texto= cajaTexto .get() +" "
    #Feedback al usuario si no ingresa ningun dato
    if texto== " ":
      cajaResultado["text"]="Escribe algo"
    else:
      result=Chemsificar(texto) 
      cajaResultado["text"]= result
    return result
  
  def Copiar(): #copia el texto del resultado
    pyperclip.copy(TextoCaja())
    

  #contenedor principal
  ventana= tk.Tk()
  ventana. geometry("300x300")
  ventana.title("Chemsificador")
  cliptext = ventana.clipboard_get()
  #contenedo de texto de entrada
  cajaTexto= tk.Entry(ventana, font="Consolas")
  cajaTexto.pack()
  #boton de envio
  botonEnviar= tk.Button(ventana, text="Chemsificar texto", command=TextoCaja)
  botonEnviar.pack()
  #contenedor de texto de salida
  cajaResultado= tk.Label(ventana, text="Chemfisicador owo", background="white", width="30", relief="raised", height="10")
  cajaResultado.pack()
  #boton para copiar texto al portapapeles
  botonCopiar= tk.Button(ventana,text="Copiar al portapapeles", command=Copiar)
  botonCopiar.pack()
  
  label=tk.Label(ventana, text=cliptext)
  label.pack()
  return ventana

def main():
  #salida de todo
  VentanaPrincipal().mainloop()
 #Ejecuta funcion principal, no borrar
if __name__== "__main__":
  main()