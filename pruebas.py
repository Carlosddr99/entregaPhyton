from Autor import Autor 
from Cancion import Cancion
from Cantante import Cantante

#Creamos varios objetos para hacer las pruebas
canciones = ['Vas a quedarte', 'Un beso', 'Diamonds', 'Malamente']
cantantes = ['Aitana', 'Rosalia', 'Rauw Alejandro', 'Rihanna']
autores1 = ["Juan Pablo Villamil", "Juan Pablo Isaz"]
autores1 = ["Sia FurlerBenjamin", "Erik Hermansen"]

cancion1 = Cancion(canciones[0], "Pop", 2018, [autores1[0], autores1[1], cantantes[0]], [cantantes[0]], 
["Vas a quedarte","Porque te juro que esta vez voy a cuidarte", "A nuestra historia le hace falta una segunda parte",
"Aunque nos digan que eso nunca sale bien", "Vas a quedarte", "Yo haré de todo por volver a enamorarte",
"Yo tengo miedo porque nunca pude reemplazarte", "Y si lo intentas te prometo que esta vez", "Vas a quedarte",
"Yo que me acostumbré a estar arrepentida", "Sigo esperando a que llegue el día"])

cancion2 = Cancion(canciones[1], "Pop urbano", 2023, [cantantes[1], cantantes[2]], [cantantes[1], cantantes[2]], 
["Yo ya necesito otro beso","Uno de esos que tú me das"])

cancion3 = Cancion(canciones[2], "Pop electrónico", 2012, [autores1[0], autores1[1]], [cantantes[3]], 
["Shine bright like a diamonds","Shine bright in a beuatiful sea"])

cancion4 = Cancion(canciones[3], "Flamenco", 2017, ["Pablo Díaz Reixa", cantantes[1]], [cantantes[1]], 
["Ese cristalito roto","Yo sentí como crujía", "Antes de caerse al suelo"])

#PRUEBAS CLASE CANCION

#probamos el añadir Autor
cancion1.addAutor(cantantes[1])
print(cancion1.autores)

#probamos el eliminar Autor
cancion1.deleteAutor(cantantes[1])
print(cancion1.autores)

#probamos el añadir Cantante
cancion1.addCantante(cantantes[2])
print(cancion1.cantantes)

#probamos el eliminar Cantante
cancion1.deleteCantante(cantantes[2])
print(cancion1.cantantes)

#Mostramos la letra de la cancion
cancion1.mostarCancion()

#Hacemos un histograma de las palabras más repetidas de la canción
cancion1.mostrarHistograma()

#PRUEBAS CLASE CANTANTE
rosalia = Cantante(cantantes[0], 1992, [cancion1])
print(rosalia.canciones)

#probamos el añadir Cancion al Cantante
rosalia.addCancion(cancion4)
rosalia.addCancion(cancion1)
print(rosalia.canciones)

#probamos el eliminar Cancion al Cantante
rosalia.deleteCancion(cancion1)
print(rosalia.canciones)

#obtenemos las canciones de cada genero y sus repeticiones
print(rosalia.obtenerCancionesGenero())

#PRUEBAS CLASE AUTOR
villamil = Autor(autores1[0], 1994, [cancion1])
print(villamil.nombre)

#probamos el añadir Cancion al Autor
villamil.addCancion(cancion3)
villamil.addCancion(cancion2)
print(villamil.canciones)

#obtenemos las canciones de cada genero y sus repeticiones
print(villamil.obtenerCancionesGenero())

#probamos el eliminar Cancion al Autor
villamil.deleteCancion(cancion1)
print(rosalia.canciones)

