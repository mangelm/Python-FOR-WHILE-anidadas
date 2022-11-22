"""
Feu un programa que imprimeixi per pantalla de forma consecutiva 
la sèrie de caràcters següent, amb aquesta metodologia:   
   -  (inici), premem intro i sortirà el següent caràcter, 
   \ , premem intro i sortirà el següent caràcter, 
   | , premem intro i sortirà el següent caràcter,  
   / , premem intro i sortirà el següent caràcter que serà l’inici una altre vegada.

El programa sortirà quan polsem la lletra ‘s’ o ‘S’. Per netejar la pantalla farem:

import os
Quan faci falta netejar la pantalla farem, os.system(‘cls’)
"""
"""
import os

inicio = True
contador = 0
salir = ""

while inicio:
        contador = 0
        salir = input("Introduce 's' para salir sino, haz intro:\n")
        if salir !="s" and salir !="S":
            contador +=1
            if contador == 1:
                print("-")
                salir = input("Introduce 's' para salir sino, haz intro:\n")
                os.system('cls')
                contador +=1
                if salir != "s" and salir != "S": 
                    if contador == 2:
                        print("'\\'")
                        salir = input("Introduce 's' para salir sino, haz intro:\n")
                        os.system('cls')
                        contador +=1
                        if salir !="s" and salir !="S":
                           if contador == 3:
                            print("|")
                            salir = input("Introduce 's' para salir sino, haz intro:\n")
                            os.system('cls')
                            contador +=1
                            if salir != "s" and salir != "S":
                                if contador == 4:
                                    print("/")
                                    salir = input("Introduce 's' para salir sino, haz intro:\n")
                                    os.system('cls')
                                    contador = 0
                            else:
                                inicio = False
                        else:
                            inicio = False
                else:
                    inicio = False
        else:
            inicio = False
""" 

"""
a = input()
if (a == "s" or a== "S"):
    os.system("cls")
else:
    while (a != "s" and a!= "S"):
        print(" - ")
        a = input()
        os.system("cls")
        if (a != "s" and a!= "S"):
            print(" \ ") 
            a = input()
            os.system("cls")
        if (a != "s" and a!= "S"):
            print(" | ")
            a = input()
            os.system("cls")
        if (a != "s" and a!= "S"):
            print(" / ")
            a = input()
            os.system("cls")
"""

# 1 print 1 input 1 os.system("cls")
import os

print("Si quieres iniciar o continuar el ciclo, pulsa el botón Intro. Si quieres salir, pulsa el botón S.")
a = input()
i = 0
c = ''
while (a != "s" and a!= "S"):
    os.system('cls')
    if i == 0:
        c = '-'
    elif (i == 1):
        c = '\\'
    elif (i == 2):
        c = '|'
    elif (i == 3):
        c = '/'
    
    print(c)
    i+=1
    if i == 4: #i%=4 # i = i%4
        i = 0
    a = input()
        
os.system('cls') 