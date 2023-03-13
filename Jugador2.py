class Jugador2:
    def __init__(self, nombre2, poder2):
        self.nombre2 = nombre2
        self.poder2 = poder2
    
    def DatosJugador2(self):
        return'El nombre del luchador es {} con un poder de {}%'.format(self.nombre2, self.poder2)
        
luchador2 = Jugador2('Zoro', 100)
print(luchador2.DatosJugador2())