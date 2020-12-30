import os
import sys
import time

os.system("cls") # Se inicia el programa con la pantalla limpia.

# Se establecen las posibles entradas validas.
posibles_respuestas_seca = ["levadura seca", "seca"]
posibles_respuestas_fresca = ["levadura fresca", "fresca"]
posibles_respuestas_continuar = ["si", "claro", "por supuesto", "obvio", "obviamente", "yes", "y", "afirmativo", "s", "por supuestisimo"]
condicion = 0 # Se inicializa la condicion del bucle while a 0.

# Funcion encargada de convertir los gramos de levadura a su equivalente en Masa Madre.
def CalculoGramos(gramos_levadura):
    if gramos_levadura in posibles_respuestas_fresca:
        gramos_MM = gramos_levadura*27.5/3
    else:
        gramos_MM = gramos_levadura*27.5    
    return int(gramos_MM)

# Se crea una clase con los valores necesarios para resaltar el resultado en negrita.
class color:
    BOLD = '\033[1m'
    END = '\033[0m'

def SalidaPorPantalla(CalculoGramos, color, respuesta, gramos_levadura):
    os.system("cls")
    print(f"{int(gramos_levadura)} gramos de {respuesta} equivalen a " + color.BOLD + f"{int(CalculoGramos(gramos_levadura))}" + color.END + " gramos de Masa Madre.")
    print("\n")
    continuar = str(input("¿Quiere hacer otra conversión S/N? ").lower())
    if continuar in posibles_respuestas_continuar:
        os.system("cls")
        condicion = 0
        return condicion
    else:
        print("\n")
        print("Gracias por usar la calculadora de Masa Madre.") 
        time.sleep(1)
        sys.exit()
    return 

while condicion == 0: # Bucle while que checkea que la respuesta sea una valida entre las posibles respuestas declaradas al inicio.
    respuesta = str(input("Que desea convertir, ¿levadura seca o fresca? ").lower())
    if respuesta == "seca" or respuesta == "fresca":
        respuesta = f"levadura {respuesta}"
    if respuesta in posibles_respuestas_fresca or respuesta in posibles_respuestas_seca:
        while True: # Bucle que checkea que el valor en gramos es númerico y si es decimal que sea separado por un punto.
            try:
                os.system("cls")
                gramos_levadura = float(input("¿Cuantos gramos (valor númerico) quiere convertir? "))
            except ValueError:
                os.system("cls")
                print(f"Tipo: {respuesta}")
                print("Introduzca un valor númerico, decimales separados por .")
                continue
            if gramos_levadura < 0:
                os.system("cls")
                print(f"Tipo: {respuesta}")
                print("Introduzca un valor númerico positivo")
                continue
            break
        SalidaPorPantalla(CalculoGramos, color, respuesta, gramos_levadura)
    else:
        os.system("cls")
        print(f"'{respuesta}' no es una respuesta válida")
        condicion = 0