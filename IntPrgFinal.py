'''
Diseñar un algoritmo que permita:
Leer 15230 números y cargarlos en un vector.
1) Calcular cual es el máximo de ese vector (de manera programática, sin ordenar)
2) Calcular el promedio del vector/array de los valores impares
3) Generar otro vector con los números pares del vector original
4) Calcular el mínimo del vector generado (El vector de los pares)
5) Insertar en la después de cada valor impar el número 999, en el vector original
6) Elimine del segundo vector (pares) el número 4, contemplar que en el caso de
no existir dicho numero eliminar el número que se encuentra en la primer posición. 
7) Invente un enunciado diferente a los anteriores y realícelo (EJ ; cual es la
suma de los elementos del segundo vector)
'''

def cargar (mensajeIngresar, vec):
  while (len(vec) < 15230):
    numero = int(input(mensajeIngresar))
    vec.append(numero)

def buscarMayor (vec):
  mayor = vec[0]
  for i in range (0, len(vec), 1):
    if (mayor < vec[i]):
      mayor = vec[i]
  return mayor

def promedioImpares (vec):
  acum = 0
  contador = 0
  for i in range (0, len(vec), 1):
    if (vec[i] % 2 != 0):
      acum += vec[i]
      contador += 1
  if (contador != 0):
    promedio = acum / contador
  else:
    promedio = 0
  return promedio

def newVectorPares (vec):
  newVec = []
  for i in range (0, len(vec), 1):
    if (vec[i] % 2 == 0):
      newVec.append(vec[i])
  return newVec

def menorVectorPares (vecPares):
  menor = vecPares[0]
  for i in range (0, len(vecPares), 1):
    if menor > vecPares[i]:
      menor = vecPares[i]
  return menor

def insert999 (vec):
  i = 0
  while i < len(vec):
    if vec[i] % 2 == 1:
      i += 1
      vec.insert(i, 999)
    i+= 1
     
def eliminarCuatro (vecPares):
  i = 0
  lenInicio = len(vecPares)
  while i < len(vecPares):
    if vecPares[i] == 4:
      vecPares.pop(i)
    i += 1
  if lenInicio == len(vecPares):
    vecPares.pop(0)

def invertirOrden (vec):
  newVec = []
  i = len(vec) - 1
  while i >= 0:
    newVec.append(vec[i])
    i = i - 1
  return newVec


vector = []

cargar ("Quiere ingresar un numero (n para stop): ",
    "Ingrese un numero: ",
    vector)

if (len(vector) != 0):
  print ("1) Calcular cual es el máximo de ese vector (de manera programática, sin ordenar)")
  mayor = buscarMayor(vector)
  print(f"El numero mayor del vector es: {mayor}")

  print("")
  print("")

  print("2) Calcular el promedio del vector/array de los valores impares")
  promImpa = promedioImpares(vector)

  if promImpa != 0:
    print (f"El promedio de los impares es de {promImpa}")
  else:
    print("no hay numeros impares en el vector")

  print("")
  print("")

  print("3) Generar otro vector con los números pares del vector original")
  vectorPares = newVectorPares(vector)
  print("Nuevo vector: ")
  print(vectorPares)

  print("")
  print("")

  print("4) Calcular el mínimo del vector generado (El vector de los pares)")
  menorVecPares = menorVectorPares(vectorPares)
  print(f"El menor del nuevo vector Pares es: {menorVecPares}")

  print("")
  print("")

  print("5) Insertar en la después de cada valor impar el número 999, en el vector original")
  insert999(vector)
  print("nuevo vector: ")
  print(vector)

  print("")
  print("")

  print("6) Elimine del segundo vector (pares) el número 4, contemplar que en el caso de " +
  "no existir dicho numero eliminar el número que se encuentra en la primer posición.")
  eliminarCuatro(vectorPares)
  print("Nuevo vector de Pares")
  print(vectorPares)
  
  print("")
  print("")

  print("7) Realizar un nuevo vector en base al original, este nuevo vector " +
      "Debera tener el orden invertido")
  vectorAlReves = invertirOrden(vector)
  print("Nuevo vector")
  print(vectorAlReves)