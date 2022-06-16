# Escriba un programa que pida dos palabras y diga si riman o no. Si coinciden las últimas tres letras tiene que decir que riman. Si coinciden sólo las últimas dos tiene que decir que riman un poco. Y si no coinciden, decir que no riman. Validar que las palabras tengan al menos tres letras. Nota: Utilizar slices

def rima(palabra1, palabra2):
    if palabra1[-3:-1] == palabra2[-3:-1]:
        print("Ambas palabras riman.")
    elif palabra1[-2:-1] == palabra2[-2:-1]:
        print("Ambas palabras riman un poco.")
    else:
        print("Ambas palabras no riman.")

def main():
    palabra1 = input("Intruduzca una palabra que tenga al menos 3 letras: ").lower()
    palabra2 = input("Introduzca otra palabra que al menos tenga 3 letras: ").lower()

    if len(palabra1) < 3 or len(palabra2) < 3:
        print("Una de las palabras tiene menos de 3 letras.")
    else:
        rima(palabra1, palabra2)

if __name__ == '__main__':
    main()