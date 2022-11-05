#Chemsificador por Francisco Blanco Lopez
from limpiar import LimpiarCadena as Limpiar
#Convierte el input en un array
def Convertirarray(x):
  return [c for c in x]
  
#compara cada uno de los elementos de la cadena
def Comparacion(texto):
  #variables
  vocales=["a","e","i", "o", "u" ]
  letraAnterior= ""
  nuevaCadena=[]
  i= 0

  #funcion que calcula el valor de E
  def E():
    valueE= len(texto)-2
    print("Valor de E:",valueE)
    return valueE
  
#ciclo de comparacion
  while i <len(texto)-1:
    letraAnterior= texto[i]
    if letraAnterior in vocales:
      nuevaCadena.append(letraAnterior)
      nuevaCadena.append("m")
      nuevaCadena.append(texto[i+1])
      #i+=2
      i+=1
    else:
      nuevaCadena.append(letraAnterior)
      nuevaCadena.append(texto[i+1])
      #i+=2
      i+=1
  print("cadena resultante:",nuevaCadena)
  return nuevaCadena, E()

#devuelve la cadena final
def ListaTexto(final):
  out= "".join([str(item) for item in final])
  print("Texto chemsificado:",out, sep="\n")
  return out

  
#Llamado de funciones aqui
def main(cadena):
  #retorna el resultado para ser usado en la GUI
  ola=Comparacion(Convertirarray(cadena)) #ola es una tupla de dos valores accesar con indices 0,1
  return ListaTexto(Limpiar(ola))
 #Ejecuta funcion principal, no borrar
if __name__=="__main__":
  #cadena= input("Ingresa el texto a chemsificar: ") + " "
  main()