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
