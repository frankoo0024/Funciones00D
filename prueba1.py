#funciones
def mostra_menu():
    print("---------Menú principal-----------")
    print("1.- Agregar mascota ")
    print("2.- Buscar mascota ")
    print("3.- Eliminar mascota ")
    print("4.- Marcar como Vacunada ")
    print("5.- Mostrar Mascotas")
    print("6.- Salir ")
    print("--------------------")

def ingresar_opcion():
    while True:
        try:
            opcion = int(input("Seleccione una opcion: "))
            if opcion < 1 or opcion > 6:
                print("Debe seleccionar una opccion del 1 al 6")
            else:
                break
        except ValueError:
            print("Debe ingresar un número")
    return opcion
#codigo principal
#declaracion la lista de mascotas
lista_mascotas = []

mostra_menu()
op = ingresar_opcion()
