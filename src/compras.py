from typing import *
from datetime import datetime
from collections import namedtuple
from parsers import *
import csv

Compra = namedtuple('Compra',['dni','supermercado','provincia','fecha_llegada','fecha_salida','total_compra'])

#EJERCICIO 1:
def lee_compras(fichero: str) -> List[Compra]:
    with open (fichero, encoding='utf-8') as f:
        lector = csv.reader(f,delimiter = ",")
        next(lector)

        res = []
        for dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra in lector:
            fecha_llegada = parsear_fecha(fecha_llegada)
            fecha_salida = parsear_fecha(fecha_salida)
            total_compra = float(total_compra)
            tupla = Compra(dni,supermercado,provincia,fecha_llegada,fecha_salida,total_compra)
            res.append(tupla)
    return res

#EJERCICIO 2:
def compra_maxima_minima_provincia(compras: List[Compra], provincia: str) -> Tuple[float,float]:
    compras_provincias = [c.total_compra for c in compras if c.provincia == provincia or provincia == None]
    return (max(compras_provincias),min(compras_provincias))

#EJERCICIO 3:
def hora_menos_afluencia(compras: List[Compra]):
    dicc = {}
    for compra in compras:
        hora_llegada = compra.fecha_llegada.hour
        if hora_llegada not in dicc:
            dicc[hora_llegada] = 1
        else:
            dicc[hora_llegada] += 1
    return min(dicc.items(),key=lambda x:x[1])

#EJERCICIO 4:
def supermercados_mas_facturacion(compras: List[Compra], n:int = 3):
    lista = []
    res = []
    i = 0
    supermercados = set(c.supermercado for c in compras)
    for supermercado in supermercados:
        ingresos_por_supermercado = sum([c.total_compra for c in compras if c.supermercado == supermercado])
        tupla = (supermercado,ingresos_por_supermercado)
        lista.append(tupla)
    lista_ordenada = sorted(lista,key=lambda x:x[1],reverse=True)
    for e in lista_ordenada:
        i+=1
        res.append((i,e))
    return res[:n]

#EJERCICIO 5:
def clientes_itinerantes(compras: List[Compra], n:int):
    lista = []
    lista_dni = list(set(c.dni for c in compras))
    for dni in lista_dni:
        provincias = sorted(set(c.provincia for c in compras if c.dni == dni))
        if len(provincias) > n:
            tupla = (dni,provincias)
            lista.append(tupla)
    return lista

#EJERCICIO 6:
def dias_estrella(compras: List[Compra], supermercado, provincia):
    fecha_estrella = []
    compras_ordenadas = sorted([c for c in compras if c.supermercado == supermercado and c.provincia == provincia], key=lambda x:x.fecha_salida)
    for i in range(1,len(compras_ordenadas)-1):
        compra_anterior = compras_ordenadas[i-1]
        compra_actual = compras_ordenadas[i]
        compra_siguiente = compras_ordenadas[i+1]
        if compra_actual.total_compra > compra_anterior.total_compra and compra_actual.total_compra > compra_siguiente.total_compra:
            fecha_estrella.append(compra_actual.fecha_salida.date())
    return fecha_estrella



            