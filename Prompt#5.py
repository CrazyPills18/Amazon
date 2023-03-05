"""
Elegir entre 3 Tiendas Online
    ►Amazon
    ►Etsy
    ►Aliexpress
Describir cada una.
"""
tienda=input("¿Cuál de estas 3 tiendas online utiliza con más frecuencia?\n"'\033[92m'+'\033[1m'"a)"'\033[0m'"Amazon\n"'\033[92m'+'\033[1m'"b)"'\033[0m'"Etsy\n"'\033[92m'+'\033[1m'"c)"'\033[0m'"Aliexpress\n=")
if tienda == "a":
    tienda="Amazon"
    print(f"Ha seleccionado {tienda}\n{tienda} es una tienda online con sedes fisicas en diferentes países. Poseen un servicio premiun que habilita diferentes beneficios a sus usuarios. Podrás encontrar casi too lo que necesites en su página web.")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
elif tienda == "b":
    tienda="Etsy"
    print(f"Ha seleccionado {tienda}\n{tienda} es una tienda online en la que se podrán encontrar objetos de decoración, ropa, accesorios, objetos de tecnología, etc. Tiene precios accesibles conforme a la calidad.")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
elif tienda == "c":
    tienda="Aliexpress"
    print(f"Ha seleccionado {tienda}\n{tienda} es una tienda online en la que se prioriza la cantidad antes que la calidad tomando como referencia sus precios tan bajo por tantos producto. ")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
else:
    print('\033[91m'"¡Ingrese una opción válida!"'\033[0m')
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")