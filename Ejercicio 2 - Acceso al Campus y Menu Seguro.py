#Ejercicio 2 — “Acceso al Campus y Menú Seguro”

usuarioCorrecto = "alumno"
claveCorrecta = "python123"

intentos = 0
loged = False

while intentos < 3 :
    intentos += 1

    usuarioIngresante = input("Ingrese nombre de usuario: ")
    claveIngresante = input("Ingrese clave: ")

    if usuarioIngresante == usuarioCorrecto and claveIngresante == claveCorrecta:
        loged = True
        break
    elif intentos < 3 :
        print(f"Usuario o clave incorrectos, intente nuevamente. Intento { intentos } / 3 ")
    elif intentos == 3 :
        print("Usuario o clave incorrectos. Intento ( 3 / 3 )")
        print("Cuenta Bloqueada")

if loged :
    print("Login correcto")

while loged :

    print("     ")
    print("--- Menu ---")
    print(f" 1. Ver estado de inscripcion ")
    print(f" 2. Cambiar clave ")
    print(f" 3. Mostrar mensaje motivacional ")
    print(f" 4. Salir ")

    opcion = input("Elija una opcion ")

    if opcion.isdigit() :
        if opcion == "1" :
            print("Estado: Inscripto")
        
        elif opcion == "2" :
            claveActual = input("Ingrese clave actual: ")

            while claveActual == claveCorrecta :
                nuevaClave = input("Ingrese nueva contraseña: ")
                if len(nuevaClave) < 6 :
                    print("La contraseña debe tener al menos 6 caracteres")
                if len(nuevaClave) >= 6 :
                    nuevaClaveConfirmacion = input("Confirme la nueva contraseña: ")
                    if nuevaClave == nuevaClaveConfirmacion:
                        print("Contraseña cambiada con exito")
                        claveActual = nuevaClave
        
        elif opcion == "3" :
            print("¡¡Manten la constancia y alcanzaras tus metas academicas!!")
        
        elif opcion == "4" :
            loged = False
        
        else :
            print("No existe opcion, intente nuevamente ( numero del 1 al 4 )")







