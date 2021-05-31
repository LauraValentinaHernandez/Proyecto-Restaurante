'''
Restaurante Ean
'''
import datetime
from typing import Iterator

# Obtener el día actual lunes 0 y domingo 6 en ese rango
dia = datetime.date.today().weekday()
#Reservaciones disponibles de lunes a domingo
reservaciones = [80,100,80,100,80,100,100]
# Menu por día
menus = [["Hamburguesa","Perro caliente","Sandwich"],
         ["Salchipapa", "Burritos"],
         ["Burritos","Hamburguesa","Perro caliente"],
         ["Hamburguesa","Perro caliente","Sandwich"],
         ["Salchipapa", "Burritos"],
         ["Burritos","Hamburguesa","Perro caliente"],
         ["Hamburguesa","Perro caliente","Sandwich"]]
plus = ["Papa francesa","Aro de cebolla","Nugguets"]
bebidas = ["Gaseosa","Jugo","Leche"]
inventario = [["Hamburguesa 🍔",100,8000],
              ["Perro caliente🌭",100, 9000],
              ["Sandwich 🥪",100, 5000],
              ["Burritos 🌯",100, 10000],
              ["Papa francesa 🍟",100, 10000],
              ["Aro de ceboll 🍟a",100, 7000],
              ["Nuggue 🍟🍟",100, 4000]]
clientes = []
empleados = []
  # Menu
while True:
    print("\n========== Menu ==========")
    print("[1] Ingresar Cliente 🧍🧍‍♀️")
    print("[2] Ingresar Empleado 🚶")
    print("[3] Mostrar clientes y empleados 👨‍👨‍👦‍👦")
    print("[4] Pedir orden del dia 🍽🍔🍕🍟🌭")
    print("[5] Pedir orden personalizada 🥪🧀")
    print("[6] Inventario✅ ")
    print("[0] Salir")
    opcion = input("Opcion: ")

    if opcion == "1":
        temp = []
        temp.append(input("Ingrese el nombre del cliente: "))
        temp.append(input("Ingrese la cedula: "))
        clientes.append(temp)
    
    if opcion == "2":
        temp = []
        temp.append(input("Ingrese el nombre del empleado: "))
        temp.append(input("Ingrese la cedula: "))
        empleados.append(temp)

    if opcion == "3":
        print("********** Clientes ***********")
        for i in clientes:
            print(i[1]," ",i[0])
        
        print("********** Empleados ***********")
        for i in clientes:
            print(i[1]," ",i[0])

    if opcion == "4":
        factura= []

# Validar ingreso del cliente
        existe = False
        cedula = input("Ingrese la cedula del cliente: ")
        for i in clientes:
            if i[1] == cedula:
                existe = True
                factura.append(i[0])
        if existe == False:
            factura.append("Desconocido")

        # Ingresar pedido
        detalles = []
        while True:
            print("********* Menu del dia *********")
            i = 1
            lista = []
            for item in menus[dia]:
                lista.append(item)
                for j in inventario:
                    if j[0] == item:
                        print(i," ",item,"............",j[2])
                i += 1
            for item in plus:
                lista.append(item)
                for j in inventario:
                    if j[0] == item:
                        print(i," ",item,"............",j[2])
                i += 1
            indice = int(input("Escoja el indice del producto(0 para finalizar): ")) - 1
            if indice == -1:
                break
            
            for j in range(len(inventario)):
                if lista[indice] == inventario[j][0]:
                    detalles.append([inventario[j][0],inventario[j][2]])
                    inventario[j][1] -= 1
        factura.append(detalles)
        factura.append(0)
        pregunta = input("Desea aplicar el descuento de afiliados (si/no): ")
        print("********** Factura ***********")
        print("Cliente:",factura[0])
        for i in factura[1]:
            print(i[0],"...........",i[1])
            factura[2] += i[1]
        if pregunta == "si":
            print("Subtotal = ",factura[2])
            print("Descuento = ",(factura[2]*0.1))
            print("Total = ",(factura[2] - (factura[2]*0.1)))
        else:
            print("Subtotal = ",factura[2])
            print("Descuento = 0.0")
            print("Total = ",factura[2])

    if opcion == "5":
        factura= []
        # Validar ingreso del cliente
        existe = False
        cedula = input("Ingrese la cedula del cliente: ")
        for i in clientes:
            if i[1] == cedula:
                existe = True
                factura.append(i[0])
        if existe == False:
            factura.append("Desconocido")
        # Ingresar pedido
        detalles = []
        while True:
            print("********* Menu del dia *********")
            i = 1
            for j in inventario:
                print(i," ",j[0],"............",j[2])
                i += 1
            indice = int(input("Escoja el indice del producto(0 para finalizar): ")) - 1
            if indice == -1:
                break

            detalles.append([inventario[indice][0],inventario[indice][2]])
            inventario[indice][1] -= 1
        factura.append(detalles)
        factura.append(0)
        pregunta = input("Desea aplicar el descuento de afiliados (si/no): ")
        print("********** Factura ***********")
        print("Cliente:",factura[0])
        for i in factura[1]:
            print(i[0],"...........",i[1])
            factura[2] += i[1]
        if pregunta == "si":
            print("Subtotal = ",factura[2])
            print("Descuento = ",(factura[2]*0.1))
            print("Total = ",(factura[2] - (factura[2]*0.1)))
        else:
            print("Subtotal = ",factura[2])
            print("Descuento = 0.0")
            print("Total = ",factura[2])

    if opcion == "6":
        print("******** Inventario **********")
        for item in inventario:
            print(item[0]," ",item[1])

    # Salir
    if opcion == "0":
        break
    
