#Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

cant_turnos_lunes = 4
cant_turnos_martes = 3
turnos_lunes = "Turno1:Turno2:Turno3:Turno4: "  # Le agregamos un espacio artificial al final del texto para asegurarnos de que el ciclo procese la última palabra de la oración.
turnos_martes = "Turno1:Turno2:Turno3: "



def reservar():

    #aprendí esta palabra clave, en base a un error Unbound que me daba al momento de testear el código
    #de esta manera, siempre usa y modifica la variable global, que está fuera de la función
    global turnos_lunes, turnos_martes, cant_turnos_lunes, cant_turnos_martes

    while True:
        dia_elegido = input("Elegir día (1=Lunes, 2=Martes): ")
        if not dia_elegido.isdigit():
            print("Error: Se permiten solo números.")
            continue
        dia_elegido = int(dia_elegido)

        if dia_elegido < 1 or dia_elegido > 2:
            print("Error: Número fuera de rango.")
            continue

        #Verificamos que haya turnos disponibles para ese día
        if dia_elegido == 1 and cant_turnos_lunes == 0:
            print("Error: No hay más turnos disponibles para el día Lunes.")
            continue
        elif dia_elegido == 2 and cant_turnos_martes == 0:
            print("Error: No hay más turnos disponibles para el día Martes.")
            continue

        while True:
            nombre_paciente = input("Nombre paciente: ")
            if not nombre_paciente.isalpha():
                print("Error: Se permiten solo letras.")
                continue
            break
        #le sumamos un espacio adelante y otro detrás para luego poder identificarlo 
        # cuando se haga el for y se recorra el string de turnos
        nombre_paciente = " " + nombre_paciente.capitalize() + " "



        #Ahora vamos a recorrer la variable correspondiente al dia
        #para verificar si ese paciente ya está. Lo recorremos con un ciclo "for"

        #Variables auxiliares
        palabra_actual = ""
        numero_turno = ""
        encontrado = False #creamos una variable bandera para saber si el paciente fue encontrado
        nombre_agregado = False #creamos una variable bandera para saber si el paciente fue agregado

        #en estas variables vamos a crear la nueva lista de turnos, con el paciente agregado, y reemplazaremos la anterior
        turnos_lunes_nuevo = "" 
        turnos_martes_nuevo = ""

        #Recorremos el día Lunes y buscamos el paciente
        if dia_elegido == 1:

            for letra in turnos_lunes:

                # Si "letra" no es un espacio, quiere decir que es una letra. La sumamos a nuestra palabra actual
                # para ir armando la palabra
                if letra != " ":
                    palabra_actual += letra

                # Si es un espacio, significa que terminamos de leer una palabra completa
                # Revisamos si es un "Turno" o un paciente
                else:

                    if palabra_actual == nombre_paciente[1:-1]: #con el [1:-1] quitamos los espacios que rodean al nombre
                        encontrado = True
                        break
                    #Si no es la palabra que buscamos, vaciamos la palabra temporal para armar la siguiente
                    #y guardamos esa palabra para usarla como numero de turno.
                    else:
                        if ":" in palabra_actual:
                            numero_turno = palabra_actual[:-1] #le quitamos los ":" de "Turno1:"
                        palabra_actual = ""

            if encontrado:
                print(f"El paciente ya se encuentra agendado para el {numero_turno} del día Lunes.")
                break

            # Si no se encuentra el paciente, lo agregamos
            # Recorremos todo el string "turnos_lunes" buscando los ":"
            # Si después del ":" no hay un espacio, significa que ese slot ya tiene un paciente
            # Si hay un espacio (slot vacío), allí agregamos al nuevo paciente
            else:
                for i in range(len(turnos_lunes)):

                    letra_actual = turnos_lunes[i]
                    turnos_lunes_nuevo += letra_actual

                    #la verificación que se hace es: Si estamos "parados" sobre los ":", y además adelante nuestro NO hay un espacio
                    #significa que ese slot ya tiene un paciente (el slot vacío tiene un espacio después del ":")
                    #A menos que sea el último turno (verificamos el carácter anterior): si es el último turno, se agrega al paciente.
                    if letra_actual == ":" and (turnos_lunes[i+1] != " " or turnos_lunes[i-1] == "4") and nombre_agregado == False:

                        #recorremos cada letra del paciente y la vamos agregando a esta nueva lista de turnos
                        for letra in nombre_paciente:
                            turnos_lunes_nuevo += letra
                        cant_turnos_lunes -= 1
                        nombre_agregado = True
                        print("Paciente agregado correctamente")
            turnos_lunes = turnos_lunes_nuevo
            print(f"Lista actualizada: {turnos_lunes_nuevo}")
            break

        #Recorremos el día Martes y buscamos el paciente
        if dia_elegido == 2:

            for letra in turnos_martes:

                # Si "letra" no es un espacio, quiere decir que es una letra. La sumamos a nuestra palabra actual
                # para ir armando la palabra
                if letra != " ":
                    palabra_actual += letra

                # Si es un espacio, significa que terminamos de leer una palabra completa
                # Revisamos si es un "Turno" o un paciente
                else:

                    if palabra_actual == nombre_paciente[1:-1]: #con el [1:-1] quitamos los espacios que rodean al nombre
                        encontrado = True
                        break
                    #Si no es la palabra que buscamos, vaciamos la palabra temporal para armar la siguiente
                    #y guardamos esa palabra para usarla como numero de turno.
                    else:
                        if ":" in palabra_actual:
                            numero_turno = palabra_actual[:-1] #le quitamos los ":" de "Turno1:"
                        palabra_actual = ""

            if encontrado:
                print(f"El paciente ya se encuentra agendado para el {numero_turno} del día Martes.")
                break

            # Si no se encuentra el paciente, lo agregamos
            # Recorremos todo el string "turnos_martes" para encontrar un espacio, que va
            # a significar que inmediatamente después hay nombre de un paciente
            else:
                for i in range(len(turnos_martes)):

                    letra_actual = turnos_martes[i]
                    turnos_martes_nuevo += letra_actual
                    #la verificacion que se hace es: Si estamos "parados" sobre los ":", y además adelante nuestro hay un espacio
                    #significa que hay un nombre en ese lugar. Al menos que sea el último turno, entonces se verifica el caracter
                    #anterior. Si es el último turno, se agrega al paciente.
                    if letra_actual == ":" and (turnos_martes[i+1] != " " or turnos_martes[i-1] == "3") and nombre_agregado == False:

                        #recorremos cada letra del paciente y la vamos agregando a esta nueva lista de turnos
                        for letra in nombre_paciente:
                            turnos_martes_nuevo += letra
                        cant_turnos_martes -= 1
                        nombre_agregado = True
                        print("Paciente agregado correctamente")
            turnos_martes = turnos_martes_nuevo
            print(f"Lista actualizada: {turnos_martes_nuevo}")
            break

    
    return

def cancelar_turno():

    global turnos_lunes, turnos_martes, cant_turnos_lunes, cant_turnos_martes

    while True:
            dia_elegido = input("Elegir día (1=Lunes, 2=Martes): ")
            if not dia_elegido.isdigit():
                print("Error: Se permiten solo números.")
                continue
            dia_elegido = int(dia_elegido)

            if dia_elegido < 1 or dia_elegido > 2:
                print("Error: Número fuera de rango.")
                continue

            while True:
                nombre_paciente = input("Nombre paciente: ")
                if not nombre_paciente.isalpha():
                    print("Error: Se permiten solo letras.")
                    continue
                break
            #le sumamos un espacio adelante y otro detrás para luego poder identificarla 
            # cuando se haga el for y se recorra el string de turnos
            nombre_paciente = " " + nombre_paciente.capitalize() + " "

            #Variables auxiliares
            palabra_actual = ""
            paciente_encontrado = False
            #en estas variables vamos a crear la nueva lista de turnos, con el paciente eliminado, y reemplazaremos la anterior
            turnos_lunes_nuevo = "" 
            turnos_martes_nuevo = ""

            #Recorremos el día Lunes y buscamos el paciente
            if dia_elegido == 1:

                for letra in turnos_lunes:

                    # Si "letra" no es un espacio, quiere decir que es una letra. La sumamos a nuestra palabra actual
                    # para ir armando la palabra
                    if letra != " ":
                        palabra_actual += letra

                    # Si es un espacio, significa que terminamos de leer una palabra completa
                    # Revisamos si es un "Turno" o un paciente
                    else:
                        if palabra_actual == nombre_paciente[1:-1]: #con el [1:-1] quitamos los espacios que rodean al nombre

                            #Quitamos el espacio que sobra y agregamos un espacio vacio a la lista
                            turnos_lunes_nuevo = turnos_lunes_nuevo[:-1]
                            turnos_lunes_nuevo += ""  #el slot queda vacío (sin nombre)
                            palabra_actual = ""
                            cant_turnos_lunes += 1
                            paciente_encontrado = True
                            print("Paciente eliminado correctamente")
                      
                        else:
                            palabra_actual = palabra_actual + " "
                            for letra in palabra_actual:
                                turnos_lunes_nuevo += letra
                            palabra_actual = ""
                turnos_lunes = turnos_lunes_nuevo
                if not paciente_encontrado:
                    print("El paciente no fue encontrado")
                print(f"Lista actualizada: {turnos_lunes_nuevo}")
                break

            if dia_elegido == 2:
            
                for letra in turnos_martes:

                    # Si "letra" no es un espacio, quiere decir que es una letra. La sumamos a nuestra palabra actual
                    # para ir armando la palabra
                    if letra != " ":
                        palabra_actual += letra

                    # Si es un espacio, significa que terminamos de leer una palabra completa
                    # Revisamos si es un "Turno" o un paciente
                    else:
                        if palabra_actual == nombre_paciente[1:-1]: #con el [1:-1] quitamos los espacios que rodean al nombre

                            #Quitamos el espacio que sobra y agregamos un espacio vacio a la lista
                            turnos_martes_nuevo = turnos_martes_nuevo[:-1]
                            turnos_martes_nuevo += ""  #el slot queda vacío (sin nombre)
                            palabra_actual = ""
                            cant_turnos_martes += 1
                            paciente_encontrado = True
                            print("Paciente eliminado correctamente")
                        
                        else:
                            palabra_actual = palabra_actual + " "
                            for letra in palabra_actual:
                                turnos_martes_nuevo += letra
                            palabra_actual = ""
                turnos_martes = turnos_martes_nuevo
                if not paciente_encontrado:
                    print("El paciente no fue encontrado")
                print(f"Lista actualizada: {turnos_martes_nuevo}")
                break

    return

def ver_agenda():

    global turnos_lunes, turnos_martes
    while True:

        #usamos la misma lógica de comprobación que las funciones anteriores
        ver_dia = input("Elegir el día 1=Lunes, 2=Martes: ")
        if not ver_dia.isdigit():
            print("Error: Se permiten solo números.")
            continue
        ver_dia = int(ver_dia)
        if ver_dia < 1 or ver_dia > 2:
            print("Error: Número fuera de rango.")
            continue

        if ver_dia == 1:
            turno_string = turnos_lunes
        else:
            turno_string = turnos_martes

        numero_slot = 0
        nombre_actual = ""
        leyendo_nombre = False

        for i in range(len(turno_string)):

            letra = turno_string[i]
            if letra == ":":
                numero_slot += 1
                # Si el siguiente carácter es espacio → slot ocupado
                if turno_string[i+1] == " ":
                    leyendo_nombre = True
                    nombre_actual = ""
                else:
                    print(f"Turno {numero_slot}: (libre)")
            elif leyendo_nombre:
                if letra == " ":
                    if nombre_actual != "":  # terminamos de leer el nombre
                        print(f"Turno {numero_slot}: {nombre_actual}")
                        leyendo_nombre = False
                else:
                    nombre_actual += letra
        if leyendo_nombre and nombre_actual == "":
            print(f"Turno {numero_slot}: (libre)")
        break

    return

#Creamos el menu con un ciclo while, donde cada opcion va a llamar a una función determinada
#De esta manera el código queda más limpio y ordenado

def ver_resumen():

    #revisamos la lista de los turnos para ver los espacios y así saber
    #si hay pacientes agendados
    #creamos unas variables banderas

    turnos_ocupados_lunes = 0
    turnos_ocupados_martes = 0
    turnos_disp_lunes = cant_turnos_lunes
    turnos_disp_martes = cant_turnos_martes
    contador_de_espacios = 0

    # creamos un ciclo for para recorrer el string de turnos
    # pero evitamos llegar al último espacio del string, para no romper la lógica del ciclo
    for i in range(len(turnos_lunes)-1):

        letra = turnos_lunes[i]

        # Si "letra" es un espacio, quiere decir que a continuación viene el nombre de un paciente

        if letra == " ":
            contador_de_espacios += 1

    turnos_ocupados_lunes = contador_de_espacios / 2

    #volvemos a 0 el contador
    contador_de_espacios = 0
    for i in range(len(turnos_martes)-1):

        letra = turnos_martes[i]

        # Si "letra" es un espacio, quiere decir que a continuación viene el nombre de un paciente

        if letra == " ":
            contador_de_espacios += 1

    turnos_ocupados_martes = contador_de_espacios / 2

    if turnos_ocupados_lunes == 0 and turnos_ocupados_martes == 0:
        dia_mas_turnos = "Ambos días no tienen turnos ocupados"
    elif turnos_ocupados_lunes == turnos_ocupados_martes:
        dia_mas_turnos = "Ambos días tienen la misma cantidad de turnos ocupados"
    elif turnos_ocupados_lunes > turnos_ocupados_martes:
        dia_mas_turnos = "Lunes"
    else:
        dia_mas_turnos = "Martes"

    print(f"""

    Día Lunes:
    ----------
    Turnos disponibles: {int(turnos_disp_lunes)} 
    Turnos ocupados: {int(turnos_ocupados_lunes)}
    
    Día Martes:
    -----------
    Turnos disponibles: {int(turnos_disp_martes)} 
    Turnos ocupados: {int(turnos_ocupados_martes)}

    Día con más turnos ocupados:
    ---------------------------
    {dia_mas_turnos}
    
""")


    return


while True:

    nombre_operador = input("Operador: ")
    if not nombre_operador.isalpha():
        print("Error: Se permiten solo letras.")
        continue
    break

while True:

    print("1) Reservar turno 2) Cancelar turno 3)Ver agenda del día 4) Ver resumen general 5) Cerrar sistema")
    opcion = input("Opción: ")
    if not opcion.isdigit():
        print("Error: Ingrese un número válido")
        continue

    opcion = int(opcion)
    if opcion < 1 or opcion > 5:
        print("Error: opción fuera de rango.")
        continue

    if opcion == 1:
        reservar()
        continue
    elif opcion == 2:
        cancelar_turno()
        continue
    elif opcion == 3:
        ver_agenda()
        continue
    elif opcion == 4:
        ver_resumen()
        continue
    elif opcion == 5:
        break

