# Ejercicio 1
# Escribir un funcion que pregunte al usuario su edad y muestre por pantalla si es mayor de edad o no.
# Para realizar este ejercicio necesitamos conocer la funcion nativa de python input()
# Documentacion --> https://www.w3schools.com/python/ref_func_input.asp
# Tener en cuenta que la funcion input retorna un string, por lo que tenemos que convertirlo a entero(int)

# def funcion1():
#     edad = int(input("Ingrese su edad: "))
#     if edad >= 18:
#         print("Es mayor de edad :",edad)
#     else:
#         print("Es menor de edad :",edad)
# funcion1()

# funcion1() #ejecuta la funcion

# Ejercicio 2
# Escribir una funcion que pida al usuario una palabra y la muestre por pantalla 10 veces.
# def funcion1():
#     palabra= input("Inserte una palabra")
#     print(palabra)
#     for x in range(10):
#         print(palabra)
# funcion1()


# Ejercicio 3
# Escribir un funcion que pregunte al usuario un número que represente un mes, escribir el nombre del mes correspondiente.
# Para realizar este ejercicio tenemos que utilizar los indices de una lista: 
# Documentacion --> https://www.programiz.com/python-programming/list
# Puede haber error en el número dado.
# meses = [ 'enero' ,'febrero' ,'marzo' ,'abril' ,'mayo' ,'junio' ,'julio' ,'agosto' ,'septiembre' ,'octubre' ,'noviembre' ,'diciembre'] 

# def funcion1():
#     numero= int(input("Que mes representa el numero "))
#     for numero in meses():
#         print(numero)

# funcion1()


# Ejercicio 4
# Escribir una funcion que pida al usuario ingresar tres números. La funcion debera hallar el mayor numero y lo muestrarlo por pantalla.

# def funcion1():
#     numero = input("Ingresar 3 numeros ")
#     n = max(numero)
#     max(numero)
#     print(n)
# funcion1()

# Ejercicio 5
# Escribir una funcion que almacene la cadena de caracteres "contraseña" en una variable
# Pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada 
# sin tener en cuenta mayúsculas y minúsculas.

# def funcion():
#     key = "contraseña"
#     password = input("Introducir contraseña: ")
#     if key == password.lower():
#         print("La contraseña coincide")
#     else:
#         print("La contraseña no coincide")
# funcion()


# Ejercicio 6
# Teniendo la siguiente lista de barrios:
# barrios_caba = ["Barrios", "Agronomía", "Almagro", "Balvanera", "Barracas", "Belgrano", "Boedo", "Caballito", "Chacarita", "Coghlan"]
# Escribir una funcion que muestre por pantalla los barrios que incien con las letras "ba"
# Para realizar este ej. podemos utilizar el metodo .startswith("Ba") de los objetos de tipo string: string.startswith("Ba")
# Documentacion --> https://www.w3schools.com/python/ref_string_startswith.asp

# def barrios():
#     barrios_caba = ["Barrios", "Agronomía", "Almagro", "Balvanera", "Barracas", "Belgrano", "Boedo", "Caballito", "Chacarita", "Coghlan"]
#     for x in barrios_caba:
#         if x.startswith("Ba"):
#             print(x)
# barrios()

# Ejercicio 7
# Escribir una funcion para hallar la superficie de un triangulo conociendo la base y la altura.
# El programa tiene que solcitar al usuario que ingrese la base y la altura.
# Superficie = base * altura / 2

# def funcion1():
#     base = int(input("Ingrese base "))
#     altura = int(input("Ingrese altura "))
#     b = (base)
#     h = (altura)
#     print((b*h)/2)
# funcion1()

# Ejercicio 8
# Escribir una funcion que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.
# def funcion2():
#     n1= int(input(" Dividendo "))
#     n2= int(input(" Divisor "))
#     print((n1/n2))
#     if n2 == 0:
#         print("ERROR")
# funcion2()
# Ejercicio 9
# Volvemos a utilizar la lista de barrios:
# barrios_caba = ["Barrios", "Agronomía", "Almagro", "Balvanera", "Barracas", "Belgrano", "Boedo", "Caballito", "Chacarita", "Coghlan"]
# Escribir un programa que muestre por pantalla todos los barrios dentro de la lista pero en mayuscula
# Para realizar este ej. podemos utilizar el metodo .upper() de los objetos de tipo string string.upper() 
# Documentacion --> https://www.w3schools.com/python/ref_string_upper.asp

# barrios_caba = ["Barrios", "Agronomía", "Almagro", "Balvanera", "Barracas", "Belgrano", "Boedo", "Caballito", "Chacarita", "Coghlan"]
# def barrios():
#     for barrio in barrios_caba:
#         if barrio.upper():
#             print(barrio.upper())
# barrios()


# Ejercicio 10
# Escribir una funcion que pida al usuario un número entero y muestre por pantalla si es par o impar.


# Ejercicio 11
# Dada la siguiente lista de frutas:m
# frutas = ["manzana", "banana", "pera", "anana"]
# Escribir un programa que le solicite al usuario una fruta y verifique si esta existe dentro de la lista de frutas.
# Para realizar este ejercicio podemos utilizar la palabra reservada in.
# Documentacion --> https://www.w3schools.com/python/ref_keyword_in.asp


# Ejercicio 12
# Para tributar un determinado impuesto se debe ser mayor de 18 años y tener unos ingresos iguales o superiores a $300.000 mensuales.
# Escribir una funcion que pregunte al usuario su edad, sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.


# Ejercicio 13
# Escribir una funcion que pida al usuario una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas)
def funcion1(): 
    frase = input("Ingrese una frase ")
    vocales = 'aeiouAEIOU'
    print(set([x for x in frase if x in vocales]))

funcion1()
# for each x in text , if x is true, add it to the list




# Ejercicio 14
# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto.
# Escribir una funcion que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

# def curso():
#     name = input("Ingrese su nombre ")
#     gender = input("Ingrese sexo M o H ")
#     if gender == "M":
#         if name.lower() < "m":
#             group = "A"
#         else:
#             group = "B"
#     else:
#         if name.lower() > "n":
#             group = "A"
#         else:
#             group = "B"
#     print("Tu grupo es " + group)
# curso()

# Ejercicio 15
# Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
# 			Renta					Tipo impositivo
#		Menos de 10000€					5%
#		Entre 10000€ y 20000€			15%
#		Entre 20000€ y 35000€			20%
#		Entre 35000€ y 60000€			30%
#		Más de 60000€					45%
# Escribir una funcion que pregunte al usuario su renta anual y muestre por pantalla el tipo impositivo que le corresponde.

# def renta_impositiva():
#     renta = float(input("Ingrese su renta anual:  "))
#     if renta < 10000:
#         tipo = 5
#     elif renta < 20000:
#         tipo = 15
#     elif renta < 35000:
#         tipo = 20
#     elif renta < 60000:
#         tipo = 30
#     else:
#         tipo = 45
#     print("Tienes que pagar ", renta * tipo / 100,"€")

# renta_impositiva()

# Ejercicio 16
# Escribir una funcion que pida al usuario un número entero positivo
# y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas.
# Para realizar este ej. podemos utilizar la funcion nativa de python range(start, stop, step).
# Documentacion --> https://www.w3schools.com/python/ref_func_range.asp 
# La funcion range utiliza 2 variables numericas start, stop como incio y fin.
# La tercer variable tambien numerica step especifica el incremento.


# Ejercicio 17
# En una determinada empresa, sus empleados son evaluados al final de cada año.
# Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios.
# Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas.
# A continuación se muestra una tabla con los niveles correspondientes a cada puntuación.
#			Nivel					Puntuación
#		Inaceptable						0.0
#		Aceptable						0.4
#		Meritorio						0.6 o más
# La cantidad de dinero conseguida en cada nivel es de $100.000 multiplicada por la puntuación del nivel.
# Escribir una funcion que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

# def empresa():
#     dinero = 100000
#     inaceptable = 0.0
#     aceptable = 0.4
#     meritorio = 0.6

#     puntos = float(input("Indique su puntuación: "))
#     if puntos == inaceptable:
#         print("Tu nivel es inaceptable ")
#     elif puntos == aceptable:
#         print("Tu nivel es aceptable ")
#     elif puntos >= meritorio:
#         print("Tu nivel Meritorio ")

#     print("Te corresponde", puntos * dinero)    
 

# # Ejercicio 18
# # Escribir una funcion que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

# def todos_los_anios():
#     edad = int(input("Ingrese su edad: "))
#     for x in range (1, edad+1,):
#         print(x, end = ", ")
# todos_los_anios()

# Ejercicio 19
# Escribir una funcion para una empresa que tiene salas de juegos para todas las edades 
# y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. 
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. 
# Si el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar $1200 y si es mayor de 18 años, $2000.


# Ejercicio 20
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.
# 		- Ingredientes vegetarianos: Morron y tofu.
#		- Ingredientes no vegetarianos: Longaniza, Jamón y Salmón.
# Escribir una funcion que pregunte al usuario si quiere una pizza vegetariana o no
# y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas.
# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.


# Ejercicio 21
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra introducida empezando por la última.
# Para realizar este ejercicio tenemos que entender los indices de un objeto iterable
# Documentacion --> https://www.digitalocean.com/community/tutorials/how-to-index-and-slice-strings-in-python-3
