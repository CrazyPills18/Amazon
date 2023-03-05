"""
Descuentos dependiendo del total de la compra
►+50$ = 5%
►+100$ = 10%
►+200$ = 14%
"""
x=0
can=int(input("Introduzca el costo total de los articulos que compró el cliente\n="))
if can >=50 and can <100:
    print("Se le aplicará un descuento del 5% en esta compra.")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
elif can >=100 and can <200:
    print("Se le aplicará un descuento del 10% en esta compra.")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
elif can >=200:
    print("Se le aplicará un descuento del 14% en esta compra.")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
else:
    print('\033[91m'"¡Ingrese una opción válida!"'\033[0m')
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")