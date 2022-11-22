"""
Un programa té les següents entrades:
un any determinat ( p.ex.2006 )
el dia de la setmana en que va començar 
( en format numèric, 1 pel dilluns, 2 
per dimarts, etc. ) 
La sortida del programa serà un calendari 
per pantalla que mostrarà una capçalera 
per a cada mes, i separarà els dies per 
setmanes. Vegeu-ne un exemple a continuació 
per l’any 2006, que ha començat en dilluns.

"""
#tener en cuenta duracion año, si bisiesto o no, dias mes
año = 0
dia_mes = 0
dia_semana = 0
dias_mes = 0
mes = 1
mes_l = ""
dia_sl = ""
semana = 0
#--------------------
año = int(input("int. año:\n"))
dia_semana = int(input("int dia de la semana 1 al 7:\n"))
#------------------------

for mes in range(1,13):
    if mes == 1: 
        mes_l="Gener"
        dias_mes = 31
    elif mes == 2:
        mes_l="Febrer"
        dias_mes = 28
        if ((año % 4 == 0 and año % 100 != 0) or año % 400 == 0) : 
            dias_mes = 29
    elif mes == 3:
        mes_l="Març"
        dias_mes = 31
    elif mes == 4:
        mes_l="Abril"
        dias_mes = 30
    elif mes == 5:
        mes_l="Maig"
        dias_mes = 31
    elif mes == 6:
        mes_l="Juny"
        dias_mes = 30
    elif mes == 7:
        mes_l="Juliol"
        dias_mes = 31
    elif mes == 8:
        mes_l="Agost"
        dias_mes = 31
    elif mes == 9:
        mes_l="Septembre"
        dias_mes = 30
    elif mes == 10:
        mes_l="Octubre"
        dias_mes = 31
    elif mes == 11:
        mes_l="Novembre"
        dias_mes = 30
    elif mes == 12:
        mes_l="Desembre"
        dias_mes = 31

    print("*******", mes_l,"**********")
    for i in range(1, dias_mes + 1 ):
        if dia_semana == 1:
            dia_sl = "Dilluns"
        elif dia_semana == 2:
            dia_sl = "Dimarts"
        elif dia_semana == 3:
            dia_sl = "Dimecres"
        elif dia_semana == 4:
            dia_sl = "Dijous"
        elif dia_semana == 5:
            dia_sl = "Divendres"
        elif dia_semana == 6:
            dia_sl = "Dissabte"
        elif dia_semana == 7:
            dia_sl = "Diumenge"
        print("Dia", i, dia_sl)
        dia_semana+=1
        if dia_semana == 8:
            dia_semana = 1
        print("***********")
        print("*****************************")
