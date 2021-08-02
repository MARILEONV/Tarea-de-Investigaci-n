class Calculadora: 
    def __init__(self, n1, n2):
        self.n1= n1
        self.n2= n2
    
    def suma(self):
        return "El resultado de la suma es: {}+{}={}".format(self.n1,self.n2,self.n1 + self.n2)
    
    def resta(self):
        if self.n1 > self.n2 : 
            return "El resultado de la resta es: {}-{}={}" .format(self.n1,self.n2,self.n1 - self.n2)
        else: 
            return "El resultado de la resta es: {}-{}={}" .format(self.n2,self.n1,self.n2 - self.n1)

    def multiplicacion(self):
        multi= self.n1 * self.n2
        return "El resultado de la multiplicación es {}*{}={}".format(self.n1,self.n2,multi)
    
    def division(self):
        while True:
            if self.n2 != 0:
                return "El resultado de la división es: {}/{}={}".format(self.n1, self.n2,self.n1 / self.n2)
            elif self.n2 == 0:
                return "El valor no es correcto"

class CalEstandar(Calculadora):
    def __init__(self, n1, n2):
        super().__init__(n1,n2)

    
    def multiplicacion(self):
        multi= super().multiplicacion()
        return multi
    
    def exponente(self):
        exp = round((self.n1 ** self.n2), 2)
        return "El resultado de la exponenciación es: {}^{}={}" .format(self.n1, self.n2,exp)
    
    def valorAbsoluto(self, n):
        r= abs(n)
        return "El valor absoluto de {} es {}" .format(n, r)

class CalCientifica(Calculadora):
    PI= 3.1416
    
    def __init__(self, n1, n2):
        super().__init__(n1, n2)
    
    def circunferencia(self, radio):
        circunferencia = 2 * radio * CalCientifica.PI
        print("La circunferencia del circulo de radio {} es de: {} mts.".format(radio, circunferencia))

    def areaCirculo(self, radio):
        area_circunferencia = CalCientifica.PI * (radio ** 2)
        print("El area del circulo de radio {} es de: {} mts^2.".format(radio, area_circunferencia))

    def areaCuadrado(self, lado):
        area_cuadrado = lado * lado
        print("El area del cuadrado de lado {} es de: {} mts^2.".format(lado, area_cuadrado))
