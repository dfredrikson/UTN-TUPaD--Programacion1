# Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
# deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad_user = int(input("Ingresa tu edad: "))

if edad_user > 18:
    print("Es mayor de edad")
else:
    print("No eres mayor de edad")


# Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
# mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
# mensaje “Desaprobado”.#

nota_user = float(input("Coloca la nota: "))

if nota_user >= 6:
    print("Aprobado")
else:
    print("Desaprobado")


# Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
# número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
# contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
# operador de módulo (%) en Python para evaluar si un número es par o impar.

num_par = int(input("Ingresa un número par: "))

if (num_par % 2 == 0):
    print("Ha ingresado un número par")
else:
    print("Por favor, ingresa un número par")

# Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
# siguientes categorías pertenece:
# • Niño/a: menor de 12 años.
# • Adolescente: mayor o igual que 12 años y menor que 18 años.
# • Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
# • Adulto/a: mayor o igual que 30 años.

edad_user = int(input("Indica tu edad:"))

if edad_user < 12:
    print("Pertenece a la categoría Niño/a")
elif edad_user >= 12 and edad_user < 18:
    print("Pertenece a la categoria Adolescente")
elif edad_user >= 18 and edad_user < 30:
    print("Pertenece a la categoria Adulto/a joven")
else:
    print("Pertenece a la categoría Adulto/a")

# Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
# (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
# pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
# pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres".
# Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos
# que tiene un iterable tal como una lista o un string.

password = input("Ingresa tu contraseña. Debe contener entre 8 y 14 caracteres: ")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Ingrese una contraseña de entre 8 a 14 caracteres")

# Escribir un programa que solicite al usuario el consumo mensual de energía eléctrica en
# kilovatios (kWh) e indique la categoría del consumo según el siguiente criterio:
# • Menor que 150 kWh: “Consumo bajo”.
# • Entre 150 y 300 kWh (inclusive): “Consumo medio”.
# • Mayor que 300 kWh: “Consumo alto”.
# Además, si el consumo supera los 500 kWh, mostrar un mensaje adicional que diga:
# “Considere medidas de ahorro energético”.
# El programa debe imprimir por pantalla la categoría correspondiente.

consm_mensual_energia = int(input("Indique el consumo mensual de energía eléctrica en kilovatios: "))

if consm_mensual_energia < 150:
    print("Su consumo es bajo")
elif consm_mensual_energia >= 150 and consm_mensual_energia <= 300:
    print("Su consumo es medio")
elif consm_mensual_energia > 300:
    print("Su consumo es alto")
    if consm_mensual_energia > 500:
        print("Considere medidas de ahorro energético")

# Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
# termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
# pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
# pantalla.

frase_user = input("Ingresa una palabra o una frase: ")
vocales = ["a","e","i","o","u"]

if frase_user[-1] in vocales:
    print(frase_user + "!")
else:
    print(frase_user)


# Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
# dependiendo de la opción que desee:
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
# El programa debe transformar el nombre ingresado de acuerdo con la opción seleccionada por
# el usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

nombre_user = input("Ingresa tu nombre:")

opcion = int(input("""¿Cómo quieres que transformemos tu nombre:
                   
1. Si quieres tu nombre en mayúsculas. Por ejemplo: PEDRO
2. Si quieres tu nombre en minúsculas. Por ejemplo: pedro
3. Si quieres tu nombre con la primera letra en mayúsculas. Por ejemplo: Pedro 
                   
Elige un número: """))

if opcion == 1:
    print(nombre_user.upper())
elif opcion == 2:
    print(nombre_user.lower())
else:
    print(nombre_user.title())

# Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
# magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
# por pantalla:
# • Menor que 3: "Muy leve" (imperceptible).
# • Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
# • Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
# generalmente no causa daños).
# • Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
# débiles).
# • Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
# • Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).

magn_terremoto = float(input("Escribe la magnitud del terremoto: "))

if magn_terremoto < 3:
    print(""" "Muy leve" (imperceptible)""")
elif magn_terremoto >= 3 and magn_terremoto < 4:
    print(""" "Leve" (ligeramente imperceptible)""")
elif magn_terremoto >= 4 and magn_terremoto < 5:
    print(""" "Moderado" (sentido por personas, pero generalmente no causa daños)""")
elif magn_terremoto >= 5 and magn_terremoto < 6:
    print(""" "Fuerte" (puede causar daños en estructuras débiles)""")
elif magn_terremoto >= 6 and magn_terremoto < 7:
    print(""" "Muy Fuerte" (puede causar daños significativos)""")
else:
    print(""" "Extremo" (puede causar graves daños a gran escala)""")

# Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
# del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
# si el usuario se encuentra en otoño, invierno, primavera o verano.

hemisferio = input("¿En qué hemisferio te encuentras?¿Norte o Sur?: ").lower()
mes = input("¿Qué mes del año es: ").lower()
dia = int(input("¿Qué días es: "))


#Norte
if hemisferio == "norte":
    if mes == "enero" or mes == "febrero":
        estacion = "INVIERNO"
    elif mes == "abril" or mes == "mayo":
        estacion = "PRIMAVERA"
    elif mes == "julio" or mes == "agosto":
        estacion = "VERANO"
    elif mes == "octubre" or mes == "noviembre":
        estacion = "OTOÑO"
    elif mes == "diciembre":
        if dia < 21:
            estacion = "OTOÑO"
        else:
            estacion = "INVIERNO"
    elif mes == "marzo":
        if dia > 20:
            estacion = "PRIMAVERA"
        else:
            estacion = "INVIERNO"
    elif mes == "junio":
        if dia < 21:
            estacion = "PRIMAVERA"
        else:
            estacion = "VERANO"
    elif mes == "setiembre":
        if dia > 20:
            estacion = "OTOÑO"
        else:
            estacion = "VERANO"

#Sur
if hemisferio == "sur":
    if mes == "enero" or mes == "febrero":
        estacion = "VERANO"
    elif mes == "abril" or mes == "mayo":
        estacion = "OTOÑO"
    elif mes == "julio" or mes == "agosto":
        estacion = "INVIERNO"
    elif mes == "octubre" or mes == "noviembre":
        estacion = "PRIMAVERA"
    elif mes == "diciembre":
        if dia < 21:
            estacion = "PRIMAVERA"
        else:
            estacion = "VERANO"
    elif mes == "marzo":
        if dia > 20:
            estacion = "OTOÑO"
        else:
            estacion = "VERANO"
    elif mes == "junio":
        if dia < 21:
            estacion = "OTOÑO"
        else:
            estacion = "INVIERNO"
    elif mes == "setiembre":
        if dia > 20:
            estacion = "PRIMAVERA"
        else:
            estacion = "INVIERNO"

        
print("En este momento te encuentras en", estacion)



