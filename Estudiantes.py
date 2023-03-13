class Estudiantes:
    def __init__(self, nombre1, nombre2, nombre3, carrera):
        self.nombre1 = nombre1
        self.nombre2 = nombre2
        self.nombre3 = nombre3
        self.carrera = carrera

    def registroestudiantes(self):
        return ' El nombre del primer estudiante es : {} su carrera es: {} nombre del segundo estudiante {} su carrera es: {} nombre del tercer estudiante {} su carrera {}'.format(self.nombre1,self.carrera, self.nombre2, self.carrera, self.nombre3, self.carrera)
    

DatosEstudiantes= Estudiantes ("juan", "Luis", "pancho", "ingeniera en desarrollo de sofware")
print(DatosEstudiantes.registroestudiantes())