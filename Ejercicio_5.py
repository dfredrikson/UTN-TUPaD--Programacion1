#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

import time 

print("""

#####################
Bienvenido a la ARENA
#####################

""")
while True:

    nombre_gladiador = input("Nombre del Gladiador: ")
    if not nombre_gladiador.isalpha():
        print("Error: Solo se permiten letras.")
        continue
    break

vida_gladiador = 100
vida_enemigo = 100
pociones_vida = 3
danio_ataque_pesado = 15
danio_base_enemigo = 12
inicio_juego = True #creamos esta bandera para saber si es el inicio del juego o un turno nuevo

while vida_gladiador > 0 and vida_enemigo > 0:

    if inicio_juego:
        print("""

        ##################
        Inicio del COMBATE
        ##################

        """)
        inicio_juego = False #el juego ya inició.

    else:
        print("""
        ---Nuevo turno---
        """)

    #mostramos la vida de ambos personajes
    print(f"""
    ----------------------
    Vida gladiador: {vida_gladiador} HP
    Vida enemigo: {vida_enemigo} HP
    Pociones restantes: {pociones_vida}
    ----------------------
    """)

    while True:

        opcion = input("""
        1. Ataque Pesado
        2. Ráfaga Veloz
        3. Curar
        """)
        if not opcion.isdigit():
            print("Error: Solo se permiten números.")
            continue

        opcion = int(opcion)
        if opcion < 1 or opcion > 3:
            print("Error: Número fuera de rango.")
            continue
        break

    #Ataque pesado
    if opcion == 1:
        if vida_enemigo < 20:
            print("GOLPE CRÍTICO!")
            golpe_critico = danio_ataque_pesado * 1.5
            vida_enemigo -= golpe_critico
            print(f"¡Atacaste al enemigo por {golpe_critico} puntos de daño!")
            time.sleep(1)
        else:
            print("Ataque Pesado!")
            vida_enemigo -= danio_ataque_pesado
            time.sleep(1)
    #Ráfaga veloz
    if opcion == 2:

        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")
            time.sleep(1)
    
    #Curar
    if opcion == 3:
        if pociones_vida > 0:
            vida_gladiador += 30
            pociones_vida -= 1
            print("Curando ...")
            time.sleep(1)
        else:
            print("¡No quedan pociones!")
            time.sleep(1)

    #Turno del enemigo
    vida_gladiador -= danio_base_enemigo
    print("¡El enemigo te atacó por 12 puntos de daño!")
    time.sleep(1)

if vida_gladiador > 0:
    print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")
elif vida_gladiador <= 0:
    print("DERROTA. Has caído en combate.")


