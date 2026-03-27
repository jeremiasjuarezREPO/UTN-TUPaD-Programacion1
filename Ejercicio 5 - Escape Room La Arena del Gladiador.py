#Ejercicio 5 — “Escape Room:"La Arena del Gladiador"

while True :
    print("--- Bienvenido a la Arena ---")
    nombre = input("Ingrese el nombre de su Gladiador: ")
    if nombre.isalpha() :
        break
    else:
        print("Error: Solo se permiten letras ")
        continue

vida_del_gladiador = 50
vida_del_enemigo = 100
pociones_de_vida = 3
ataque_pesado = 15
ataque_enemigo = 12
turno_gladiador = True

while vida_del_enemigo > 0 and vida_del_gladiador > 0 :

    if turno_gladiador :
        
        print("-- Estadisticas actuales del juego --")
        print(f"Vida del Gladiador: { vida_del_gladiador } - Pociones restantes: { pociones_de_vida } ")
        print(f"Vida Enemigo: { vida_del_enemigo } ")
        print("   ")

        print("-- Menu de opciones del Gladiador --")
        print("   ")
        print("1. Ataque Pesado ")
        print("2. Ráfaga veloz ")
        print("3. Curar ")


        while True :
            accion = input("Indique con un numero del 1 al 3 que acción desea realizar: ")

            if accion.isdigit() :
                match accion:
                    case "1" :
                        break
                    case "2" :
                        break
                    case "3" :
                        break
                    case _ :
                        print("Opción Errónea ")
                        continue
            else :
                print("Opción Errónea ")

        if accion == "1" :
            print("Usted eligió la opcion 1: Ataque Pesado ")

            if vida_del_enemigo < 20 :
                vida_del_enemigo = vida_del_enemigo - ( ataque_pesado * 1.5 )
                print( f"¡¡Atacaste al enemigo con un golpe crítico por { ataque_pesado * 1.5 } puntos de daño!! ")
                print("   ")
            else :
                vida_del_enemigo = vida_del_enemigo - ataque_pesado
                print( f"Atacaste al enemigo por { ataque_pesado } puntos de daño ")
                print("   ")

        if accion == "2" :
            print("Usted eligió la opcion 2: Ráfaga Veloz ")

            for i in range(3) :
                print("¡Golpeaste al enemigo por 5 puntos de daño!")
                vida_del_enemigo -= 5

        if accion == "3" :
            print("Usted eligió la opcion 3: Curar ")
            
            if pociones_de_vida <= 0 :
                print("¡No quedan pociones! ")
            else :
                vida_del_gladiador += 30
                pociones_de_vida -= 1
                if vida_del_gladiador >= 100 :
                    vida_del_gladiador = 100
        
        if vida_del_enemigo > 0 :

            vida_del_gladiador -= 12
            print("   ")
            print("Turno del enemigo ")
            print("El enemigo ataca por 12 puntos de daño al Gladiador, pierdes 12 puntos de vida ")
            print("   ")
        
        if vida_del_enemigo <= 0 :
            print(f"¡VICTORIA! { nombre } ha ganado la batalla ")
        elif vida_del_gladiador <= 0 :
            print(f"DERROTA. Has caído en combate")
            break
