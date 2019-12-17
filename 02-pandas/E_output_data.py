# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 07:56:50 2019

@author: USRBET
"""

import pandas as pd
import os
import sqlite3

path_guardado_completo = "C://Users//USRBET//Documents//GitHub//py-pachacama-simba-a-pamela-abigail//02-pandas//data//artwork_data_completo.pickle"
df5 = pd.read_pickle(path_guardado_completo)

df =df5.iloc[49980:50019,:].copy()
#tIPOS DE ARCHIVO
#JSON
#EXCEL
#SQL

###EXCEL###

path_guardado= 'C://Users//USRBET//Documents//GitHub//py-pachacama-simba-a-pamela-abigail//02-pandas//data//mi_df_completo.xlsx'
df.to_excel(path_guardado)
df.to_excel(path_guardado, index=False)
columnas=['artist','title','year']
df.to_excel(path_guardado, columns = columnas)

## multiple hojas de trabajo

path_multiple= 'C://Users//USRBET//Documents//GitHub//py-pachacama-simba-a-pamela-abigail//02-pandas//data//mi_df_multiple.xlsx'
writer = pd.ExcelWriter(path_multiple, engine='xlsxwriter')
df.to_excel(writer, sheet_name='Primera')
df.to_excel(writer, sheet_name='Segunda', index=False)
df.to_excel(writer, sheet_name='tercera', columns=columnas)

writer.save()

### mnultiples hojas de trabajo

num_artist = df['artist'].value_counts()
path_colores= 'C://Users//USRBET//Documents//GitHub//py-pachacama-simba-a-pamela-abigail//02-pandas//data//mi_df_colores.xlsx'
writer = pd.ExcelWriter(path_colores, engine='xlsxwriter')
num_artist.to_excel(writer, sheet_name = 'Artistas')
hoja_artistas = writer.sheets['Artistas']
rango_celdas = 'B2:B{}'.format(len(num_artist.index)+1)
formato_artista = {"type":"2_color_scale", 
                   "min_value":"10",
                   "min_Type":"percentile",
                   "ma_value":"99",
                   "max_type":"percentile"
                   }
hoja_artistas.conditional_format(rango_celdas, formato_artista)
writer.save()


#####SQL######
with sqlite3.connect("bdd_artist.db") as conexion:
    df5.to_sql('py_artist', conexion)

###### mysql#####
##    df5.to_sql('tabla_mysql',conexion)

### JSON#####
df.to_json('artistas.json')
df.to_json('artistas_tabla.json',orient='table')







