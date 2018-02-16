class Mascota(object):
    def __init__(self, nombre):
        self.nombre = nombre

    def printName(self):
        print "Nombre: ",self.nombre

class Perro(Mascota):
    def __init__(self, nombre):
        super(Perro, self).__init__(nombre)
        self.patas = 4
        self.nombre = nombre

class Raza(Perro):
    def __init__(self, nombre, raza):
        super(Raza, self).__init__(nombre)
        self.raza = raza

    def printRaza(self):
        print self.raza

perro = Raza("Toby", "Golden")
perro.printName()
perro.printRaza()