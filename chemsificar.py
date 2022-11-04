#Chemsificador por Francisco Blanco Lopez

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
#ciclo de comparacion
  while i <len(texto)-1:
    letraAnterior= texto[i]
    if letraAnterior in vocales:
      nuevaCadena.append(letraAnterior)
      nuevaCadena.append("m")
      nuevaCadena.append(texto[i+1])
      i+=2
    else:
      nuevaCadena.append(letraAnterior)
      nuevaCadena.append(texto[i+1])
      i+=2
  return nuevaCadena
#devuelve la cadena final
def ListaTexto(final):
  out= "".join([str(item) for item in final])
  print("Texto chemsificado:",out, sep="\n")

#Llamado de funciones aqui
def main(cadena):
  ListaTexto(Comparacion(Convertirarray(cadena)))
 #Ejecuta funcion principal, no borrar
if __name__=="__main__":
  #cadena= input("Ingresa el texto a chemsificar: ") + " "
  main()
