import random

# ==============================
# MARCADOR (Diccionario)
# ==============================

marcador = {
    "victorias": 0,
    "derrotas": 0,
    "empates": 0
}

# ==============================
# LISTA DE OPCIONES
# ==============================

opciones = ["piedra", "papel", "tijera"]

# ==============================
# TUPLA CON LAS REGLAS DEL JUEGO
# Cada tupla representa una
# combinación ganadora.
# ==============================

reglas = (
    ("piedra", "tijera"),
    ("papel", "piedra"),
    ("tijera", "papel")
)

# ==============================
# LISTA PARA GUARDAR EL HISTORIAL
# ==============================

historial = []

print("=================================")
print("     PIEDRA, PAPEL O TIJERA")
print("=================================")

while True:

    jugador = input("\nElige Piedra, Papel o Tijera: ").lower()

    if jugador not in opciones:
        print("Opción no válida. Intenta nuevamente.")
        continue

    computadora = random.choice(opciones)

    print(f"\nTu elección: {jugador}")
    print(f"Elección de la computadora: {computadora}")

    # Determinar el ganador

    if jugador == computadora:

        resultado = "Empate"
        print("¡Empate!")

        marcador["empates"] += 1

    elif (jugador, computadora) in reglas:

        resultado = "Victoria"
        print("¡Ganaste!")

        marcador["victorias"] += 1

    else:

        resultado = "Derrota"
        print("¡Perdiste!")

        marcador["derrotas"] += 1

    # Guardar el historial de la partida

    historial.append((jugador, computadora, resultado))

    # Mostrar marcador

    print("\n----- MARCADOR -----")

    print(f"Victorias: {marcador['victorias']}")
    print(f"Derrotas : {marcador['derrotas']}")
    print(f"Empates  : {marcador['empates']}")

    jugar_otra = input("\n¿Deseas jugar otra vez? (s/n): ").lower()

    if jugar_otra != "s":
        break

print("\n=================================")
print("      JUEGO FINALIZADO")
print("=================================")

print(f"Victorias: {marcador['victorias']}")
print(f"Derrotas : {marcador['derrotas']}")
print(f"Empates  : {marcador['empates']}")

print("\n===== HISTORIAL DE PARTIDAS =====")

for numero, partida in enumerate(historial, start=1):

    jugador, computadora, resultado = partida

    print(f"\nPartida {numero}")
    print(f"Jugador     : {jugador}")
    print(f"Computadora : {computadora}")
    print(f"Resultado   : {resultado}")

print("\n¡Gracias por jugar!")