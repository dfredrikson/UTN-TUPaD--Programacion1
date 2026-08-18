while True:

    print("""
    ==================================================
                MENÚ DE TRABAJOS PRÁCTICOS
    ==================================================
    1. Ejercicio 1 (Imprimir números del 0 al 100)
    2. Ejercicio 2 (Contar dígitos de un número)
    3. Ejercicio 3 (Sumar números comprendidos entre 2 valores)
    4. Ejercicio 4 (Sumar números en secuencia)
    5. Ejercicio 5 (Juego adivinar número)
    6. Ejercicio 6 (Imprimir números pares)             
    7. Ejercicio 7 (Suma de números comprendidos entre 0 y un número)
    8. Ejercicio 8 (Categorizar 100 números)
    9. Ejercicio 9 (Calcular la media de valores)
    10. Ejercicio 10 (Invertir número)
    
    0. Salir del programa
    ==================================================
    """)

    while True:

        opcion = input("Ingresa la opción que desea revisar: ")
        if not opcion.isdigit() or int(opcion) > 10:
            print("Debes ingresar un número comprendido entre el 0 y 10")
            continue
        opcion = int(opcion)
        break

    if opcion == 0:
        print("\nMuchas gracias por revisar!")
        break

    elif opcion == 1:
        print("\n--- EJECUTANDO EJERCICIO 1 ---")
        for i in range(0,101):
            print(i)
        print("-------------------------------\n")
        

    elif opcion == 2:
        print("\n--- EJECUTANDO EJERCICIO 2 ---")
        # Creamos una validación para el input del usuario, y asegurarnos que ingrese dígitos numéros.
        while True:

            num = input("Ingresa un número entero: ")
            if not num.isdigit():
                print("Debes ingresar un número entero")        
                continue
            num = int(num)
            break

        #ahora contamos la cantidad de dígitos que tiene el número. Como no sabemos la cantidad, utilizamos un bucle while.
        # Pero antes verificamos si el número es 0

        cont = 0
        num_aux = num

        if num_aux == 0:
            cont += +1
        else:
            while num_aux > 0:
                num_aux = num_aux // 10 #vamos reduciendo la cantidad de dígitos. Ejemplo 25//10 = 2 | 2//10 = 0
                cont += 1

        print(f"El número {num} tiene {cont} dígitos.")
        print("-------------------------------\n")    
        

    elif opcion == 3:
        print("\n--- EJECUTANDO EJERCICIO 3 ---")

        # Creamos un bucle for ya que sabemos la cantidad de datos que vamos a pedir.
        # Tambien creamos una validación para el input del usuario, y asegurarnos que ingrese dígitos números.

        num_1 = None
        num_2 = None

        for i in range(2):

            while True:
                aux = input(f"Ingresa un valor número {i+1}: ")
                if not aux.isdigit():
                    print("Debes ingresar un número entero")
                    continue
                aux = int(aux)
                break
            if i == 0:
                num_1 = aux
            else:
                num_2 = aux

        #Ahora usamos un bucle for para recorrer los numeros comprendidos entre num_1 y num_2, y sumarlos.

        suma = 0

        for i in range(num_1, num_2):
            suma += i

        print(f"La suma de los números comprendidos entre {num_1} y {num_2} es {suma}.") 
        print("-------------------------------\n")
        

    elif opcion == 4:
        print("\n--- EJECUTANDO EJERCICIO 4 ---")
        total = 0
        
        print("Vamos a sumar todos los números que ingreses, en secuencia. " \
        "Si deseas detener el programa, ingresa el número 0.")
        
        while True:
            aux = input("Ingrese un número entero, que desee sumar: ")
            if not aux.isdigit():
                print("Debe ingresar un número entero.")
                continue
            aux = int(aux)
            if aux == 0:
                break
            total += aux
            print(f"La suma hasta ahora es {total}.")


        print(f"El total de la suma de todos los números es {total}.")
        print("-------------------------------\n")
        
    elif opcion == 5:
        print("\n--- EJECUTANDO EJERCICIO 5 ---")
        import random

        num_random = random.randint(0,9)
        cont = 0

        print("Hagamos un juego! Debes adivinar un número entre el 0 y el 9. Empecemos")

        while True:
            num_user = input("Dime el número:")
            if not num_user.isdigit() or int(num_user) > 9: #verificamos que sea un dígito y menor de 9.
                print("Debes ingresar un número entero, entre 0 y 9")
                continue
            num_user = int(num_user)
            cont += 1
            if num_user == num_random:
                print(f"Perfecto! Adivinaste luego de {cont} intentos. El número era el {num_user}.")
                break

        print("-------------------------------\n")
        
    elif opcion == 6:
        print("\n--- EJECUTANDO EJERCICIO 6 ---")
        for i in range(100,-1,-2):
            print(i)
        print("-------------------------------\n")
        
    elif opcion == 7:
        print("\n--- EJECUTANDO EJERCICIO 7 ---")
        import time

        print("Vamos a sumar números! Sumaremos todos los números enteros comprendidos " \
        "entre el 0 y el número positivo que elijas.")

        suma = 0

        #validamos que el número ingresado sea correcto
        while True:

            num = input("Elije tu número: ")
            if not num.isdigit():
                print("Recuerda que debe ser un número entero y positivo")
                continue
            num = int(num)
            break

        print("Sumando...")
        time.sleep(1)

        #recorremos todos los números y los vamos sumando a la variable "suma". Los mostramos en pantalla para 
        #que el usuario verifique. 
        for i in range(1,num+1):
            suma_anterior = suma
            suma += i
            print(f"{suma_anterior} + {i} = {suma}")

        print(f"La suma de todos los dígitos entre el 0 y el {num} es {suma}.")
        print("-------------------------------\n")
        
    elif opcion == 8:
        print("\n--- EJECUTANDO EJERCICIO 8 ---")
        cant_numeros = 5 #<----- #CAMBIAR EL CONTADOR POR LA CANTIDAD DE NÚMEROS QUE SE DESEA PEDIR AL USUARIO

        print(f"""
        **************************************************
        Vamos a categorizar tus números. 
        Cuántos son pares, impares, negativos y positivos.
        Para eso debe elegir {cant_numeros} números.
        **************************************************

        """)

        pares = 0
        impares = 0
        positivos = 0
        negativos = 0
        cont = 0


        #acá debemos corroborar si el usuario ingresó un número o no (negativo o positivo)
        #debemos despegar el primer signo negativo (-) por las dudas que el usuario ingrese algo como "-a", "--2" o "-5a"
        #despejamos el signo y verificamos.
        while cont < cant_numeros:

            num = input("Ingresa el número: ")
            if num[0] == "-": #verificamos el primer dígito
                aux = num[1:] #guardamos en un auxiliar
                if not aux.isdigit(): #verificamos el auxiliar
                    print("Debes colocar un número entero")
                    continue
                num = int(num)
                negativos += 1
            else:
                if not num.isdigit(): 
                    print("Debes colocar un número entero")
                    continue
                num = int(num)
                positivos += 1
            if num % 2 == 0:
                pares += 1
            else:
                impares += 1
            
            cont += 1

        print(f"""
        **************************************************
        RESULTADOS DE LA CATEGORIZACIÓN ({cant_numeros} números)
        **************************************************
        Cantidad de números pares:     {pares}
        Cantidad de números impares:   {impares}
        Cantidad de números negativos: {negativos}
        Cantidad de números positivos: {positivos}
        **************************************************
        Nota: El número 0 se considera par y positivo.
        """)
        print("-------------------------------\n")
        
    elif opcion == 9:
        print("\n--- EJECUTANDO EJERCICIO 9 ---")
        cant_numeros = 5 #<----- #CAMBIAR EL CONTADOR POR LA CANTIDAD DE NÚMEROS QUE SE DESEA PEDIR AL USUARIO

        print(f"""
        **************************************************
        Vamos a calcular la media de todos tus números. 
        Para eso debe elegir {cant_numeros} números.
        **************************************************

        """)

        cont = 0
        total = 0

        while cont < cant_numeros:
            
            num = input("Ingresa un número: ")
            if not num.isdigit():
                print("Debes ingresar un número entero")
                continue
            num = int(num)
            cont += 1
            total += num

        print(f"""
        RESULTADO
        *************
        El total acumulado es: {total}
        La media de los {cant_numeros} números es: {total/cont}
        """)
        print("-------------------------------\n")
        
    elif opcion == 10:
        print("\n--- EJECUTANDO EJERCICIO 10 ---")
        print("""
        ****************************
        Vamos a invertir tu número!
        ****************************
        """)

        while True:
            #validamos el número
            num = input("Ingresa un número: ")
            if not num.isdigit():
                print("Debes ingresar un número entero positivo")
                continue
            num = int(num)
            break

        """
        Utilizamos %, // y * para ir desarmando el número. Creamos un numero_invertido en 0, donde vamos a ir
        colocando cada número, de atrás para adelante.

        Ejemplo:
            num = 547
            547 % 10 = 7 <--- obtenemos el último digito. Lo guardamos en ultimo_digito. ultimo_digito == 7
            (numero_invertido * 10 ) + 7 = 7
            547 // 10 = 54 <--- obtenemos el nuevo numero para continuar. Lo guardamos numero_auxiliar. numero_auxiliar == 54
            numero_auxiliar % 10 = 4 <--- obtenemos el último digito. Lo guardamos en ultimo_digito. ultimo_digito == 4
            (numero_invertido * 10 ) + 4 = 74
            54 // 10 = 5 <--- obtenemos el nuevo numero para continuar. Lo guardamos numero_auxiliar. numero_auxiliar == 5
            numero_auxiliar % 10 = 5 <--- obtenemos el último digito. Lo guardamos en ultimo_digito. ultimo_digito == 5
            (numero_invertido * 10 ) + 4 = 574
        """

        numero_auxiliar = num
        numero_invertido = 0
        ultimo_digito = 0

        #ejemplo: num = 547
        while numero_auxiliar > 0:

            ultimo_digito = numero_auxiliar % 10 #547 % 10 = 7
            numero_invertido = (numero_invertido * 10) + ultimo_digito #(0 * 10) + 7 = 7
            numero_auxiliar = numero_auxiliar // 10 #547 // 10 = 54

        print(f"""
        ****************************
        RESULTADO
        ****************************
        Tu número: {num}
        Número invertido: {numero_invertido}
        """)

        print("-------------------------------\n")
        

    input("\nPresiona ENTER para volver al menú principal...")