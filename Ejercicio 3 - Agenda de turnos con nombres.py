# Ejercicio 3 (Alta) — “Agenda de Turnos con Nombres (sin listas)”

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""

martes1 = ""
martes2 = ""
martes3 = ""

turnosLunes = 0
turnosMartes = 0
loged = True

while True:
    operador = input("Ingrese nombre del operador: ")
    if operador.isalpha():
        loged = True
        break
    else:
        print("El nombre del operador solo puede estar compuesto por letras ")

while loged :
    print("---Menu---")
    print("  ")
    print("1. Reservar turno ")
    print("2. Cancelar turno ( por nombre ) ")
    print("3. Ver agenda del dia ")
    print("4. Ver resumen general ")
    print("5. Cerrar sistema ")
    print("  ")
    opcion = input("Elija una opcion: ")

#reservar

    if opcion == "1" :
        print("Elija un dia. Utilice el n° 1 para Lunes y el n° 2 para Martes: ")
        dia = input("Dia: ")
        
        while dia != "1" and dia != "2":
            print("Dia incorrecto, debe ingresar 1 para Lunes y 2 para Martes: ")
            dia = input("Dia: ")

        while True :
            paciente = input("Indique nombre del paciente: ")
            if paciente.isalpha() :
                break
            else:
                print("Error al ingresar nombre del paciente, asegurese de que este compuesto solo por letras ")
        
        if dia == "1":
            if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4 :
                print(f"{ paciente } ya posee un turno agendado el dia Lunes ")
            else :
                if lunes1 == "":
                    lunes1 = paciente
                    turnosLunes += 1
                    print("Turno guardado exitosamente ")

                elif lunes2 == "" :
                    lunes2 = paciente
                    turnosLunes += 1
                    print("Turno guardado exitosamente ")

                elif lunes3 == "" :
                    lunes3 = paciente 
                    turnosLunes += 1
                    print("Turno guardado exitosamente ")

                elif lunes4 == "" :
                    lunes4 = paciente
                    turnosLunes += 1
                    print("Turno guardado exitosamente ")

                else :
                    print("No hay mas turnos disponibles el dia Lunes ")

        if dia == "2" :
            if paciente == martes1 or paciente == martes2 or paciente == martes3 :
                print(f"{ paciente } ya posee un turno agendado el dia Martes ")
            else :
                if martes1 == "":
                    martes1 = paciente
                    turnosMartes += 1
                    print("Turno guardado exitosamente ")

                elif martes2 == "" :
                    martes2 = paciente
                    turnosMartes += 1
                    print("Turno guardado exitosamente ")

                elif martes3 == "" :
                    martes3 = paciente 
                    turnosMartes += 1
                    print("Turno guardado exitosamente ")

                else :
                    print("No hay mas turnos disponibles el dia Martes ")


#cancelar

    elif opcion == "2" :
        print("Elija un dia. Utilice el n° 1 para Lunes y el n° 2 para Martes: ")
        dia = input("Dia: ")
        
        while dia != "1" and dia != "2":
            print("Dia incorrecto, debe ingresar 1 para Lunes y 2 para Martes: ")
            dia = input("Dia: ")

        while True :
            paciente = input("Indique nombre del paciente: ")
            if paciente.isalpha() :
                break
            else:
                print("Error al ingresar nombre del paciente, asegurese de que este compuesto solo por letras ")

        if dia == "1" :
            if paciente == lunes1 :
                lunes1 = ""
                turnosLunes -= 1
                print("Turno eliminado con exito")

            elif paciente == lunes2 :
                lunes2 = ""
                turnosLunes -= 1
                print("Turno eliminado con exito")

            elif paciente == lunes3 :
                lunes3 = ""
                turnosLunes -= 1
                print("Turno eliminado con exito")

            elif paciente == lunes4 :
                lunes4 = ""
                turnosLunes -= 1
                print("Turno eliminado con exito")

            else :
                print("El paciente no posee un turno reservado")

        elif dia == "2" :
            if paciente == martes1 :
                martes1 = ""
                turnosMartes -= 1
                print("Turno eliminado con exito")

            elif paciente == martes2 :
                martes2 = ""
                turnosMartes -= 1
                print("Turno eliminado con exito")

            elif paciente == martes3 :
                martes3 = ""
                turnosMartes -= 1
                print("Turno eliminado con exito")

            else :
                print("El paciente no posee un turno reservado")

#ver agenda

    elif opcion == "3" :
        print("Elija un dia. Utilice el n° 1 para Lunes y el n° 2 para Martes: ")
        dia = input("Dia: ")
        
        while dia != "1" and dia != "2":
            print("Dia incorrecto, debe ingresar 1 para Lunes y 2 para Martes: ")
            dia = input("Dia: ")

        if dia == "1" :

            if lunes1 == "" :
                print( "Lunes - Turno 1 : libre ")
            else :
                print( f"Lunes - Turno 1 : { lunes1 }")
            
            if lunes2 == "" :
                print( "Lunes - Turno 2 : libre ")
            else :
                print( f"Lunes - Turno 2 : { lunes2 }")

            if lunes3 == "" :
                print( "Lunes - Turno 3 : libre ")
            else :
                print( f"Lunes - Turno 3 : { lunes3 }")

            if lunes4 == "" :
                print( "Lunes - Turno 4 : libre ")
            else :
                print( f"Lunes - Turno 4 : { lunes4 }")

        if dia == "2" :

            if martes1 == "" :
                print( "Martes - Turno 1 : libre ")
            else :
                print( f"Martes - Turno 1 : { martes1 }")
            
            if martes2 == "" :
                print( "Martes - Turno 2 : libre ")
            else :
                print( f"Martes - Turno 2 : { martes2 }")

            if martes3 == "" :
                print( "Martes - Turno 3 : libre ")
            else :
                print( f" Martes - Turno 3 : { martes3 }")

#resumen general

    elif opcion == "4" :
        print(f"El lunes hay agendados { turnosLunes }")
        print(f"El martes hay agendados { turnosMartes }")
    
        if turnosLunes > turnosMartes :
            print("El dia lunes tiene mas turnos agendados")
        elif turnosLunes < turnosMartes :
            print("El dia martes tiene mas turnos agendados")
        elif turnosLunes == 0 and turnosMartes == 0 :
            print("Todavia no hay turnos agendados")
        elif turnosLunes == turnosMartes :
            print("Hay la misma cantidad de turnos agendados tanto el dia lunes como el dia martes")

#Cerrar sistema

    elif opcion == "5" :
        loged = False
        print("Se cerro el sistema")

# manejo menu incorrecto
    else :
        print("Ingrese un indice valido ( numero del 1 al 5 )")

