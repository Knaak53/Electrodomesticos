class Electrodomestico:
    precioConsumo={'A':100,'B':80,'C':60,'D':50,'E':30,'F':10}
    def __init__(self, precio=100,peso=10,consumo='F',color='blanco'):
        self.precioBase=precio
        self.color=color
        self.__comprobarConsumoEnergetico(consumo)
        self.consumoEnergetico=consumo
        self.peso=peso
    #metodos
    def getPrecio(self):
        return self.precioBase
    def getColor(self):
        return self.color
    def getConsumo(self):
        return self.consumoEnergetico
    def getPeso(self):
        return self.peso
    def __comprobarConsumoEnergetico(self, letra):
        if letra < 'A' or letra > 'F':
            self.consumoEnergetico='F'
        else:
            self.consumoEnergetico=letra
    def __comprobarColor(self, color):
        if color != 'blanco' or color != 'negro' or color != 'rojo' or color != 'azul' or color != 'gris':
            self.color = 'blanco'
        else:
            self.color = color

    def precioFinal(self):
        if (self.consumoEnergetico== 'A'):
            precioBase = self.precioBase + 100
        if (self.consumoEnergetico == 'B'):
            precioBase = self.precioBase + 80
        if (self.consumoEnergetico == 'C'):
            precioBase = self.precioBase + 60
        if (self.consumoEnergetico== 'D'):
            precioBase = self.precioBase + 50
        if (self.consumoEnergetico == 'E'):
            precioBase = self.precioBase + 30
        if (self.consumoEnergetico== 'F'):
            precioBase = self.precioBase + 10
        if (19 >= self.peso > 0):
            precioBase = self.precioBase + 10
        if (49 >= self.peso >= 20):
            precioBase = self.precioBase + 50
        if (79 >= self.peso >= 50):
            precioBase = self.precioBase + 80
        if (self.peso >= 80):
            precioBase = self.precioBase + 100
        return precioBase