# Escribir un programa que contenga una función que reciba una lista de palabras y devuelva la más larga. Imprimir por pantalla la palabra resultante.

def largo(lista):
    lista_aux = []
    largo_palabra = 0
    contador = 2
    while contador != 0:
        for i in range(len(lista)):
            palabra = lista[i]
            if len(palabra) >= largo_palabra:
                largo_palabra = len(palabra)
            elif palabra not in lista_aux:
                lista_aux.append(palabra)
            else:
                pass
        contador -= 1
    for i in range(len(lista_aux)):
        palabra = lista_aux[i]
        lista.remove(palabra)
    return lista 

def main():
    palabras = []
    cantidad = int(input("Cuantas palabras desea introducir en la lista? "))
    
    for i in range(cantidad):
        palabra = input("Introduzca una palabra: ")
        palabras.append(palabra)

    seleccionada = largo(palabras)
    if len(seleccionada) > 1:
        print("Las palabras más largas son "+str(seleccionada))
    else:
        print("La palabra más larga es "+str(seleccionada))

if __name__ == '__main__':
    main()