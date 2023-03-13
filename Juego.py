from Jugador1 import Jugador1
from Jugador2 import Jugador2
from Jugador1 import luchador
from Jugador2 import luchador2
class Juego(Jugador1,Jugador2):
    pass
    def Jugadores():
        return'Luchador {} su poder es {} vs Luchador {} su poder es {}'.format(luchador.nombre, luchador.poder, luchador2.nombre2, luchador2.poder2)

luchador1 = Juego
print(luchador1.Jugadores())
print("El luchador " + luchador.nombre + " lanza un ataque pierna del diablo ")
print("El luchador " + luchador2.nombre2 + " recibe el ataque y contra ataca con el uso de las 3 catanas")
print("El poder del luchador " + luchador2.nombre2 + " es de 70%")