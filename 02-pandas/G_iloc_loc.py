# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:04:33 2019

@author: USRBET
"""

import pandas as pd

path_guardado_completo = "C://Users//USRBET//Documents//GitHub//py-pachacama-simba-a-pamela-abigail//02-pandas//data//artwork_data_completo.pickle"
df = pd.read_pickle(path_guardado_completo)



df2 = df.set_index('id')
segundo = df2.loc[0]
primero = df2.iloc[0]
"""
NOMBRE  nota 1  disciplina
Pepito    7        5
Juanita   8        9
Maria     9        2

"""

nombre = ['Pepito','Juanito','Maria']
nota1 = [7,8,9]
disciplina=[5,9,2]


datos = {
        "nota1":{
                "Pepito":7,
                "Juanita":8,
                "Maria":9},
        "disciplina":{
                "Pepito":5,
                "Juanita":9,
                "Maria":2}
        }
notas = pd.DataFrame(datos)

notas.loc["Pepito"]
notas.iloc[0]

notas.loc["Pepito","disciplina"]

notas.loc["Pepito",["disciplina","nota1"]]
notas.loc[["Pepito","Juanita"]]
notas.loc[["Pepito","Juanita"],["nota1"]]
notas.loc[[True,False, True]]

condicion_nota = notas["nota1"]>7
mayores_siete=notas.loc[condicion_nota]
condicion_disciplina=notas["disciplina"]>7
condicion_disciplina2=notas["disciplina"]<7
mayor_siete=notas.loc[condicion_nota][condicion_disciplina]

mayores_siete=notas.loc[condicion_nota, ['nota1']]
notas.loc["Maria","disciplina"]= 7

notas.loc[condicion_disciplina2, "disciplina"]=7
notas.loc["Pepito",:]= 10
notas.loc[:,"disciplina"]= 7
notas["promedio"]=(notas["nota1"]+notas["disciplina"])/2





