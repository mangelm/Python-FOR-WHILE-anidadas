"""
Realitzar un programa que donat un número enter
 i una posició, ens retorni el valor de la part
  menys significativa a partir de la dreta:
Exemple: num = 14563, pos = 2 (incloent), imprimeix 63
"""
num = int(input("introduce numero\n"))

posicion = int(input("introduce la posicion que quieres para dar el numero\n"))

#esta variable es para incluir el numero de la posicion
multiplicacion = 1
for i in range (0, posicion):
    #multiplicamos para sacar el modulo necesario hasta la pos que queremos y asi la incluimos
    multiplicacion = multiplicacion * 10

#al hacer el modulo le quitamos los numeros restantes y nos quedamos con todos los despues de la pos ademas de la pos
num = num % multiplicacion
    
print (num) 
