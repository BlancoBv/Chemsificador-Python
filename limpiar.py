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

if __name__=="__main__":
  #cadena= input("Ingresa el texto a chemsificar: ") + " "
  LimpiarCadena()