from Electrodomestico import  Electrodomestico
class Lavadora(Electrodomestico):
    CARGA_DEF=5;

    def __init__(self,precioBase=10,peso=10,consumoEnergetico='F',color='blanco',carga=CARGA_DEF):
        super(Lavadora, self).__init__(precioBase,peso,consumoEnergetico,color)
        self.carga=carga

    #Métodos publicos
    def __getCarga(self):
        return self.carga

    def precioFinal(self):
        self.plus=Electrodomestico.precioFinal(self)
        if (self.carga>30):
            self.plus+=50
        return self.plus