from Electrodomestico import  Electrodomestico
class Television(Electrodomestico):
    CARGA_DEF=5;

    def __init__(self,precioBase=10,peso=10,consumoEnergetico='F',color='blanco',resolucion=20,fourK=False):
        super(Television, self).__init__(precioBase,peso,consumoEnergetico,color)
        self.resolucion=resolucion
        self.fourK=fourK

    #Métodos publicos
    def __getReolucion(self):
        return self.resolucion

    def __getfourK(self):
        return self.fourK

    def precioFinal(self):
        self.plus=Electrodomestico.precioFinal(self)
        if (self.resolucion>40):
            aux=(self.precioBase/100)*30
            self.plus+=aux
        if(self.fourK==True):
            self.plus+=50
        return self.plus