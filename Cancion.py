import matplotlib.pyplot as plot

class Cancion:
    #Constructor Cancion
    def __init__ (self, nombre, genero, anyo, autores, cantantes, letra):
        self.nombre = nombre
        self.genero = genero
        self.anyo = anyo
        self.autores = autores
        self.cantantes = cantantes
        self.letra = letra

    #Metodo que añade un autor a la lista
    def addAutor(self,autor):
        self.autores.append(autor)
    
    #Metodo que elimina un autor de la lista
    def deleteAutor(self,autor):
        self.autores.remove(autor)

    #Metodo que añade un cantante a la lista
    def addCantante(self,cantante):
        self.cantantes.append(cantante)
    
    #Metodo que elimina un cantante de la lista
    def deleteCantante(self,cantante):
        self.cantantes.remove(cantante)
    
    #Recorremos la lista de canciones, cada elemento es una linea de esta y la mostramos por pantalla
    def mostarCancion(self):
        for linea in self.letra:
            print(linea+ '\n')
    
    

    def mostrarHistograma(self):
        palabras ={}
        histograma = {}
        #Hacemos un diccionario con cada palabra y sus repeticiones
        for linea in self.letra:
            for palabra in linea.split():
                if(palabras.keys().__contains__(palabra)):
                    palabras[palabra] += 1
                else:
                    palabras[palabra] = 1
        #Obtenemos las 10 palabras mas utilizadas
        for elemento in range(10):
            if(len(palabras)>0):
                #Usamos esta función para saber la clave de la máxima
                mayor = max(palabras, key=palabras.get)
                histograma[mayor] = palabras[mayor]
                #Eliminamos del diccionario la clave máxima para que no coincida en la siguiente iteración
                palabras.pop(mayor)

        #Utilizamos la libreria matplotlib.pyplot para construir el histograma
        plot.title('Histograma de palabras')
        plot.xlabel('Palabras')
        plot.ylabel('Repeticiones')
        plot.plot(histograma.keys(), histograma.values(), 'ro')

        plot.show() #dibujamos el histograma    


