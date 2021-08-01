class Basico:
    
    def numerosN1(self,n):
        print("Números del 1 al {}" .format(n))
        for i in range(1, n+1): 
            print(i)
        
    def multiplo(self,num,multiplo):
        """Comprueba si un número es multiplo de otro"""
        if num % multiplo == 0:
            return "El numero {} es multiplo de {}".format(num,multiplo)
        else:
            return "El numero {} no es multiplo de {}".format(num,multiplo)
    
    def divisoresNumero(self,num):
        div = []
        for i in range(1, num):
            if num % i == 0: 
                div.append(i)
        print("Los divisores del numero {} son: {}" .format(num, div))
        return div
    
    def primo(self,num):
        acum = 0
        for i in range(1, num+1):
            if (num % i) == 0:
                acum += 1
        if acum == 2: return True
        else: 
            return False
        
    def perfecto(self,num):
        acu=0
        for contador in range(1,num):
            rec= num % contador
            if rec == 0:
                acu+= contador
        if acu == num:
            return "El número: {} es Perfecto".format(num)
        else:
            return "El número: {} no es Perfecto".format(num)
        
class Intermedio(Basico):

    def numerosN(self,n):
        acum = 0
        for i in range(1,n+1):
            acum += i
        return "La suma de 1 hasta {} es de: {}" .format(n, acum)
    
    def factorial(self,num):
        fact=1
        for i in range(1, num+1):
            fact *= i
            print("El factorial del número {} es: {}".format(num, fact))
        return fact
    
    def fibonacci(self,n):
        a=1
        b=1
        if n==1:
            print('0')
        elif n==2:
           print('0','1')
        else:
            print('0')
            print(a)
            print(b)
            for i in range(n-2):
                total = a + b
                b=a
                a= total
                print(total)
    
    def primosGemelos(self, n1, n2):
        if super().primo(n1) == "El numero {} es primo".format(n1):
            pass
        else: 
            print("El numero {} no es primo".format(n1))
        if super().primo(n2) == "El numero {} es primo".format(n2):
            pass
        else: 
            print("El numero {} no es primo".format(n2))

        if n1 > n2: 
            aux = n1 - n2
        else: 
            aux = n2 - n1
        if aux == 2: 
            return "Los numeros {} ; {} son primos gemelos".format(n1, n2)
        else: 
            return "Los numeros {} ; {} no son primos gemelos".format(n1, n2)
        
    def amigos(self,n1, n2):
        div_n1 = super().divisoresNumero(n1)
        print(div_n1)
        div_n2 = super().divisoresNumero(n2)
        acu1= 0
        acu2= 0
        for i in div_n1: 
            acu1 += i
        for j in div_n2: 
            acu2 += j
        if acu1==n2 and acu2 == n1: 
            return "El {} ; {} son números amigos".format(n1,n2)
        else: 
            return "El {} ; {} no son números amigos".format(n1,n2)
 