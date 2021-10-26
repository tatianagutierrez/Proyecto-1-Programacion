def expreRegulares():
    print("Punto 1")
    print("^(LV|LQ)-(\D{3}|\D{1,2}\d+) \n")

    print("Punto 2\n")
    #resolucion

def recursion():
    print("Punto 1\n")
    #resolucion

    print("Punto 2\n")
    #resolucion

    print("Punto 3\n")
    #resolucion

    print("Punto 4\n")
    #resolucion

def colecciones():
    print("Punto 1\n")
    #resolucion

    print("Punto 2\n")
    #resolucion

def intercambioDatos():
    print("Punto 1\n")
    #resolucion

    print("Punto 2\n")
    #resolucion

print("MENU DEL PROGRAMA")
print("---------------------------")
menu = {1: "Expresiones regulares", 2: "Recursion", 3: "Colecciones", 4: "Formato de intercambios de datos", 0: "Salir"}

# Este while pretende simular un switch case
while True: 
    # Se imprime el menu
    opcionKey = menu.keys()
    for i in opcionKey:
        print("[", i, "]", menu[i])

    opcion = int(input("Que ejercicio desea ver?: "))
    if opcion == 1:
        expreRegulares()
    elif opcion == 2:
        recursion()
    elif opcion == 3:
        colecciones()
    elif opcion == 4:
        intercambioDatos()
    elif opcion == 0:
        break
    else:
        print("Error. La opcion es incorrecta. Intentelo nuevamente\n")

print("\nPrograma finalizado")

    
