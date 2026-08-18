#Ejercicio 2 — “Acceso al Campus y Menú Seguro”
#Objetivo: Login con intentos + menú de acciones con validación estricta.

usuario_correcto = "alumno"
clave_correcta = "python123"

#Se crea una función con todo el menú, para que quede más ordenado. Luego la llamo dentro del ciclo "for"
def menu():

    #Se crea un menú donde la única opción para salir, sea que el usuario coloque el número 4
    while True:
        print("1) Estado 2) Cambiar clave 3) Mensaje 4) Salir")
        opcion = input("Opción: ")
        if not opcion.isdigit():
            print("Error: ingrese un número válido.")
            continue
        #una vez validado que es un número, transformamos la variable de string a un dígito.
        opcion = int(opcion) 

        if opcion < 1 or opcion > 4:
            print("Error: opción fuera de rango.")
            continue

        #Opciones del menú

        #Opción 1: muestra la palabra "Inscripto"
        if opcion == 1:
            print("Inscripto")

        #Opción 2: pide nueva clave de 6 caracteres mínimo. Si no da error y vuelve al menú.
        #Luego se pide confirmacion. Si no coincide, da error y vuelve al menú.
        elif opcion == 2:
            while True:
                nueva_clave = input("Nueva clave: ")
                if len(nueva_clave) < 6:
                    print("Error: mínimo 6 caracteres.")
                    continue
                confirmacion_clave = input("Confirmación nueva clave: ")
                if confirmacion_clave != nueva_clave:
                    print("Error: Las claves no coinciden.")
                    continue
                print("Clave modificada correctamente.")
                break

        #Opción 3: muestra mensaje motivacional
        elif opcion == 3:
            print("La paciencia crea genios: Nadie nace sabiendo, la constancia supera con creces al talento natural.")
            continue
        if opcion == 4:
            break

    return


for i in range(3):

    usuario = input(f"Intento {i+1}/3 - Usuario: ")
    clave = input("Clave: ")
    if usuario != usuario_correcto or clave != clave_correcta:
        print("Error: credenciales inválidas.")
    else:
        print("Acceso concedido.")
        menu()
        break
#Lo que permite este "else" es que si se ejecuta el break que está después de la función "menu"
#el ciclo "for" lo ignora, por lo que no se imprime en pantalla

else:
    print("Cuenta bloqueada")