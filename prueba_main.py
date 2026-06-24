import prueba as p
#codigo pricipal
opcion = 0 
while opcion != 6:
    p.mostrar_menu()
    opcion = 0.ingresar_opcion() 

    if opcion == 1:
        #llamar a la funcion que ingresa nuevas reservas
        p.agregar_reserva(lista_reservas)
    elif opcion == 2:
        #solicitamos al nombre a buscar
        nombre = input("Ingrese el nombre del huesped a buscar: ")
        #llamamos a la funcion encargada de buscar
        pos = p.buscar_reserva(lista_reservas, nombre)
        #validamos que retorna la funcion buscar
        if pos != -1:
            #se encontro el huesped asi que muestro sus datos
            print("========Reserva encontrada=========")
            print(f"Nombre del huesped: {lista_reservas[pos]["huesped"]}")
            print(f"Numero de la habitacion: {lista_reservas[pos]["habitacion"]}")
            print(f"Noches del hospedaje: {lista_reservas[pos]["noches"]}")
            estado = "Confirmado" if lista_reservas[pos]["confirmada"] else "pendiente"
            print(f"Estado: {}")
            print("*********************************")  
        else:
            print(f"El huesped {nombre} no ha sido encontrado")

    elif opcion == 3:
        nombre = input("Ingrese el nombre del huesped a buscar: ")
        #llamamos a la funcion encargada de busacar
        pos = p.buscar_reservas(lista_reservas, nombre)
        if pos != -1:
            lista_reservas.pop(pos)
        else: 
            print(f"El huesped {nombre} no ha sido encontrado")

    elif opcion == 4:
        #llamamos a la funcion que confirma las reservas 
        p.confirmar_reserva(lista_reservas)
    elif opcion == 5:
        p.confirmar_reserva(lista_reservas)
        p.mostrar_reserva(lista_reservas)
    elif opcion == 6:
        print("Gracias por usar el programa, vuelva pronto")