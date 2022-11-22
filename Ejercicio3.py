"""
Usant la funció input(), creeu un programa que 
sigui capaç de llegir un número sencer 
pel teclat ( format per varis caràcters)  
i que el desi a una variable int. 

Cada caràcter numèric correcte que es llegeixi, 
es mostrarà per pantalla.

Quan l’usuari introdueixi ‘q’ es mostrarà 
a la línia següent el valor de la variable 
de tipus int on ha quedat guardat el número. 

Haurem de convertir cada caràcter que representa 
un número al seu valor numèric, 
es a dir, ‘1’’2’ no és el valor 12, 
sinó que haureu de fer els càlculs mitjançant ASCII.
Veieu la taula ASCII i feu conversions amb els valors. 

Per exemple:
Ficarem ‘1’, ‘2’, ’3’ haurà de guardar-se en una 
variable el valor 123 com a numèric enter.
"""
#ascii comprendido entre 48 a 57 del 0 al 9
""" salida = True
i = 0
a = ""
b = 0
conversion = 0
num = 0

while (salida):
    a = input("introduce cifra\n")
    b = ord(a)
    if (b > 47 and b < 58):
        conversion = b - 48        
        if(i == 0):
            num = conversion

            i+=1
        else:
            num = (num * 10) + conversion

    else:
        salida=False

print(num,"operacion", num + 10) """

salida=True
i=0
caracter=""
ordinal= 0
conversion = 0
decimal = 0

while (salida):
    caracter=input("Introduce cifra:\n")
    ordinal=ord(caracter)
    if (ordinal>47 and ordinal<58):
        conversion = ordinal - 48        
        decimal = (decimal * 10) + conversion
    else:
        salida=False

print(decimal,"operacion", decimal + 10)

"""
#Explicacion

a = input("")
b = ord(a)
print(b)
c = b - 48
print(c)
#multiplico cada caracter ordinal por un 10 segun su posicion desde la segunda:
ejemplo:
1 = 1
2 = 12 * 10
3 = 123 * 10
"""