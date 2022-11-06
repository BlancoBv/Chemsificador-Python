#compara cada uno de los elementos de la cadena
def Comparacion(texto):
  #variables
  vocales=["a","e","i", "o", "u" ]
  excepciones=["m","n","r"]
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
      if texto[i+1] in vocales or texto[i+1] in excepciones:
        nuevaCadena.append(letraAnterior)
        nuevaCadena.append(texto[i+1])
      else:
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

if __name__=="__main__":
  #cadena= input("Ingresa el texto a chemsificar: ") + " "
  Comparacion()
