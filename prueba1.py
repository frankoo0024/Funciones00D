#funciones
#validaciones
def validar_nombre(nombre):
    #una funcion de python que verifica los espacios al inicio o al final de un string y se queda vacia devuleve una False
    return nombre.strip() != "" #retorna true si es valido - False si es invalido
def validar_especie(especie):
    #verificar que es perro, gato o ave solamente (sin diferenciar mayusculas o minusculas)
    especies_validas = ["perro",
                    "gato","ave"]
    return especie.strip().lower() in especies_validas
def validar_edad(edad):
    #que sean numeros y mayor a cero
    #isdigit() --> revisa que el string contenga solo digitos (no negativo, no decimal)
    return edad.isdigit() and int(edad) > 0


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
#Funcion para agregar una mascota nueva
def agregar_mascota(lista):
    nombre = input("Ingresa el nombre de la mascota: ")
    #llamar la funcion que valida el nombre para mostrar el mensaje 
    correcto = validar_nombre(nombre)
    if not correcto:
        print("El nombre no puede estar vacio")
        return

    especie = input("Ingrese la especie de la mascota (perro, gato o ave): ")
    correcto = validar_especie(especie)
        print("La especie solo puede ser perro, gato o ave")
        return

    edad = input("Ingrese la edad de la mascota: ")
    correcto = validar_edad(edad)
        print("La edad ingresada debe ser un número entero mayor a cero")
        return
    #aqui agrego el diccionario
    mascota = {
        "nombre": nombre.strip(),
        "especie": especie.strip().lower(),
        "edad": int(edad),
        "vacunada": False

    }
    #agrego a la lista
    lista.append(mascota)
    print("Mascota agregada correctamente")

#codigo principal
#declaracion la lista de mascotas
lista_mascotas = []

op = 0
while op != 6:
    mostra_menu()
    op = ingresar_opcion()

    if op ==1:  
        agregar_mascota(lista_mascotas)    
    elif op == 2:
        print()
    elif op ==  3:
        print()
    elif op ==  4:
        print()
    elif op ==  5:
        print()
    elif op ==  6:
        print("Gracias por usar el sistema")