from Categorias import Categorias
from Categorias import categorias
class Peliculas(Categorias):
    def __init__(self, datos, datos2, datos3, datos4):
        self.datos = datos
        self.dato2 = datos2
        self.dato3 = datos3
        self.dato4 = datos4

    def nomPeliculas(self):
        categorias1 = categorias.categoria1
        categorias2 = categorias.categoria2
        categorias3 = categorias.categoria3
        if categorias1 == self.datos:
            print("Pelicula de romance: " + objeto.dato2)
        else:
            if categorias2 == self.datos:
                print("Pelicula de comedia: " + objeto.dato3)
            else:
                if categorias3 == self.datos:
                    print("Pelicula de anime: " + objeto.dato4)
                else:
                    print("Error")
        

objeto = Peliculas("Anime", "propuesta laboral", "tom y jeey", "amor de gata")
print(objeto.nomPeliculas())