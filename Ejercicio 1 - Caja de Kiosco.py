# Ejercicio 1 - Caja de kiosco


while True :
    nombre = input("Hola ¿Cuál es su nombre?: ")
    if nombre.isalpha() :
        break
    else :
        print("Ingrese un nombre valido ( Solo letras ): ")

print( "Hola " + nombre + " " )


while True :
    productos = input("¿Cuantos productos desea llevar hoy?: ")
    if productos.isdigit() and int(productos) > 0 :
        productos = int(productos)
        break
    else :
        print("Por favor ingrese un numero de productos mayor a 0: ")

precios = []
descuentos = []
totalSinDescuentos = 0
totalDescuentos = 0

for i in range( productos ):
    while True :
        precio = input("ingrese precio del producto seleccionado: ")
        if precio.isdigit() :
            precio = int(precio)
            totalSinDescuentos = totalSinDescuentos + precio
            precios.append(precio)

            break
        else :
            print("Ingrese un precio valido")

    while True :
        descuento = input("¿Posee descuento el producto seleccionado? ( S/N )").lower()
        if descuento == "s" or descuento == "n" :
            descuentos.append(descuento)
            break
        else :
            print("Por favor ingrese 'S' para confirmar existencia de descuento o 'N' en caso de no tener descuento")
    
    if descuento == "s" :
        totalDescuentos = totalDescuentos + ( precio / 10 )
        precio = precio * 0.9

totalConDescuento = totalSinDescuentos - totalDescuentos
promedio = totalConDescuento / productos

print(f"Cliente: { nombre }")
print(f"Cantidad de productos { productos }")

for i in range(productos) :
    print(f"Producto { i + 1 } - Precio : { precios[i] } - Con Descuento (S/N) : { descuentos[i] }")

print(f"Total sin descuentos: { totalSinDescuentos }")
print(f"Total con descuentos: { totalConDescuento }")
print(f"Ahorro: { totalDescuentos }")
print(f"Promedio por producto: { promedio:.2f}")








