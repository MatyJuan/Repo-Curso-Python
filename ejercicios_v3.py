#Ejercicios Diccionarios --> https://ellibrodepython.com/diccionarios-en-python

#Ejercicio 1
"""
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}.
Preguntar al usuario por una divisa y muestre su símbolo o un mensaje de aviso si la divisa no está en el diccionario.
"""

def divisas():
    lista_divisa = {'euro':'€', 'dollar':'$', 'yen':'¥'}
    x=input("escriba su divisa ")
    if x in lista_divisa:
            print(lista_divisa[x])
    else:print("la divisa no está en el diccionario")

divisas()


#Ejercicio 2
"""
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario.
Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.

"""


#Ejercicio 3
"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla.
Preguntar al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
    Fruta	    Precio
    Plátano	    1.35
    Manzana	    0.80
    Pera	    0.85
    Naranja	    0.70
"""


#Ejercicio 4
"""
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla.
Preguntar al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos de fruta.
Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
    Fruta	    Precio
    Plátano	    1.35
    Manzana	    0.80
    Pera	    0.85
    Naranja	    0.70
"""


#Ejercicio 5
"""
Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} 
Después muestre por pantalla los créditos de cada asignatura en el formato <asignatura> tiene <créditos> créditos, 
donde <asignatura> es cada una de las asignaturas del curso, y <créditos> son sus créditos. 
Al final debe mostrar también el número total de créditos del curso.
"""

