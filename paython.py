print("Software de Inicio")

def menu():
    opcionesIniciales = '''
    *****************************
    *  1- Inicie sesion         *
    *  2- Ingrese contraseña    *
    *  3- Salir                 *
    *****************************    
    '''
    print(opcionesIniciales)
    opcion = int(input("Ingrese la opcion:" ))
    return opcion

while True:
    menu()