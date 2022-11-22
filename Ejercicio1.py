"""
Farem un programa que llegeixi del teclat 
un número múltiple de 10. No acceptarem 
el número fins que sigui múltiple de deu, 
si no ho és, el tornem a demanar.
Un cop el tinguem, el programa escriurà 
una sortida per pantalla tal i com es 
mostra ens els següents exemples: per exemple, 

entrada 		        missatge de sortida
1200            	  	12 per 10 elevat a 2
2300000              	23 per 10 elevat a 5
"""
num = 0
cont = 0
res = 0
a = True

num = int (input(("Introduzca número\n")))

while (a):
    if (num%10==0):
        while (num%10==0):
            res = num/10
            cont = cont + 1
            num = res      
        print (res, "por 10 elevado a", cont)
        a = False
    else:
        print("No es multiple de 10.")
        num = int (input("Introduzca número:\n"))