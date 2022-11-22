"""
Farem un programa que permeti llegir pel teclat un número romà, 
i ens retorni el valor numèric decimal.
Llegirem la pulsació de cada tecla amb input.
Només admetrem els símbols I, V, X, L, C, D, M. ( o l’equivalent 
en minúscules )
Les altres tecles polsades seran ignorades.
Cada cop que llegim una tecla vàlida, mostrarem el símbol en 
pantalla ( sempre en majúscules )
Quan l’usuari premi ENTER ( busqueu-ne el codi ASCII ), atureu el 
procés i mostreu el número decimal equivalent. Amb això acaba el 
programa.Per a començar farem un conversor senzill, que apliqui 
les normes bàsiques (n’hi ha forces més): 
cada lletra té el seu pes. Per saber el valor decimal del número, 
haurem de sumar els valors individuals de cadascun dels símbols
romans en el cas de que un símbol de menor valor estigui a 
l’esquerra d’un de major valor, aquest RESTARÀ en comptes de sumar.
no permetrem en cap cas que V, L i D estiguin a l’esquerra 
d’un valor major ( no poden restar)
no permetrem en cap cas repetir el símbol V, L i D

Simbol  I   V   X   L   C   D   M   
Valor   1   5   10  50  100 500 1000
"""
romano = ""

if romano == "I":
    romano = 1
elif romano == "V":
    romano = 5
elif romano == "X":
    romano = 10
elif romano == "L":
    romano = 50
elif romano == "C":
    romano = 100
elif romano == "D":
    romano = 500
elif romano == "M":
    romano = 1000