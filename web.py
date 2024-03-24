#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 08:52:18 2022

@author: egon
"""

from flask import Flask
from predictor1 import predecir
from resultados1 import resultados

app = Flask(__name__)


from flask import request, render_template,session,redirect,url_for

@app.route("/")
def route_main():
    
    return render_template("cuestionario1.html")

@app.route("/predecir1", methods=['POST']) 
def route_predecir1():

    data = request.form
     
    response = data.copy()
    
    try:
        p = predecir(response)
        
    except Exception as e:
        
        return "Erro: "+str(e)

    return render_template("resultado.html",
                              resultado=resultados[p]
                               )

if __name__=="__main__":
    
    app.run(debug=True, port=8080)
