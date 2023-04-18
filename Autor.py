
class Autor:
    
    #Constructor Autor
    def __init__(self, nombre, anyoNacimiento, canciones):
        self.nombre = nombre
        self.anyoNacimiento = anyoNacimiento
        self.canciones = canciones

    #Metodo que añade una cancion a la lista
    def addCancion(self,cancion):
        self.canciones.append(cancion)
    
    #Metodo que elimina una cancion de la lista
    def deleteCancion(self,cancion):
        self.canciones.remove(cancion)
    
    #Creamos un diccionario con el genero de la lista de canciones y sus repeticiones
    def obtenerCancionesGenero(self):
        cancionesGenero ={}
        for cancion in self.canciones:
            genero = cancion.genero
            if(cancionesGenero.keys().__contains__(genero)):
                cancionesGenero[genero] += 1
            else:
                cancionesGenero[genero] = 1

        return cancionesGenero
            

    




