from Estudiantes import Estudiantes
from Materias import Materias
from Estudiantes import DatosEstudiantes

class Notas(Estudiantes, Materias):

    def __init__(self, notasLab, notasPar):
        self.notasLab = notasLab
        self.notasPar = notasPar
    
    def registroNotas(self):
        return 'notas del estudiante {} en la materia de {} son: la nota del laboratorio es: {}, y la nota del parcial es: {}'.format(DatosEstudiantes.nombre3, Materias.nombre, self.notasLab, self.notasPar)
    

DatosNotas = Notas(8.8, 10)
print(DatosNotas.registroNotas())

