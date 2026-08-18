#Ejercicio 1 — “Caja del Kiosco”
#Objetivo: Simular una compra con validaciones y cálculo de total.

import time

#Pedir nombre del cliente
while True:

    nombre_del_cliente = input("Ingresa el nombre del cliente: ")
    if not nombre_del_cliente.isalpha():
        print("Debe ingresar letras. Intenta nuevamente")
        continue
    break
#Pedir cantidad de productos a comprar
while True:
    cant_productos = input("Ingresa la cantidad de productos a comprar: ")

    if not cant_productos.isdigit():
        print("Debe ingresar números positivos. Intenta nuevamente")
        continue
    cant_productos = int(cant_productos)

    if cant_productos <= 0:
        print("Debe ingresar un número superior a 0")
        continue
    break


#Comprobación
print(f"""

**************************************
Datos ingresados correctamente. 
Ahora se te pedirá algunos datos de los {cant_productos} productos
**************************************

""")
time.sleep(1)


#Se pedirá el precio de cada producto, y se guardará en 2 variables.
#Una para los productos sin descuento y otra con los productos que tienen descuento
#Se crea un string para ir guardando el reporte de productos

total_compra = 0
total_con_descuento = 0
reporte_productos = ""

for i in range(cant_productos):

    while True:
        precio_producto = input(f"Ingresa el PRECIO del producto {i+1}: ")
        if precio_producto.isdigit() and int(precio_producto) != 0:
            break
        else:
            print("Debe ingresar solo números enteros positivos, mayores a 0. Intenta nuevamente")
            continue
    precio_producto = int(precio_producto)
    print(f"Producto {i+1} agregado")

    while True:
        tiene_desc = input("¿El producto tiene descuento? S/N: ").upper()
        if tiene_desc != "S" and tiene_desc != "N":
            print("Debes ingresar solo la letra S o N")
        if tiene_desc == "S":
            print("Se aplica un 10% de descuento al producto")
            total_compra += precio_producto #sumamos el precio al total antes de aplicarle el descuento
            precio_producto = precio_producto * 0.9
            total_con_descuento += precio_producto #sumamos el precio al total con descuento
            break
        if tiene_desc == "N":
            total_compra += precio_producto
            print("Producto registrado sin descuento")
            break

    # Vamos armando el texto del reporte, agregando un salto de línea (\n) al final de cada producto
    reporte_productos += f"Producto {i + 1} - Precio: {precio_producto} Descuento (S/N): {tiene_desc}\n"

    
#Calculamos totales para luego imprimirlos en pantalla
ahorro_total = total_compra - total_con_descuento
promedio_productos = total_con_descuento / cant_productos


print(f"""

Cliente: {nombre_del_cliente}
Cantidad de productos: {cant_productos}
{reporte_productos}
**************************************
Total sin decuentos: ${total_compra}
Total con descuentos: ${total_con_descuento}
Ahorro total: ${ahorro_total}
Promedio por productos: ${promedio_productos:.2f}
**************************************

""")