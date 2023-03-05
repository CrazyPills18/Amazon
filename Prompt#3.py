"""
Temas de interés de un cliente
Preguntar cual de estos 6 temas es del interés del cliente
-Fitness
-Musica y arte
-Libros
-Comida
-Tecnología
-Jardinería
Posteriormente realizar 3 preguntas en base a su elección e imprimir al final un agradecimiento por la paciencia
junto a su nombre y el mensaje "Te recomendaremos más sobre {tema}"
"""
print('\033[1m'"<=Encuesta sobre tus temas de interés=>\n"'\033[0m')
nom=input("Ingrése su nombre de usuario\n=")
sel=input(("Elija la opción de su interés\n\n"'\033[92m'+'\033[1m'
           "a)"'\033[0m'"Fitness\n"'\033[92m'+'\033[1m'
           "b)"'\033[0m'"Música y arte\n"'\033[92m'+'\033[1m'
           "c)"'\033[0m'"Libros\n"'\033[92m'+'\033[1m'
           "d)"'\033[0m'"Jardinería\n"'\033[92m'+'\033[1m'
           "e)"'\033[0m'"Tecnología\n"'\033[92m'+'\033[1m'
           "f)"'\033[0m'"Comida\n"'\033[92m'+'\033[1m'
           '\033[0m'"\n(Escriba la "'\033[4m'"letra"'\033[0m'" que aparece en "'\033[92m'"verde"'\033[0m'" para seleccionar la opción deseada.)\n="))
if sel=="a":
    sel=('\033[96m'"Fitness"'\033[0m')
    print(f"Ha seleccionado la opción {sel}.\nA continuación se le harán 3 preguntas con respecto a su tema de interés.\n")
    q1=input("Pregunta#1\n"
             "¿Posee algúna rutina de ejercicios?\n=")
    q2=input("\nPregunta#2\n"
             "¿Utiliza suplementos para aumentar su masa muscular?\n=")
    q3=input("\nPregunta#3\n"
             "¿Ha recibido asesoramiento personal?\n=")
    print(f"\n¡Muy bien {nom}!\n"
          f"Gracias por responder las preguntas brindadas. Te recomendaremos más sobre {sel}")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
elif sel=="b":
    sel=('\033[96m'"Música y arte"'\033[0m')
    print(f"Ha seleccionado la opción {sel}.\nA continuación se le harán 3 preguntas con respecto a su tema de interés.\n")
    q1=input("Pregunta#1\n"
             "¿Cuál es tu artista, banda o compositor músical favorito?\n=")
    q2=input("\nPregunta#2\n"
             "¿Cuál tipo de arte es tu preferido?\n=")
    q3=input("\nPregunta#3\n"
             "¿Tienes algúna habilidad relacionada al arte?\n=")
    print(f"\n¡Muy bien {nom}!\n"
          f"Gracias por responder las preguntas brindadas. Te recomendaremos más sobre {sel}")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
elif sel=="c":
    sel=('\033[96m'"Libros"'\033[0m')
    print(f"Ha seleccionado la opción {sel}.\nA continuación se le harán 3 preguntas con respecto a su tema de interés.\n")
    q1=input("Pregunta#1\n"
             "¿Quién es tu autor preferido?\n=")
    q2=input("\nPregunta#2\n"
             "¿Cuál estu saga de libros favorita?\n=")
    q3=input("\nPregunta#3\n"
             "¿Cuál es tu género favorito?\n=")
    print(f"\n¡Muy bien {nom}!\n"
          f"Gracias por responder las preguntas brindadas. Te recomendaremos más sobre {sel}")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
elif sel=="d":
    sel=('\033[96m'"Jardinería"'\033[0m')
    print(f"Ha seleccionado la opción {sel}.\nA continuación se le harán 3 preguntas con respecto a su tema de interés.\n")
    q1=input("Pregunta#1\n"
             "¿Posee un jardín propio?\n=")
    q2=input("\nPregunta#2\n"
             "¿Cuál elemento natural es su preferido?\n=")
    q3=input("\nPregunta#3\n"
             "¿Qué tipo de plantas posee en su hogar?\n=")
    print(f"\n¡Muy bien {nom}!\n"
          f"Gracias por responder las preguntas brindadas. Te recomendaremos más sobre {sel}")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
elif sel=="e":
    sel=('\033[96m'"Tecnología"'\033[0m')
    print(f"Ha seleccionado la opción {sel}.\nA continuación se le harán 3 preguntas con respecto a su tema de interés.\n")
    q1=input("Pregunta#1\n"
             "¿Le gustan los videojuegos?\n=")
    q2=input("\nPregunta#2\n"
             "¿Posee equipo de alta gama?\n=")
    q3=input("\nPregunta#3\n"
             "¿Que ramas de la tecnología le llaman la atención?\n=")
    print(f"\n¡Muy bien {nom}!\n"
          f"Gracias por responder las preguntas brindadas. Te recomendaremos más sobre {sel}")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
elif sel=="f":
    sel=('\033[96m'"Comida"'\033[0m')
    print(f"Ha seleccionado la opción {sel}.\nA continuación se le harán 3 preguntas con respecto a su tema de interés.\n")
    q1=input("Pregunta#1\n"
             "¿Cuál es su platillo o comida favorito?\n=")
    q2=input("\nPregunta#2\n"
             "¿Prefiere la comida de su país o extranjera?\n=")
    q3=input("\nPregunta#3\n"
             "Mencione algún alimento o alimentos que no le guste o no pueda comer\n=")
    print(f"\n¡Muy bien {nom}!\n"
          f"Gracias por responder las preguntas brindadas. Te recomendaremos más sobre {sel}")
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
else:
    print('\033[91m'"¡Ingrese una opción válida!"'\033[0m')
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")