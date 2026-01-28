def calcular_comision():
    total_ventas = 0
    total_comisiones = 0

    while True:
        cedula = int(input("Ingrese cédula (o -1 para terminar): "))
        if cedula == -1:
            break

        nombre = input("Ingrese nombre: ")
        tipo = int(input("Tipo de vendedor (1: Puerta a Puerta, 2: Telemercadeo, 3: Ejecutivo de ventas): "))
        ventas = float(input("Valor de ventas del mes: "))

        if tipo == 1:
            porcentaje = 0.20
        elif tipo == 2:
            porcentaje = 0.15
        elif tipo == 3:
            porcentaje = 0.25
        else:
            print("Tipo inválido")
            continue

        comision = ventas * porcentaje

        print("Vendedor:", nombre)
        print("Comisión a pagar: $", comision)
        print("---------------------------")

        total_ventas += ventas
        total_comisiones += comision

    print("Total ventas del mes: $", total_ventas)
    print("Total comisiones a pagar: $", total_comisiones)


calcular_comision()
    total_ventas = 0
    total_comisiones = 0

    while True:
        cedula = int(input("Ingrese cédula (o -1 para terminar): "))
        if cedula == -1:
            break

        nombre = input("Ingrese nombre: ")
        tipo = int(input("Tipo de vendedor (1: Puerta a Puerta, 2: Telemercadeo, 3: Ejecutivo de ventas): "))
        ventas = float(input("Valor de ventas del mes: "))

        if tipo == 1:
            porcentaje = 0.20
        elif tipo == 2:
            porcentaje = 0.15
        elif tipo == 3:
            porcentaje = 0.25
        else:
            print("Tipo inválido")
            continue

        comision = ventas * porcentaje

        print("Vendedor:", nombre)
        print("Comisión a pagar: $", comision)
        print("---------------------------")

        total_ventas += ventas
        total_comisiones += comision

    print("Total ventas del mes: $", total_ventas)
    print("Total comisiones a pagar: $", total_comisiones)
def calcular_comision():
    total_ventas = 0
    total_comisiones = 0

    while True:
        cedula = int(input("Ingrese cédula (o -1 para terminar): "))
        if cedula == -1:
            break

        nombre = input("Ingrese nombre: ")
        tipo = int(input("Tipo de vendedor (1: Puerta a Puerta, 2: Telemercadeo, 3: Ejecutivo de ventas): "))
        ventas = float(input("Valor de ventas del mes: "))

        if tipo == 1:
            porcentaje = 0.20
        elif tipo == 2:
            porcentaje = 0.15
        elif tipo == 3:
            porcentaje = 0.25
        else:
            print("Tipo inválido")
            continue

        comision = ventas * porcentaje

        print("Vendedor:", nombre)
        print("Comisión a pagar: $", comision)
        print("---------------------------")

        total_ventas += ventas
        total_comisiones += comision

    print("Total ventas del mes: $", total_ventas)
    print("Total comisiones a pagar: $", total_comisiones)


calcular_comision()
