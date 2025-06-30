import random

historial_resultados = []

def guardar_resultado(resultado):
    historial_resultados.append(resultado)
    print(f"Guardado: {resultado}")  

def mostrar_menu():
    print("Bienvenido al juego de piedra, papel o tijera, elige una opción")
    print("MENÚ PRINCIPAL")
    print("1. Jugar")
    print("2. Ver las reglas del juego")
    print("3. Salir")

def reglas():
    print("REGLAS DEL JUEGO:")
    print("1. Piedra le gana a tijera")
    print("2. Tijera le gana a papel")
    print("3. Papel le gana a piedra")
    print("4. Si ambos jugadores eligen la misma opción, es un empate")

def jugar():
    print("Selecciona el modo de juego:")
    print("1. Jugar contra la PC")
    print("2. Jugar contra otro jugador")
    modo = input("Elige 1 o 2: ")
    if modo == "1":
        jugar_PC()
    elif modo == "2":
        multijugador()
    else:
        print("Opción no válida")

def jugar_PC():
    print("JUEGO CONTRA LA PC")
    opciones = ["piedra", "papel", "tijera"]
    while True:
        eleccion = input("Elige piedra, papel o tijera: ").lower()
        if eleccion not in opciones:
            print("Opción no válida, intenta de nuevo.")
            continue

        eleccion_pc = random.choice(opciones)
        print("La PC ha elegido:", eleccion_pc)

        if eleccion == eleccion_pc:
            resultado = "empate"
            print("Empate")
        elif (eleccion == "piedra" and eleccion_pc == "tijera") or (eleccion == "papel" and eleccion_pc == "piedra") or (eleccion == "tijera" and eleccion_pc == "papel"):
            resultado = "ganaste"
            print("¡Ganaste!")
        else:
            resultado = "perdiste"
            print("Perdiste")

        guardar_resultado(resultado)
        print(f"Historial actual: {historial_resultados}")

        seguir = input("¿Deseas jugar de nuevo? (si/no): ").lower()
        if seguir != "si":
            break

def multijugador():
    print("MODO MULTIJUGADOR")
    opciones = ["piedra", "papel", "tijera"]
    while True:
        jugador1 = input("Jugador 1, elige piedra, papel o tijera: ").lower()
        jugador2 = input("Jugador 2, elige piedra, papel o tijera: ").lower()

        if jugador1 not in opciones or jugador2 not in opciones:
            print("Opción no válida, intenten de nuevo")
            continue

        if jugador1 == jugador2:
            resultado = "empate"
            print("Empate")
        elif (jugador1 == "piedra" and jugador2 == "tijera") or (jugador1 == "papel" and jugador2 == "piedra") or (jugador1 == "tijera" and jugador2 == "papel"):
            resultado = "gana el jugador 1"
            print("¡Gana el Jugador 1!")
        else:
            resultado = "gana el jugador 2"
            print("¡Gana el Jugador 2!")

        guardar_resultado(resultado)
        print(f"Historial actual: {historial_resultados}")

        seguir = input("¿Desean jugar otra vez? (si/no): ").lower()
        if seguir != "si":
            break

def mostrar_resumen():
    print("RESUMEN FINAL")
    print(f"Lista de resultados: {historial_resultados}")
    print(f"Total partidas jugadas: {len(historial_resultados)}")
    print(f"Ganaste (vs PC): {historial_resultados.count('ganaste')}")
    print(f"Perdiste (vs PC): {historial_resultados.count('perdiste')}")
    print(f"Gana el jugador 1 (multijugador): {historial_resultados.count('gana el jugador 1')}")
    print(f"Gana el jugador 2 (multijugador): {historial_resultados.count('gana el jugador 2')}")
    print(f"Empates: {historial_resultados.count('empate')}")
    print("Gracias por jugar. ¡Adiós!")


name = input("Ingresa tu nombre o alias: ")
while name.strip() == "":
    print("Error, no escribiste tu nombre")
    name = input("Por favor, escribe tu nombre o alias: ")

while True:
    mostrar_menu()
    opcion = input("Escribe tu opción (1/2/3): ")

    if opcion == "1":
        jugar()
    elif opcion == "2":
        reglas()
    elif opcion == "3":
        mostrar_resumen()
        break
    else:
        print("Opción no válida. Intenta otra vez.")