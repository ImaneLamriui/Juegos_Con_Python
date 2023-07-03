import random

def piedra_papel_tijera():

    print("*****************************")
    print("   ¡Bienvenido al Juego!     ")
    print("*****************************")

    jugador = input("elije p para piedra,pa para papel y t para tijera: \n").lower()
    laptop = random.choice(['p', 'pa', 't'])
    # Piedra gana a tijera, Papel gana a piedra, Tijera gana a papel
    if jugador == laptop:
        return '¡Empate!'
    elif ((jugador=='p' and laptop=='t') or (jugador=='pa' and laptop=='p') or(jugador=='t' and laptop=='pa')):
        return '¡Ganaste!,  :' + laptop
    else:
        return '¡Perdiste! ,  laptop ha eligido :' +laptop
       
print(piedra_papel_tijera())
