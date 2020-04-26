import binarytree

log = True


# Funcion que tiene el Ejercicio B
def ejercicio_b():
    arbol = binarytree.bst(height=4, is_perfect=False)
    print(arbol, '\n')

    print('El numero de nodos es: ', arbol.size, '\n')


# Funcion que tiene el Ejercicio C
def ejercicio_c():
    arbol = binarytree.bst(height=5, is_perfect=False)
    print(arbol, '\n')

    print('El numero de nodos es: ', arbol.height + 1, '\n')  # Sumamos 1 porque contamos la profundidad desde 1


# Funcion que tiene el Ejercicio D
def ejercicio_d():
    values = (['B', 'U', 'I', 'E', 'R', 'E', 'L', 'N', None, None, 'R', 'N', None, 'B', None,
               'O', 'A', None, None, None, None, 'A', 'O', None, None, 'A', None, None, None,
               None, None, None, 'S', None, None, None, None, None, None, None, None, None,
               None, 'S', None, None, None, None, None, 'O', None, None, None, None, None, None, None])

    raiz = binarytree.build(values)

    print(raiz)


# Funcion principal
def main():
    ejercicio = '0'
    loop = True

    while loop:
        print("\n\n\nElija una de las opciones")
        print("Escriba 1 para el Ejercicio B")
        print("Escriba 2 para el Ejercicio C")
        print("Escriba 3 para el Ejercicio D")
        print("Escriba 0 para finalizar")

        ejercicio = input("Escriba una opcion: ")

        if ejercicio == '1':
            ejercicio_b()
        elif ejercicio == '2':
            ejercicio_c()
        elif ejercicio == '3':
            ejercicio_d()
        elif ejercicio == '0':
            loop = False
            print("Que pase un buen dia.")
        else:
            print("Elija una opcion valida.")


def login():
    global log
    while log == False:
        email = input("Ingrese su email: ")
        contra = input("Ingrese su password: ")
        if (email == '21806108@live.uem.es'):
            if (contra == '1234'):
                print("Acceso concedido")
                log = True
        else:
            print("Email y password invalidos")
            exit()


login()
if log:
    main()
