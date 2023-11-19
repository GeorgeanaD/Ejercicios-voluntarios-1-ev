#Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número.
def factorial():
  numero=int(input("Dime un numero y te dire su factorial: "))
  f=1
  if numero<0:
    print("Ingresa otro numero porfavor")
  if numero>0:
    for cont in range(1, numero+1):
      f=f*cont
  print("Factorial: ", f)
factorial()
    