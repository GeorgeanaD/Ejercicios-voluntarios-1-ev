#este programa dara la opcion entre dos formas geometricas formadas por asteriscos 
#definiremops la funcion
#daremos la primeras opcion entre formas geometricas
#daremos la segunda opcion entre simbolos
#se mostratara la forma elegida
def comienzo():
  print("********************************************")
  print("** ¿CUANTO SABES SOBRE GEOMETRIA BASICA?  **")
  print("********************************************")
  print("*******(solo para los mas listos)***********")
  print("ELIJE")
  print("1.CONTINUARÉ LA DIFÍCIL TAREA")
  print("2.NO ESTOY LISTO PARA ESTO")
  preparado=input("¿1 o 2?")
  return(preparado)
def geometria():
  preparado= int(comienzo())
  if preparado==2: 
    print("le tienes miedo al exito...")
  if preparado==1:
    print("pocos saben responder a esta pregunta, ¿que figura contiene 3 vertices, 3 angulos interiores y si lo dibujas solo necesitas tres trazos con el lapiz?")
    print("1- triangulo")
    print("2- cuadrado")
    print("3-trapezoide")
    triangulo=int(input("ELIJE"))
    if triangulo==3:
      print("vas mas perdido que un sordo en un dictado...")
      print("¡Intentalo otra vez!")
    if triangulo==2:
      print("Vaya!, casi casi...")
      print("¡Intentalo otra vez!")
    if triangulo==1:
      print("Muy bien!!, ahora una mas complicada")
      print("Su area es l*l")
      print("1- trapezoide")
      print("2- triangulo rectangulo")
      print("3- cuadrado")
      cuadrado=int(input("ELIJE"))
      if cuadrado==2:
        print("que pena...")
        print("pero no te preocupes ¡has conseguido tener tu propio triangulo!")
        print("                 * "    )
        print("               *****")
        print("              *******")
        print("             *********")
        print("            ***********")
      if cuadrado==1:
        print("que pena...")
        print("pero no te preocupes ¡has conseguido tener tu propio triangulo!")
        print("                 * "    )
        print("               *****")
        print("              *******")
        print("             *********")
        print("            ***********")
      if cuadrado==3:
        print("eres todo un as de las matematicas!!")
        print("has conseguido tu cuadrado")
        print("**********")
        print("**********")
        print("**********")
        print("**********")
       
  

geometria()
        
    

  