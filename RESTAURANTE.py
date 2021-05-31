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
inventario = [["Hamburguesa",100,8000],
              ["Perro caliente",100, 7500],
              ["Sandwich",100, 5000],
              ["Burritos",100, 10000],
              ["Papa francesa",100, 6000],
              ["Aro de cebolla",100, 7000],
              ["Nugguets",100, 4000]]
clientes = []
empleados = []
