"""
Realizar una encuesta sobre la satisfacción de un cliente, que muestre un diferente mensaje junto a: 
-Una promoción si la satisfacción del servicio es alta
-Solo el mensaje si la satisfacción del servicio es media
-Un banco de opiniones si la satisfacción del servicio es baja
"""
class bold_color:
    red='\033[91m'
    yellow='\033[93m'
    green='\033[92m'
    blue='\033[94m'
    purple='\033[95m'
    cyan='\033[96m'
    dark_cyan='\033[36m'
    under_l='\033[4m'
    bold='\033[1m'
    end='\033[0m'
print(bold_color.bold,'<=Encuesta de satisfacción de los servicios de Amazon=>',bold_color.end)
print("\nPara mostrar su satisfacción con respecto a nuestros Servicios\nEscriba un número entre el "'\033[1m'"1 y 5"'\033[0m'". Siendo 1 ",bold_color.red,"\"Completamente insatisfecho\"",bold_color.end,"y 5",bold_color.green,"\"Muy satisfecho\".\n"'\033[0m')
q1=int(input('\033[1m'"¿Cómo calificaría la cálidad de los productos que están a la venta en nuestra página web?\n="'\033[0m'))
q2=int(input('\033[1m'"\n¿Cómo calificaría los tiempos de espera para la entrega de los artículos que haya adquirido de nuestra página web?\n="'\033[0m'))
q3=int(input('\033[1m'"\n¿Cómo calificaría el estado de los artículos al momento de ser entregados?\n="'\033[0m'))
q4=int(input('\033[1m'"\n¿Cómo calificaría el diseño y la distribución del menú de la página web?\n="'\033[0m'))
q5=int(input('\033[1m'"\n¿Cómo calificaría las descripciones que se le proporcionan a los artículos de la página web?\n="'\033[0m'))
if q1>=1 and q1<=5 and q2>=1 and q2<=5 and q3>=1 and q3<=5 and q4>=1 and q4<=5 and q5>=1 and q5<=5:
    tot=q1+q2+q3+q4+q5
    if tot>=5 and tot<=10:
        opi=(input("\nLamentamos que nuestro servicio no haya sido de su agrado.\nPara poder mejorar nuestro servicio, le pedimos que deje una opinión más detallada sobre los aspectos específicos que la empresa podría mejorar\n= "))
        print('\033[1m'"¡Gracias por su contribución!"'\033[0m'"\nHaremos todo lo posible por mejorar nuestros servicios.")
        input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
    elif tot>=11 and tot<=19:
        print('\033[1m'"¡Gracias por su contribución!"'\033[0m'"\nNos ayuda a hacer todo lo posible por mejorar nuestros servicios.")
        input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
    elif tot>=20:
        print('\033[1m'"¡Gracias por su contribución!\n"'\033[0m'"\nPor su alta valoración de nuestros servicios, le otorgamos un cupón de 5% de descuento en cualquier compra que realice proximamente.")
        print('\033[1m'"¡Gracias por preferirnos!"'\033[0m')
        input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
else:
    print(bold_color.red,"\n¡Ingrese los números solicitados!",bold_color.end)
    input("[PRESIONE "'\033[1m'+'\033[4m'+"ENTER"+'\033[0m'" PARA CONTINUAR]")
