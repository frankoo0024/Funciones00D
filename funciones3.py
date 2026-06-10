def ficha_producto(nombre, precio, stock): 
    print("=================")
    print(f"Nombre del producto: {nombre}")
    print(f"Stock del producto: {stock} ")
    print(f"Precio del producto: {precio} ")
    print("=================")

nombre1 = input("Ingresa el nombre del producto")
while True:
    try:
        stock1 = int(input("Ingrese el stock: "))
        if stock1 < 0:
            print("Debe ser mayor o igual a cero")
        else:
            break
    except ValueError:
            print("Debe ingresar numeros")
while True:
    try:
        precio1 = int(input("Ingrese el stock: "))
        if precio1 < 0:
            print("Debe ser mayor o igual a cero")
        else:
            break
    except ValueError:
            print("Debe ingresar numeros")
        
ficha_producto(nombre1, precio1, stock1)
