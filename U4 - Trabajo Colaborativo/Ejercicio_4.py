#Ejercicio 4 — “Escape Room: La Bóveda”

import time
import random, string #se importa para usar como código parcial

print("""

Historia
--------
Sos un agente que intenta abrir una bóveda con 3 cerraduras. Tenés energía y tiempo
limitados.
Si abrís las 3 cerraduras antes de quedarte sin energía o sin tiempo, ganás.

""")


cerraduras_abiertas = 0
energia = 100
tiempo = 12
alarma = False
codigo_parcial = ""
regla_antispam = 0
sistema_bloqueo = False

while True:

    nombre_agente = input("Ingresa tu nombre agente: ")
    if not nombre_agente.isalpha():
        print("Error: Ingrese solo letras.")
        continue
    break

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and sistema_bloqueo == False:

    #Estado del jugador
    print(f"""
    ------------------
    Energia: {energia}
    Tiempo: {tiempo}
    Cerraduras abiertas: {cerraduras_abiertas}
    Codigo Parcial: {codigo_parcial}
    ------------------
    """)

    while True:

        opcion = input("""
        1-Forzar cerradura (costo: -20 energía, -2 tiempo)
        2-Hackear panel (costo: -10 energía, -3 tiempo)
        3-Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10
    energía extra)

        Opción: """)
        if not opcion.isdigit():
            print("Error: Ingrese solo números.")
            continue
        break
    opcion = int(opcion)
    if opcion == 1:
        if regla_antispam == 2:
            print("Forzando ...")
            time.sleep(1)
            print("Cerradura trabada por 3 intentos seguidos...")
            time.sleep(1)
            alarma = True
            print("Se activa alarma por cerradura trabada")
            regla_antispam = 0

        elif energia < 40:
            while True:
                alarma_opcion = input("""
                Riesgo de alarma!
                Elige un número del 1 al 3: 
                """)
                if not alarma_opcion.isdigit():
                    print("Error: Ingresa solo números.")
                    continue
                alarma_opcion = int(alarma_opcion)
                if alarma_opcion < 1 or alarma_opcion > 3:
                    print("Error: Número fuera de rango")
                    continue
                break
            if alarma_opcion == 3:
                alarma = True
                print("Alarma activada ...")
                time.sleep(1)
            else:
                regla_antispam += 1
                cerraduras_abiertas += 1
                print("Forzando cerradura ...")
                time.sleep(1)
        else:
            regla_antispam += 1
            cerraduras_abiertas += 1
            print("Forzando cerradura ...")
            time.sleep(1)
        #Actualizamos la energia y el tiempo utilizado
        energia -= 20
        tiempo -= 2

    #Si elige la opción 2 o 3, reiniciamos la regla anti spam, debido a que eligió otra opción que no es la 1
    if opcion == 2:
        regla_antispam = 0
        pasos = 4
        for i in range(pasos):
            print("Hacking...")
            time.sleep(2)
            codigo_parcial += random.choice(string.ascii_uppercase)
            print(f"Código parcial: {codigo_parcial}")

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("Cerradura abierta!")
            codigo_parcial = ""
        #Actualizamos la energia y el tiempo utilizado
        energia -= 10
        tiempo -= 3

    #Si la energía está en 85 o más, la seteamos en 100 directamente
    #ya que no debe pasarse del máximo. Sino, le sumamos los 15 puntos correspondientes.
    if opcion == 3:

        regla_antispam = 0
        tiempo -= 1
        if energia > 85:
            energia = 100
        else:
            energia += 15
        if alarma:
            energia -= 10
        print(f"""
        Descansando ...
        """)
        time.sleep(1)

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        sistema_bloqueo = True
        print("""
        Sistema BLOQUEADO
        """)

    if cerraduras_abiertas == 3:
        print("""
        Se abrieron todas las cerraduras.
        VICTORIA!
        """)
    if energia <= 0 or tiempo <= 0:
        print("""
        DERROTA!
        """)
    if sistema_bloqueo:
        print("""
        DERROTA! (bloqueo)
        """)
