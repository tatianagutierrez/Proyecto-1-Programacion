def expreRegulares():
    print("Punto 1")
    print("^(LV|LQ)-(\D{3}|\D{1,2}\d+) \n")

    print("Punto 2\n")
    # resolver: no se imprime bien por tener caracteres especiales.
    # nota: tal vez haya que considerar los casos de numeros negativos.
    print("\b(1900|1[1-8]\d{2}|\d{1,3})\b")

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
    
    print("map(): Recibe como parametro una funcion que es aplicada a los elementos de su segundo parametro, una coleccion.")
    print("Ej: Convertir la primera letra en mayuscula de cada elemento perteneciente a una lista.\n")

    print("filter(): Filtra los elementos de una coleccion. La funcion dada sirve como criterio para realizar esta operacion y devuelve un booleano. Los elementos que pasen este filtro seran agregados a una nueva coleccion.")
    print("Ej: Dada una lista de numeros enteros, solo queremos obtener aquellos que sean negativos.\n")

    print("reduce(): Permite reducir los elementos de una coleccion, devolviendo un solo valor. La funcion que le pasamos suele ser una funcion acumulativa y el retorno, su resultado. ")
    print("Ej: Dada una lista que contenga todas las notas finales de los alumnos, obtener el promedio.")

    #Faltan los diagramas

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

    
