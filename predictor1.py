#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 10:54:34 2022

@author: egon
"""


['SEXO', 'grupo', 'EDAD', 'Influenciapaterna', 'organización',
       'Expectativasallogro', 'Miedoaloerrores', 'destre.Aperder',
       'destre.Aganar', 'dstre.durantejuego', 'destre.Juegojusto',
       'habilidadessociales', 'satisvida', 'catdep_2', 'catdep_3']
    

import joblib

file_name = 'modelo_datos1.pkl'

modelo1 = joblib.load(file_name)

st = joblib.load("st_scaler.pkl")

def sumar(datos, de, hasta, lista=None):
    
    if lista:
        rango = lista 
    else:
        rango = range(de, hasta+1)
        
    return sum([int(datos["q"+str(idx)]) for idx in rango])

miedo = [37 + item for item in [9,10,14,17,21,23,25,28,32,33,34]]
influencias = [37+item for item in [1,3,5,11,15,20,22,26,35]]
expectativas = [37+item for item in [4,6,12,13,16,18,19,24,30]]
organizacion = [37+item for item in [2,7,8,27,29,31]]
    
def guardar(datos, file_name):
    
    
    if isinstance(datos, dict):
        datos = [v for k,v in datos.items()]
        
    linea = ",".join( [str(item) for item in datos])
        
    with open(file_name, "a") as f:
        f.write(linea)
        f.write("\n")
        
def predecir(datos):
    
    numerical = [ datos["age"],        
     sumar(datos, 0, 0, influencias), # 'Influenciapaterna', 
     sumar(datos, 0, 0, organizacion), # 'organización',
     sumar(datos, 0, 0, expectativas), #      'Expectativasallogro', 
     sumar(datos, 0, 0, miedo), #       'Miedoaloerrores', 
          sumar(datos, 1,5), #  'destre.Aperder',
           sumar(datos,6,10), #  'destre.Aganar',
            sumar(datos, 11, 15), # 'dstre.durantejuego', 
            sumar(datos, 16, 20), # 'destre.Juegojusto',
           sumar(datos, 21, 32), #'habilidadessociales', 
           sumar(datos, 33, 37)] # 'satisvida',     ]
    
    num_st = st.transform([numerical])
    
    X = [[
          datos["gender"], 
          datos["Category"]] + 
        
          list(num_st[0]) + 
          
          [
          1 if datos["sportCategory"] in ["4", "5"] else 0, # catdep_2
          1 if datos["sportCategory"] == "6" else 0  # catdep_3
        ]]
    
    pred = modelo1.predict(X)[0]
    
    guardar(datos, "datos_form.csv")
    guardar(X[0], "datos.csv")
    
    return pred