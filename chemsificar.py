#Chemsificador por Francisco Blanco Lopez
#importaciones de modulos
from limpiar import LimpiarCadena as Limpiar
from comparacion import Comparacion
#Convierte el input en un array
def Convertirarray(x):
  return [c for c in x]

#devuelve la cadena final
def ListaTexto(final):
  out= "".join([str(item) for item in final])
  print("Texto chemsificado:",out, sep="\n")
  return out

#Llamado de funciones aqui
def main(cadena):
  ola=Comparacion(Convertirarray(cadena)) #ola es una tupla de dos valores accesar con indices 0,1
  return ListaTexto(Limpiar(ola)) #retorna el resultado para ser usado en la GUI

 #Ejecuta funcion principal, no borrar
if __name__=="__main__":
  #cadena= input("Ingresa el texto a chemsificar: ") + " "
  main()