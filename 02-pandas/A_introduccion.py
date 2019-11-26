# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import numpy as np
import pandas as pd

lista_numero = [1,2,3,4]
tupla_numeros = (1,2,3,4)
np_numeros = np.array((1,2,3,4))

serie_a = pd.Series(
        lista_numero)
serie_b = pd.Series(
        tupla_numeros)
serie_c = pd.Series(
        np_numeros)
serie_d = pd.Series([
        True, False,12,12.2, "Pamela",None,(),[],{"nombre":"Pamela"}])

serie_d[3]

lista_ciudades = ["Ambato","Cuenca","Loja","Quito"]

serie_ciudades = pd.Series(lista_ciudades, index=["A","C","L","Q"])

serie_ciudades["Q"]

serie_ciudades[3]

valores_ciudad = {
        "Ibarra":9500,
        "Guayaquil":10000,
        "Cuenca":7000,
        "Quito":8000,
        "Loja":3000
        }

seria_valor_ciudad = pd.Series(valores_ciudad)

seria_valor_ciudad["Cuenca"]
seria_valor_ciudad[2]


ciudades_menores_5000 = seria_valor_ciudad < 5000

s5=seria_valor_ciudad[ciudades_menores_5000]

s6= seria_valor_ciudad * 1.1

s6["Quito"]= s6 ["Quito"]-50

print("Lima" in s6)
print("Loja" in s6)

rsquare = np.square(s6)

rseno = np.sin(s6)

ciudades_uno = pd.Series({
        "Montanita":300,
        "Guayaquil":10000,
        "Quito":2000})

ciudades_dos = pd.Series({
        "Loja":300,
        "Guayaquil":10000})

ciudades_uno["Loja"]= 0
ciudades_dos["Montanita"]= 0
ciudades_dos["Quito"]= 0


print (ciudades_uno + ciudades_dos)

ciudad_add=ciudades_uno.add(ciudades_dos)

ciud_concatenadas = pd.concat([
        ciudades_uno, ciudades_dos])

ciud_concatenadas_v = pd.concat([
        ciudades_uno, ciudades_dos], verify_integrity = True)

ciud_append = ciudades_uno.append(ciudades_dos,  verify_integrity = True)

ciudades_uno.max()
pd.Series.max(ciudades_uno)
np.max(ciudades_uno)

ciudades_uno.min()
pd.Series.min(ciudades_uno)
np.min(ciudades_uno)

#Estadistica

ciudades_uno.mean()
ciudades_uno.median()
np.average(ciudades_uno)


ciudades_uno.head(2)
ciudades_uno.tail(2)

ciudades_uno.sort_values(ascending = False).head(2)
ciudades_uno.sort_values().head(2)
ciudades_uno.sort_values().tail(2)
