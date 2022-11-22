"""
Realitzar un programa que donat un número enter, i 
una posició, ens retorni el valor de la posició a 
partir de la dreta:
Exemple:  num =1456, pos = 3, imprimeix 4.
"""
num = 18989
encontrado = False
aux = num
pos = 2
cifra = 0
i = 0

while aux != 0 and not encontrado:
    cifra = aux%10
    i+=1
    if (i == pos):
        encontrado =True
    #Para "restarle" la cifra encontrada al numero (de uno en uno hasta posicion)
    aux = int(aux/10)

print(num,encontrado, cifra)


"""
num = int(input("introduce numero"))

posicion = int(input("introduce la posicion que quieres para dar el numero"))


for i in range (0, posicion):
    pos = num % 10
    num = int(num/10)

print (pos)
"""