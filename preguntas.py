"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""
import csv
with open('data.csv','r',encoding='UTF-8') as data:
ent=csv.reader(data,delimiter=' ')
lista=list(ent)
print(lista)

ldef=[]
for linea in lista:
    a=linea[0].split('\t')
ldef.append(a)


def pregunta_01():
    """
    Retorne la suma de la segunda columna.



    Rta/
    214

    """
    Sum=0
    for i in ldef:
        Sum=suma+int(i[1])
    return Sum



def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    lista2=[]
    for i in ldef: 
        lista2.append(i[0])
        listaaa=[]
        listaaa.append(("A",lista2.count("A")))
        listaaa.append(("B",lista2.count("B")))
        listaaa.append(("C",lista2.count("C")))
        listaaa.append(("D",lista2.count("D")))
        listaaa.append(("E",lista2.count("E")))
        
    return listaaa


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    dicc={}
    with open("data.csv") as file:
        for line in file:
           line= line.replace("\n","")
           line= line.replace("\t","")
           line= line.split(",")
           linea1= line[0]
            linea2= line[1]
            if linea 1 in dicc:
                dicc[linea1]= int(dicc[linea1])+int(linea2)
                
            else:
                dicc[linea1] = linea2
    dicc= sorted(dicc.items())
    return dicc



def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            line = line.split(",")
            suma = line[2]
            suma = suma.split("-")
            suma = suma[1]
            if suma in dicc:
                dicc[suma] = dicc[suma] + 1
            else: 
                dicc[suma] = 1
    dicc = sorted(dicc.items())
    return dicc


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            line = line.split(",")
            numero = line[1]
            linea1 = line[0]
            if linea1 in dicc:
                dicc[linea1].append(numero)
            else: dicc[linea1] = [numero]
    lista3=[]
    lista4=[]
    for key in dicc:  
        dicc[key] = [max(dicc[key]), min(dicc[key])]
    
    lista3 = sorted(dicc.items())
    for value in lista3:
        lista4.append((value[0], int(value[1][0]), int(value[1][1])))
    return lista4


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            for caracter in line.split(','):
                if caracter.count(':') > 0:
                    if caracter[:3] in dicc:
                        dicc[caracter[:3]].append(int(caracter[4:]))
                    else: 
                        dicc[caracter[:3]] = [int(caracter[4:])]

    for key, value in dicc.items():
        dicc[key] = [int(min(value)),int(max(value))]
    lista3 = sorted(dicc.items())
    
    lista4 = []
    for value in lst:
        lista4.append((value[0], int(value[1][0]), int(value[1][1])))
    return lista4


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
     dicc2 ={}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            line = line.split(",")
            numero = line[1]
            linea1 = line[0]

            if numero in dicc2:
                dicc2[numero].append(linea1)
            else: dicc2[numero] = [linea1] 

    lista3 = sorted(dicc2.items())

    lista4 = []
    for value in lista3:
        lista4.append((int(value[0]),value[1]))
    return lista4


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
     dicc2 ={}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            line = line.split(",")
            numero = line[1]
            linea1 = line[0]

            if numero in dicc2:
                if linea1 in dicc2[numero]:
                    continue
                else: dicc2[numero].append(linea1)
            else: dicc2[numero] = [linea1] 

    for key, value in dicc.items():
        dicc[key] = (sorted(value))
    lista3 = sorted(dicc2.items())

    lista4 = []
    for value in lista3:
        lista4.append((int(value[0]),value[1]))

    return lista4


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    dicc ={}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.replace("\t",",")
            for caracter in line.split(','):
                if caracter.count(':') > 0:
                    if caracter[:3] in dicc:
                        dicc[caracter[:3]] +=1
                    else: 
                        dicc[caracter[:3]] = 1


    registros = dict((k,v) for k,v in sorted(dicc.items()))

    return registros


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    lista3 =[]
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.split("\t")
            linea1 = line[0]
            col4= line[3].count(',')+1
            col5= line[4].count(',')+1
            lista3.append((linea1, col4, col5))
    return lista3


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    dicc = {}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.split("\t")
            col2 = int(line[1])
            col4 = line[3]
            for letra in col4.split(','):
                if letra in dicc.keys():
                    dicc[letra] += col2
                else: dicc[letra] = col2
    lista3 = sorted(dicc.items())
    dic_= {}

    for item in lista3:
        dic_[item[0]] = item[1]
    return dic_


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    dicc = {}
    with open("data.csv") as file:
        for line in file:
            line = line.replace("\n","")
            line = line.split("\t")
            col_1 = line[0]
            col_5 = line[4]
            col_5 = col_5.replace(":",",").split(",")
            i = 0
            number = 0
            for valor in col_5:
                if valor.isnumeric() == True: number = numero + int(valor)

            if col_1 in dicc:
                dicc[col_1] += number
            else: dicc[col_1] = number
    
    abc = {}
    lista3 = sorted(dicc.items())
    for valor in lista3: abc[valor[0]]=valor[1]
    return abc
