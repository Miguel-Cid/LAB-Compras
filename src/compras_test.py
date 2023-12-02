from compras import *

def test_lee_compras(compras):
    print("\nTEST de lee_compras")
    print(f"Números de registros leidos: {len(compras)}")
    print("Las 3 primeras son:")
    for i in compras[:3]:
        print(i)
    print("Las 3 últimas son:")
    for e in compras[len(compras)-3:]:
        print(e)

def test_compra_maxima_minima_provincia(compras):
    print("##########################################################################################")
    print("\nTEST de compra_maxima_minima_provincia")
    provincias = ["Huelva",None]
    for provincia in provincias:
        max = compra_maxima_minima_provincia(compras,provincia)[0]
        min = compra_maxima_minima_provincia(compras,provincia)[1]
        print(f"En {provincia} el importe máximo fue de {max} y el mínimo fue de {min}")

def test_hora_menos_afluencia(compras):
    print("##########################################################################################")
    print("\nTEST de hora_menos_afluencia")
    print(f"La hora con menos afluencia es: {hora_menos_afluencia(compras)[0]} h, con {hora_menos_afluencia(compras)[1]} llegadas de clientes")

def test_supermercados_mas_facturacion(compras):
    print("##########################################################################################")
    print("\nTEST de supermercados_mas_facturacion")
    n = 2
    print(f"Los {n} supermercados que más facturan son: {supermercados_mas_facturacion(compras,n)}")

def test_clientes_itinerantes(compras):
    print("##########################################################################################")
    print("\nTEST de clientes_itinerantes")
    n=6
    print(f"Los clientes itinerantes que han comprado al menos en {n} provincias son:")
    for dni,provincias in clientes_itinerantes(compras,n):
        print(f"Dni: {dni} ===> {provincias}")

def test_dias_estrellas(compras):
    print("##########################################################################################")
    print("\nTEST de dias_estrellas")
    fechas = []
    supermercado = "Aldi"
    provincia = "Huelva"
    for fecha in dias_estrella(compras,supermercado,provincia):
        fechas.append(f"{fecha.day}/{fecha.month}/{fecha.year}")
    print(f"Los días estrella del supermercado {supermercado} de la provincia de {provincia} son: {fechas}")

def main():

    compras = lee_compras("./data/compras.csv")
    test_lee_compras(compras)
    test_compra_maxima_minima_provincia(compras)
    test_hora_menos_afluencia(compras)
    print(supermercados_mas_facturacion(compras,n=3))
    test_supermercados_mas_facturacion(compras)
    test_clientes_itinerantes(compras)
    test_dias_estrellas(compras)

if __name__ == '__main__':
    main()