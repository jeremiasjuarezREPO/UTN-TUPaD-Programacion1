# Ejercicio 4 — “Escape Room: La Bóveda”

#Variables iniciales
energia = 100
tiempo = 12
cerraduras_abiertas = 0
forzar_cerradura = 0
alarma = False
codigo_parcial = ""
nombre = ""

#Validacion nombre y acceso al menu del juego

while not nombre.isalpha():
    nombre = input("Ingrese su nombre: ")
    if not nombre.isalpha():
        print("Su nombre solo puede estar compuesto por letras ")

acceso = True

#Menu y evaluacion de la continuidad del juego dependiendo de las estadisticas

while acceso :

    if energia <= 0 or tiempo <= 0 :

        if tiempo <= 0 and energia <= 0 :
            print("Usted se quedo sin tiempo y sin energia ")
            print("Fin del juego ")
        
        elif energia <= 0 :
            print("Usted se quedo sin energia ")
            print("Fin del juego ")
        
        elif tiempo <= 0 :
            print("Usted se quedo sin tiempo ")
            print("Fin del juego ")
        
        acceso = False
        break

    if cerraduras_abiertas == 3 :
        print("¡VICTORIA! Ha logrado abrir la bobeda. ")
        break
        
    
    if alarma and tiempo <= 3 :
        print("Sistema Bloqueado por alarma ")
        print("Fin del juego ")

        acceso = False
        break
    
    print("Estadisticas: ")
    print(f" Energia: { energia } , Tiempo: { tiempo }, Cerraduras Abiertas: { cerraduras_abiertas }, Alarma: { 'Activada' if alarma else 'Apagada' }")

    print("--- Acciones ---")
    print("1. Forzar cerradura  (costo: -20 energía, -2 tiempo) ")
    print("2. Hackear panel  (costo: -10 energía, -3 tiempo) ")
    print("3. Descansar (costo: +15 energía (máx 100), -1 tiempo; si alarma ON: -10 energía extra) ")
    print("   ")
    opcion = input("Ingrese un numero del 1 al 3 dependiendo la accion que desee realizar: ")
    print("   ")

    while opcion not in ( "1", "2", "3" ):
        opcion = input("Ingrese un numero entre 1 y 3 para seleccionar una accion: ")
        print("   ")

#Logica Opcion 1 Forzar Cerradura

    while opcion.isdigit() and opcion == "1" :

        print("Usted opto por la opcion 1: Forzar Cerradura ")
        print("   ")

        if forzar_cerradura >= 2 :
            alarma = True
            energia -= 20
            tiempo -= 2
            print("Cerradura trabada, alarma activada ")
            print("   ")
            break

        while True :

            if alarma == True :
                print("No es posible forzar cerradura con la alarma activada ")
                print("   ")
                break
            
            if energia <= 40 :
                print("Hay riesgo de activar la Alarma ")
                intento_baja_energia = input("Ingrese un numero del 1 al 3 para forzar una cerradura: ")

                if not intento_baja_energia.isdigit() or intento_baja_energia not in ( "1" ,"2" ,"3" ) :
                    print("Ingrese un numero valido entre el 1 y el 3 ")
                    continue

                if intento_baja_energia == "3" :
                    print("Error al abrir la cerradura ")
                    print("Se ha disparado la alarma ")
                    alarma = True
                    energia -= 20
                    tiempo -= 2
                    forzar_cerradura += 1
                    break
                else :
                    print("Ha logrado abrir una cerradura correctamente ")
                    print("   ")
                    energia -= 20
                    tiempo -= 2
                    cerraduras_abiertas += 1
                    forzar_cerradura += 1
                    break
            
            elif energia > 40 :
                    print("Ha logrado abrir una cerradura correctamente ")
                    print("   ")
                    energia -= 20
                    tiempo -= 2
                    cerraduras_abiertas += 1
                    forzar_cerradura += 1
                    break

        opcion = ""

#Logica opcion 2 Hackear Panel

    while opcion.isdigit() and opcion == "2" :

        print("Usted opto por la opcion 2: Hackear panel ")
        print("   ")

        forzar_cerradura = 0
        energia -= 10
        tiempo -= 3

        for i in range(4) :
            match i:
                case 0:
                    print("Forzando ingreso al sistema...")
                case 1:
                    print("Ingresando al sistema...")
                case 2:
                    print("Buscando contraseñas...")
                case 3:
                    if len(codigo_parcial) >= 8 :
                        print("Contraseña encontrada con exito ")
                    else :
                        print("Contraseña parcial encontrada, pruebe intentando nuevamente ")        
            
            codigo_parcial += "C"
        
        if len(codigo_parcial) >= 8 :
            print("¡Felicitaciones! Ha logrado abrir una cerradura con exito ")
            print("  ")
            cerraduras_abiertas += 1
        else :
            print("No ha logrado abrir una cerradura ")
            print("  ")
        break

#Logica opcion 3 Descansar

    while opcion.isdigit() and opcion == "3" :

        print("Usted opto por la opcion 3: Descansar ")
        print("  ")

        if energia == 100 :
            print("La energia ya se encuentra al maximo, no es necesario descansar ")
            break

        forzar_cerradura = 0
        tiempo -= 1 

        if alarma :
            print("La alarma se encuentra activada, solo recupera 5 de energia ")
            print("  ")
            energia += 5
        else :
            print("Descanso satisfactorio, recuperas energia ")
            energia += 15
        
        if energia > 100 :
            energia = 100
        
        opcion = ""
        






