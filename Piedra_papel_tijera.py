# Programa para simular el juego piedra papel o tijera
print("--------------------------------------")
print("-------PIEDRA PAEL O TIJERA-----------")
print("--------------------------------------")
import random

# processing 
maquina = random.randint(1,3)

# maquina = random.randint(1,3)

jugador = int(input("DIGITE LA OPCION:"))

if (maquina==1): # PIEDRA
    if (jugador==1):
        Rta = "Empate"
    elif (jugador==2):
        Rta = "Ganaste!"
    else:
        Rta = "PERDISTE"

if (maquina==2): # PAPEL
    if (jugador==2):
        Rta = "Empate"
    elif (jugador==3):
        Rta = "Ganaste!"
    else: 
        Rta = "PERDISTE"

if (maquina==3): # TIJERAS
    if (jugador==3):
        Rta = "Empate"
    elif (jugador==1):
        Rta = "Ganaste!"
    else:
        Rta = "PERDISTE"

    

# output
print
