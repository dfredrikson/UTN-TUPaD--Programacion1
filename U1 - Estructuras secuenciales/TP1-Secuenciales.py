
#//////////////////////////////Ejercicio 1
print("Hola Mundo!")

#//////////////////////////////Ejercicio 2
nombre = input("Hola! dime tu nombre:")
print(f"Tu nombre es {nombre}")

#//////////////////////////////Ejercicio 3
nombre = input("Dime tu nombre: ")
apellido = input("Ahora dime tu apellido: ")
edad = input("Tu edad: ")
residencia = input("¿Cuál es tu lugar de residencia?: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#//////////////////////////////Ejercicio 4
import math

radio_circulo = int(input("Dime cuál es el rádio del círculo que quieres calcular: "))
area = math.pi * (radio_circulo**2)
perimetro = 2 * math.pi * radio_circulo

print(f"El área del círculo con radio {radio_circulo} es de {area}, y su perímetro es {perimetro}")

#//////////////////////////////Ejercicio 5
segundos = int(input("Dime la cantidad de segundos que quieres calcular: "))
calculo_cant_horas = segundos / 60 / 60

print(f"La cantidad de {segundos} segundos equivale a {calculo_cant_horas} horas")

#//////////////////////////////Ejercicio 6
numero = int(input("Dime un número y te muestro su tabla de multiplicar: "))
print(f"La tabla de multiplicar hasta el 10 del número {numero} es: ")
print(numero*1, numero*2, numero*3, numero*4, numero*5, numero*6, numero*7, numero*8, numero*9, numero*10)


#//////////////////////////////Ejercicio 7
print("Voy a calcular la suma, resta, multiplicación y división de 2 números que elijas.")

numero1 = int(input("Dime el primer número entero diferente de 0: "))
numero2 = int(input("Dime el otro número entero diferente de 0: "))
suma = numero1 + numero2
resta = numero1 - numero2
multiplicacion = numero1 * numero2
division = numero1 / numero2

print(f"Los resultados son los siguientes: \
      {numero1} + {numero2} = {suma} \
      {numero1} - {numero2} = {resta} \
      {numero1} x {numero2} = {multiplicacion} \
      {numero1} / {numero2} = {division}")


#//////////////////////////////Ejercicio 8
altura = float(input("Dime tu altura para calcular el Indice de masa corporal: "))
peso = float(input("Ahora tu peso: "))
imc = peso / (altura**2)

print(f"Tu Índice de masa corporal es de {imc}")

#//////////////////////////////Ejercicio 9
print("Vamos a convertir grados Celsius en Fahrenheit!")
celsius = float(input("Dime la cantidad de grados Celsius que quieres convertir: "))
Fahrenheit = 9/5 * celsius + 32

print(f"{celsius} grados Celcius equivalen a {Fahrenheit} grados Fahrenheit")

#//////////////////////////////Ejercicio 10
print("Vamos a calcular el promedio de 3 números que elijas")

numero1 = float(input("Elije el primer número: "))
numero2 = float(input("Ahora el segundo número: "))
numero3 = float(input("Y por último el tercer número: "))

promedio = (numero1+numero2+numero3) / 3

print(f"El promedio de los números {numero1}, {numero2} y {numero3} es {promedio}")
