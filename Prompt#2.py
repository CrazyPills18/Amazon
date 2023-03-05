"""
Realizar una encuesta a los clientes sobre su método favorito de entrega para, de este modo, establecerlo como su método de entrega predeterminado.
Las 4 opciones son:
a)Entrega a domicilio por un camión de entregas
    ►Camión exprés
    ►Camión estándar
b)Entrega vía dron
    ►Dron de carga pesada (Tarda más en entregar, pero puede llevar más peso)
    ►Dron ligero (Tarda menos en entregar, pero su capacidad de peso es más reducida)
c)Entrega a un punto específico
    ►Casillero específico
    ►Tienda con servicios de entrega de Amazon
d)Entrega internacional
    ►Aduanas del país y posteriormente a la dirección asignada
"""
print('\033[1m'"<=Encuesta para determinar su método de entrega predeterminado en Amazon=>\n"'\033[0m')
res=input(("De las siguientes opciones ¿Cuál se ajusta mejor a su forma deseada de recibir los productos que adquiera?\n"'\033[92m'+'\033[1m'"a)"'\033[0m'"Entrega a domicilio por un camión de entregas\n"'\033[92m'+'\033[1m'"b)"'\033[0m'"Entrega vía Dron\n"'\033[92m'+'\033[1m'"c)"'\033[0m'"Entrega a un punto específico\n"'\033[92m'+'\033[1m'"d)"'\033[0m'"Entrega internacional\n\n(Escriba la "'\033[4m'"letra"'\033[0m'" que aparece en "'\033[92m'"verde"'\033[0m'" para seleccionar la opción deseada.)\n="))
if res=="a":
    sel=int(input('\033[1m'"\nSeleccionó \"Entrega a domicilio por camión de entregas\""'\033[0m'"\n¿Cuál de las siguientes 2 opciones se ajusta a sus preferencias?\n\n"'\033[92m'+'\033[1m'"1)"'\033[0m'"Camión exprés\n"'\033[92m'+'\033[1m'"2)"'\033[0m'"Camión estándar\n\n(Escriba el "'\033[4m'"número"'\033[0m'" que aparece en"'\033[92m'" verde "'\033[0m'"para seleccionar la opción deseada.)\n="))
    if sel==1:
        sel="\"Camión exprés\"."
        print("Ha elegido la opción",sel,"Esta será su opción asignada para todas sus entregas.\n¡Gracias por utilizar nuestros servicios!")
        input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
    elif sel==2:
        sel="\"Camión estándar\"."
        print("Ha elegido la opción",sel,"Esta será su opción asignada para todas sus entregas.\n¡Gracias por utilizar nuestros servicios!")
        input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
elif res=="b":
    sel=int(input('\033[1m'"\nSeleccionó \"Entrega vía dron\""'\033[0m'"\n¿Cuál de las siguientes 2 opciones se ajusta a sus preferencias?\n\n"'\033[92m'+'\033[1m'"1)"'\033[0m'"Dron de carga pesada (Tarda más en entregar, pero puede llevar más peso)\n"'\033[92m'+'\033[1m'"2)"'\033[0m'"Dron ligero (Tarda menos en entregar, pero su capacidad de peso es más reducida)\n\n(Escriba el "'\033[4m'"número"'\033[0m'" que aparece en"'\033[92m'" verde "'\033[0m'"para seleccionar la opción deseada.)\n="))
    if sel==1:
        sel="\"Dron de carga pesada\"."
        print("Ha elegido la opción",sel,"Esta será su opción asignada para todas sus entregas.\n¡Gracias por utilizar nuestros servicios!")
        input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
    elif sel==2:
        sel="\"Dron ligero\"."
        print("Ha elegido la opción",sel,"Esta será su opción asignada para todas sus entregas.\n¡Gracias por utilizar nuestros servicios!")
        input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
    print("")
elif res=="c":
    sel=int(input('\033[1m'"\nSeleccionó \"Entrega a un punto específico\""'\033[0m'"\n¿Cuál de las siguientes 2 opciones se ajusta a sus preferencias?\n\n"'\033[92m'+'\033[1m'"1)"'\033[0m'"Casillero específico\n"'\033[92m'+'\033[1m'"2)"'\033[0m'"Tienda con servicios de entrega de Amazon\n\n(Escriba el "'\033[4m'"número"'\033[0m'" que aparece en"'\033[92m'" verde "'\033[0m'"para seleccionar la opción deseada.)\n="))
    if sel==1:
        sel="\"Casillero específico\"."
        print("Ha elegido la opción",sel,"Esta será su opción asignada para todas sus entregas.\n¡Gracias por utilizar nuestros servicios!")
        input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
    elif sel==2:
        sel="\"Tienda con servicios de entrega de Amazon\"."
        print("Ha elegido la opción",sel,"Esta será su opción asignada para todas sus entregas.\n¡Gracias por utilizar nuestros servicios!")
        input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
elif res=="d":
    sel=int(input('\033[1m'"\nSeleccionó \"Entrega internacional\""'\033[0m'"\nEsta opción solo cuenta con una forma de entrega\n\n"'\033[92m'+'\033[1m'"1)"'\033[0m'"Aduana del país y posteriormente a la dirección asignada\n\n(Escriba el "'\033[4m'"número"'\033[0m'" que aparece en"'\033[92m'" verde "'\033[0m'"para seleccionar la opción deseada.)\n="))
    sel="\"Aduanas del país y posteriormente a la dirección asignada\"."
    print("Ha elegido la opción",sel,"Esta será su opción asignada para todas sus entregas.\n¡Gracias por utilizar nuestros servicios!")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
else:
    print('\033[91m'"¡Ingrese una opción válida!"'\033[0m')
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")