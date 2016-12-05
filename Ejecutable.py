from Electrodomestico import Electrodomestico
from Television import Television
from Lavadora import Lavadora
class Ejecutable:
    def exe(self):
        listaElectrodomesticos=[]

        listaElectrodomesticos.append(Electrodomestico(200, 60, 'C', "Verde"))
        listaElectrodomesticos.append(Lavadora(150, 30))
        listaElectrodomesticos.append(Television(500, 80, 'E', "negro", 42, False))
        listaElectrodomesticos.append(Electrodomestico())
        listaElectrodomesticos.append(Electrodomestico(600, 20, 'D', "gris"))
        listaElectrodomesticos.append(Lavadora(300, 40, 'Z', "blanco", 40))
        listaElectrodomesticos.append(Television(250, 70))
        listaElectrodomesticos.append(Lavadora(400, 100, 'A', "verde", 15))
        listaElectrodomesticos.append(Television(200, 60, 'C', "naranja", 30, True))
        listaElectrodomesticos.append(Electrodomestico(50, 10))

        sumaElectrodomesticos=0;
        sumaTelevisiones=0;
        sumaLavadoras=0;

        for i in listaElectrodomesticos:
            if(isinstance(i,Electrodomestico)):
                sumaElectrodomesticos+=i.precioFinal()
            if(isinstance(i,Lavadora)):
                sumaLavadoras+=i.precioFinal()
            if(isinstance(i,Television)):
                sumaTelevisiones+=i.precioFinal()


        print("La suma del precio de los electrodomesticos es de "+str(sumaElectrodomesticos))
        print("La suma del precio de las lavadoras es de "+str(sumaLavadoras))
        print("La suma del precio de las televisiones es de "+str(sumaTelevisiones))
        print(str(Television(200, 60, 'C', "naranja", 30, True).precioFinal()))

eje=Ejecutable()
eje.exe()