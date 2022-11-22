"""
Semblant els exercicis de numeracions anteriors,
fer un programa que donat un numero sencer,
retorni les dues claus, una de xifres parelles
i l'altre de senars.

Exemple: 34561 clau1 = 46 clau2 = 351
Exemple: 34261 clau1 = 426 clau2 = 31
"""
num = 0
i = 0
res1 = 0
res2 = 0
mult1 = 1
mult2 = 1

num = int(input("Introdueix número;\n"))

while num !=0:
    #mod y lo del num para restar un digito
    mod = num%10
    num = int(num/10)

    if (mod%2 == 0):
        #el mod por su multiple y le sumamos el mismo numero
        res1 = mod*mult1+res1
        mult1 = mult1*10
    elif (mod%2 !=0):
        res2 = mod*mult2+res2
        mult2 = mult2*10

print("Clau1 =",res1,"Clau2 =",res2)