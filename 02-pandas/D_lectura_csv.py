# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 08:19:52 2019

@author: USRBET
"""

import pandas as pd
import os

#1- JSON CSV HTML XML ....
#2- Binary files -> (!#mf-.1234'120)
#3- Relational Database

path = "C://Users//USRBET//Documents//GitHub//py-pachacama-simba-a-pamela-abigail//02-pandas//data//artwork_data.csv"

df = pd.read_csv(path, nrows = 10)

columnas=['id','artist','title','medium','year','acquisitionYear','height','width','units']

df2 = pd.read_csv(path, nrows = 10, usecols = columnas)

df3 = pd.read_csv(path, nrows = 10, usecols = columnas, index_col ='id')

path_guardado = "C://Users//USRBET//Documents//GitHub//py-pachacama-simba-a-pamela-abigail//02-pandas//data//artwork_data.pickle"

df3.to_pickle(path_guardado)

df4 = pd.read_csv(path)

path_guardado_completo = "C://Users//USRBET//Documents//GitHub//py-pachacama-simba-a-pamela-abigail//02-pandas//data//artwork_data_completo.pickle"

df4.to_pickle(path_guardado_completo)

df5 = pd.read_pickle(path_guardado)





