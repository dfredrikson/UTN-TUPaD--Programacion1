import math

radio_circulo = int(input("Dime cuál es el rádio del círculo que quieres calcular: "))
area = math.pi * (radio_circulo**2)
perimetro = 2 * math.pi * radio_circulo

print(f"El área del círculo con radio {radio_circulo} es de {area}, y su perímetro es {perimetro}")