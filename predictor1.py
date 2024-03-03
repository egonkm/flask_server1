#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 10:54:34 2022

@author: egon
"""
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
import re, string, spacy

nlp=spacy.load('es_core_news_lg')

archivo_modelo = "model.final_num_cat_descr_img.h5"
archivo_embedding = "modelo_embedding.h5"

categoricas = [ 'antiVieja', 
   'emisionesMedia', 'localidad_ciudad vieja', 'localidad_corts',
   'localidad_ensanche', 'localidad_gracia', 'localidad_horta',
   'localidad_nou barris', 'localidad_plaza españa',
   'localidad_san martin', 'localidad_sant andreu', 'localidad_sants',
   'localidad_sarria', 'ascensor', 'blindada', 'cocinaequipada',
   'parking', 'trastero', 'terraza', 'aire',
   'armarios', 'lavadero', 'videoportero', 'cocinaoffice', 'patio',
   'suite', 'parquet']

preciom2 = [4075.3, 4884.8, 3661.1, 4901.2, 5740.5, 4284.6,
            3286.7, 2545.9, 3219.9, 4553.3, 4000.0]
max_y = 5.
pre_y = 100_000
# X_std = (X - X.min(axis=0)) / (X.max(axis=0) - X.min(axis=0))

X_min = np.array([ 1.,  1., 32.,  0.])
X_max = np.array([4.0, 2.0, 1.5000e+02, 5.7405e+03])
modelo = None
embedding = None

# 
def tabulares(datos):
    
    X = np.zeros( (1,31))
    
    loc = int(datos["localidad"])
    X[0, 6+loc] = 1
    
    numericas = [ datos["habitaciones"], datos["banos"], datos["metros"],
                 preciom2[loc]]
    
    for idx,num in enumerate(numericas):
        
        num = int(num)
        X[0, idx] = (num-X_min[idx])/(X_max[idx]-X_min[idx])
        
    for idx, categorica in enumerate(categoricas):
        
        if "localidad" in categorica: continue
    
        X[0, 4+idx] = 1 if categorica in datos else 0
        
    return X 
        
        
def descr(datos):
    
    d = datos["descr"]
    
    d = d.replace("Translate to English", "")
    d = d.lower().strip()
    
    doc = nlp(d)
    resultado = [ token.lemma_ for token in doc 
                    if (token not in nlp.Defaults.stop_words 
                        ) and not token.is_punct ]

    tokens = " ".join(resultado).strip()
    
    X = np.zeros( (1,300))
    X[0] = nlp(tokens).vector
    
    return X

from PIL import Image, ImageOps

def resize(img_file, size, keep_ratio=True, gray=True):
    
    img = Image.open(img_file)

    if gray:
        img = ImageOps.grayscale(img)
    else:
        if img.mode != "RGB":
                img = img.convert("RGB")

    if not keep_ratio: 
        img = img.resize( (size,size))
    else:
        ratio = size/(img.size[0 if img.size[0]<img.size[1] else 1])

        i2 = img.resize( ( int(img.size[0]*ratio),
                                       int(img.size[1]*ratio)))

        img = i2.crop( ( 0, i2.size[1]-size,
                        size, i2.size[1]))
         
    return img


def imagen(datos, embedding):
    
    size = (128,128,1)
    X = np.empty( (1, *size), dtype=np.float32 )
    X[0] = np.array(resize(datos["img"], size[0])).reshape(size)
    X = X / 255
    
    X_emb = np.empty( (1, 100))
    X_emb = embedding.predict(X)
    
    return X_emb
    
def predecir(datos):
    global modelo, embedding
    
    if modelo is None:
        modelo = load_model(archivo_modelo)
    
    if embedding is None:
        embedding = load_model(archivo_embedding)

    
    X = tabulares( datos)
    X_descr = descr(datos)
    X_img = imagen(datos, embedding)
    
    pred = modelo.predict( [X,  X_img, X_descr])[0][0]
    
    pred = pred*pre_y*max_y
    
    
    return pred