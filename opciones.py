import csv
import statistics
from collections import Counter
from pprint import pprint
# def op1():
#     barrio=[]
#     with open("casos_covid19.csv") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=";")
#         for row in csv_reader:
#             if row[4] == 'CABA':
#                 barrio.append(str(row[5]))
#         falopa = (max(Counter(barrio),key=Counter(barrio).get))
#     print(falopa,Counter(barrio)[falopa])
# op1()

#Ej0

# def op1():
#     barrios={}
#     with open("casos_covid19.csv") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=";")
#         for row in csv_reader:
#             if row[4] == 'CABA':
#                 if row[5] in barrios:
#                     barrios[row[5]] +=1
#                 else:
#                     barrios[row[5]] = 1
#         barrios.pop('NA')
# #printear barrio con mayor cantidad de casos        
#         print (max(barrios,key=barrios.get))

#     return max(barrios,key=barrios.get)


#EJ1

# op1()

# def op1():
#     barrios={}
#     with open("casos_covid19.csv") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=";")
#         for row in csv_reader:
#             if row[4] == 'CABA':
#                 if row[5] in barrios:
#                     barrios[row[5]] +=1
#                 else:
#                     barrios[row[5]] = 1
#         barrios.pop('NA')
#         pprint(barrios)
# #printear barrio con mayor cantidad de casos        
# #        print (max(barrios,key=barrios.get))

#     return max(barrios,key=barrios.get)

# op1()

#Ej2

# def op1(nombre_barrio):
    
#     barrio={nombre_barrio:0}
#     with open("casos_covid19.csv") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=";")
#         for row in csv_reader:
#             if row[4] == 'CABA' and row[5] == nombre_barrio:
#                 barrio[row[5]] +=1
#     return barrio


#ej3

# def op1():
#     caba = 0 
#     gba = 0
#     with open("casos_covid19.csv") as csv_file:
#         csv_reader = csv.reader(csv_file, delimiter=";")
#         for row in csv_reader:
#             if row[4] == 'CABA':
#                     caba +=1
#             elif row[4] == 'Buenos Aires':
#                 gba +=1

#         print(caba,gba)