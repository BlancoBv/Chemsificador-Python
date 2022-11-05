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
#funcion que elimina duplicados
def LimpiarCadena(cadenaResult):
  #variables
  e=cadenaResult[1]
  contadorDel=0
  cadenaAsign= cadenaResult[0]
  
  for i in range(len(cadenaAsign)-1):
    if cadenaAsign[i]==cadenaAsign[i+1]:
      cadenaAsign.pop(i)
      contadorDel+=1
      if contadorDel == e:
        #detiene el ciclo para evitar errores
        break
  return cadenaAsign
  
#Llamado de funciones aqui
def main(cadena):
  #retorna el resultado para ser usado en la GUI
  ola=Comparacion(Convertirarray(cadena)) #ola es una tupla de dos valores accesar con indices 0,1
  return ListaTexto(LimpiarCadena(ola))
 #Ejecuta funcion principal, no borrar
if __name__=="__main__":
  #cadena= input("Ingresa el texto a chemsificar: ") + " "
  main()