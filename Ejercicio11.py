"""
Realitzar un programa que comprovi que dos números
 enters son amics. Dos números són amics si la suma 
 dels seus divisors menys ell mateix és igual a l’altre 
 número i viceversa.
Exemple: els números 220 i 284 són amics, la suma dels 
divisors de 220 és igual a 284 i la suma dels divisors 
de 284 és igual a 220.

Altres números:
1184 -1210
171856 – 176336
17041010 – 19150222
...

http://www.vaxasoftware.com/doc_edu/mat/numamigos_esp.pdf

"""
num1 = 0
num2 = 0
divisores = 0

num1=int(input("Introduce el primer numero:\n"))
num2=int(input("Introduce el segundo numero:\n"))

i=1
suma1=0
while i<num1:
    divisores=num1%i
    if divisores== 0:
        suma1=suma1+i
    i=i+1

i=1
suma2=0
while i<num2:
    divisores=num2%i
    if divisores== 0:
        suma2=suma2+i
    i=i+1

if (suma1==num2 and suma2==num1):
    print("Estos 2 numeros son super amiguis")
