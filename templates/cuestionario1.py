#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 08:52:18 2022

@author: egon
"""

from flask import Flask
import tempfile
from predictor import predecir

app = Flask(__name__)


from flask import request, render_template,session,redirect,url_for

@app.route("/")
def route_main():
    
    return render_template("index.html")

@app.route("/predecir", methods=['POST']) 
def route_predecir():

    data = request.form
 
    img = request.files["imagen"]
    
    _, temp_file_path = tempfile.mkstemp()
    
    img.save(temp_file_path)
    
    response = data.copy()
    
    response["img"] = temp_file_path
    
    try:
        p = predecir(response)
        
    except Exception as e:
        
        return "Erro: "+str(e)
    
    p = str(int(p))
    
    response["predict"] = p
    

    return f"Valor predicto: {p}€"

if __name__=="__main__":
    
    app.run(debug=True, port=8080)