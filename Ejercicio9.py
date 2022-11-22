"""
Realitzar un programa que donat un número enter i 
una posició, ens retorni el valor de la part més 
significativa a partir de la dreta:
Exemple: num = 14563, pos =  2 (sense incloure) , 
imprimeix 145
"""
num=0
pos=0

num=int(input("Introduce el numero\n"))

pos=int(input("Introduce la posicion que quieres ver\n"))

for i in range (0, pos):
    #Para "restarle" la cifra encontrada al numero (de uno en uno hasta posicion)
    num = int(num/10)
print(num)  