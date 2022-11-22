"""
Fer un programa que doni la llista dels N 
primers números primers. (N és una entrada
per teclat )Quan posem N vol dir que pot 
ser qualsevol valor, en aquest cas faria 
referencia fins a on arribarem.
"""
num = 1
n = 0
contador = 0

n = int(input("Introduce un numero como limite:\n"))

while contador < n:
    i = 2
    primo = True
    #verificar primo
    while i < num and primo:
        if num%i == 0:
            primo = False
        i+=1
    #mostrar primo
    if primo:
        print(num)
        contador+=1
    num+=1
