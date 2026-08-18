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
