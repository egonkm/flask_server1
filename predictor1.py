#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 10:54:34 2022

@author: egon
"""


archivo_modelo = "model.final_num_cat_descr_img.h5"

['SEXO', 'grupo', 'EDAD', 'Influenciapaterna', 'organización',
       'Expectativasallogro', 'Miedoaloerrores', 'destre.Aperder',
       'destre.Aganar', 'dstre.durantejuego', 'destre.Juegojusto',
       'habilidadessociales', 'satisvida', 'cat_2', 'cat_3', 'cat_4', 'cat_5',
       'cat_6', 'catdep_2', 'catdep_3']
    

import joblib

file_name = 'modelo_datos1.pkl'

modelo1 = joblib.load(file_name)

def predecir(datos):
    
    
    X = [[1] * 20
        ]
    
    pred = modelo1.predict(X)[0]
    
    
    return pred