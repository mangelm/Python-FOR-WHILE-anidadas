"""
Feu un programa que ens mostri un menú per pantalla per fer càlculs bàsics:
=========MENU===========
1.- Suma
2.- Resta
3.- SORTIR
========================
L’usuari pot entrar pel número d’opció o el nom 
(posant suma, resta o sortir), les cadenes de 
caràcters (strings) a python es defineix com a, var = “valor cadena”
El procés de cada opció (excepte sortir) serà:
Netejar la pantalla (amb os.system(‘cls’))
Demanar els valors
Mostrar el resultat, quan polseu intró tornarà al menú inicial	
"""
import os

eleccion = ""
numero = 0
numero2 = 0
operacion = 0
i = 0 

print("=========MENU===========")
print("1.- Suma") 
print("2.- Resta") 
print("3.- SORTIR")
print("========================")
    
eleccion = input("Escoge una opción del menu:\n")


while eleccion !="SORTIR" and eleccion !="sortir" and eleccion !="3":
    numero = int(input("Introduce un numero para hacer la operacion:\n"))
    numero2 = int(input("Introduce el segudo numero para hacer la operacion:\n"))
    
    if eleccion == "1" or eleccion == "2":
        os.system('cls')

        if eleccion == "1":
            operacion = numero + numero2
        
        elif eleccion == "2":
            operacion = numero - numero2
    
        print("Resultado: ",operacion)
        
    eleccion = input("Escoge una opción del menu:\n")
    i+=1
print("Has salido del programa")