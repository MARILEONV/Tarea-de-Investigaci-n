class Cadena:
    def __init__(self, cadena):
        self.cadena= cadena
    
    def recorrerCadena(self):
        for i in self.cadena:
            print(i)

    def buscarCaracter(self,buscado):
        p= self.cadena.find(buscado)
        return "El valor {} se encuentra en la posicion {}" .format(buscado,p)

    def listaPosiciones(self,caracter):
        lista=[]
        for idx,x in enumerate(self.cadena):
            if x==caracter:
                lista.append(idx)
        return "El caracter {} se encuentra en la posición: {}".format(caracter,lista)

    def listaPalabras(self):
        return self.cadena.split(" ")

    def cadenaLista(self):
        cad = self.cadena.split()
        print(cad)
        cadena=" ".join(cad)
        return "La cadena es: {}".format(cadena)

    def insertarDato(self,buscado, posicion):
        string= self.cadena.split()
        string.insert(posicion,buscado)
        fin_string= " ".join(string)
        return "La nueva cadena es: {}".format(fin_string)

    def eliminarOcurrencias(self,buscado):
        try: 
            while True:
                string= self.cadena.split()
                string.remove(buscado)
                break
        except:
            pass
        return "Cadena: {}".format(" ".join(string))

    def retornaValor(self,posicion):
        lista= list(self.cadena)
        if posicion<len(lista):
            lista.pop(posicion)
            self.cadena= " ".join(lista)
            return "La nueva cadena es: {}".format(self.cadena)
        else:
            return "La posicion {} no se encuentra en la cadena".format(posicion)

    def concatenarCadena(self,dato):
        return "Cadena: {}".format(self.cadena + ' ' + dato)

