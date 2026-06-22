





#retornar la opcion del menu elegido por el usuario
def ingresar_opcion():
    while True
        try:
            op = int(input("Seleccione una opccion: "))
            if op < 1 or op > 6:
                raise ValueError
            else:
                return op
        except ValueError:
            print("Debe ingresar un numero del 1 al 6")
#opccion 1 
#funcion para agregar 
def agregar_reserva(lista_r):
    nombre_completo = input("Ingrese su nombre completo del huesped: ")
    correcto = validar_huesped(nombre_completo)
    if not correcto:
        print("El nombre no puede estar vacío")
        return

    numero_habitacion = input("Ingrese el numero de habitaciones a resrvar: ")
    correcto = validar_habitacion(numero_habitacion)
    if not correcto:
        print("La habitacion debe se un numero entre 1 y 200")

    cant_noches = input("Ingrese la cantidad de noches a hospedarse: ")
    correcto = validar_noches(cant_noches)
    if not correcto:
        print("La cantidad de noches debe ser mayor a cero")
        return

    #agregamos al diccionario
    reserva = {
        "huesped": nombre_completo.strip().upper(),
        "habitacion": int(numero_habitacion), 
        "noches": int(cant_noches),
        "confirmada": False
    }
    lista_r.append(reserva)
    print("Reserva agregada correctamente")

#opcion 2
def buscar_reserva(lista_r, huesped):
    #recorrer la lista
    for x in range(len(lista_r)):
        #verificar si existe dentro
        if huesped == lista_r[x]["huesped0"]:
            return x
        
    return -1 

#opcion 4
def confirmar_reservas(lista_r):
    for i in lista_r:
        if i["noches"] >= 2:
            i["confirmada"] = True
        else:
            i["confirmada"] = False 
#opcion 5
def mostrar_reservas(lista_r):
    print("------Lista de reservas------")
    for i in lista_r:
        print(f"Huesped: {i["huesped"]}")
        print(f"habitacion: {i["habitacion"]}")
        print(f"noches: {i["noches"]}")
        if i["confirmada"]:
            print("Estado: CONFIRMADA")
        else: 
            print(f"estado: PENDIENTE")
        print("============================")



#funciones de validaciones
def validar_huesped(nombre):
    retur nombre.strip().upper() != ""
def validar_habitacion(hab):

    if hab.isdigit():
        validar = int(hab)
        return validar >= 1 and validar <= 200
    return False

def validar_noches(noches):
    if noches.isdigit():
        validar = int(noches)
        return validar > 0
    return False 

#codigo principal 