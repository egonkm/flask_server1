#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:50:15 2024

@author: egon


Script para generar código HTML para las preguntas del cuestionario
para facilitar la construcción de la página web del formulário

"""

def generate_html(questions, start=1, label=[]):
    
    html_sections = ""
    
    for i, question in enumerate(questions, start=start):
        
        html_sections += f'''
        <!-- Question {i} -->
        <label for="q{i}">{i}. {question}</label><br>
        '''
        for j in range(5, 0, -1):
            html_sections += f'''
            <input type="radio" id="q{i}-{j}" name="q{i}" value="{j}"><label for="q{i}-{j}">{label[j-1]}</label>
            '''
        html_sections += "<br>\n"

    return html_sections

survey_questions = [
    "¿Felicitas al ganador al perder un partido o un juego?",
    "¿Te mantienes calmado y positivo?",
    "¿Ignoras la burla de otros compañeros?",
    "¿Evitas culpar a tus compañeros de equipo por una mala ejecución personal?",
    "¿Respetas tus propios materiales (ej. Raqueta de tenis) y los materiales de otros compañeros?",
    "¿Evitas criticar al que perdió o a los que perdieron?",
    "¿Aceptas complementos de otros al ganar?",
    "¿Aportas sugerencias a otros de manera respetuosa?",
    "¿Demuestras apreciación a oponentes y compañeros de equipo?",
    "¿Te recompensa a ti mismo y te mantienes motivado sin reírte de los demás?",
    "¿Sigues las reglas de juego en todo momento?",
    "¿Haces comentarios positivos de la actuación de otros durante el juego?",
    "¿Ayudas a otros durante el juego de ser necesario? (ej. Ayuda a otros a levantarse del suelo luego de una caída)",
    "¿Respetas el nivel de habilidad de los demás sin menospreciarles o burlarte de ellos?",
    "¿Eres un buen miembro del equipo trabajando colaborativamente (no querer jugar solo)?",
    "¿Participas con entusiasmo e intensidad?",
    "¿Realizas tu mejor esfuerzo para mejorar en tus destrezas y nivel de actividad física?",
    "¿Controlas tu conducta en todo momento?",
    "¿Tratas de resolver conflictos de manera adecuada?",
    "¿Respetas la decisión de algún compañero o maestro que asuma la posición de árbitro (oficial)?",
    "¿Interactúas de manera adecuada con tus compañeros/as de clase?",
    "¿Escuchas cuando alguien te habla?",
    "¿Mantienes un contacto visual cuando alguien te habla?",
    "¿Sigues las órdenes del profesor?",
    "¿Usas un tono de voz apropiado?",
    "¿Aprendes a manejar situaciones de burla, enojo y malentendido?",
    "¿Compartes el equipamiento durante las clases?",
    "¿Usas un lenguaje apropiado y correcto en las clases?",
    "¿Ayudas a otros cuando lo necesitan?",
    "¿Sonríes adecuadamente?",
    "¿Respetas los turnos de intervención de tus compañeros?",
    "¿Tienes gestos apropiados con tus compañeros?"
]

labels1 = [
    "Nunca", "Casi nunca", "A menudo",
    "Casi Siempre", "Siempre"
    
    ]
           
           
           
perfectionism_questions = [
    "Mis padres me fijaron metas muy altas",
    "La organización es muy importante para mí",
    "Cuando era niño/a fui castigado por no hacer las cosas a la perfección",
    "Si no me fijo metas muy elevadas probablemente acabaré siendo una persona de segunda categoría",
    "Mis padres nunca intentaron entender mis errores",
    "Es importante para mí ser absolutamente competente en todo lo que hago",
    "Soy una persona ordenada",
    "Intento ser una persona organizada",
    "Si fallo en el trabajo en la escuela o en casa soy un fracaso como persona",
    "Debo preocuparme si cometo un error",
    "Mis padres querían que yo fuera el/la mejor en todo",
    "Me fijo metas más elevadas que la mayoría de la gente",
    "Si alguien hace mejor que yo las cosas en el trabajo en la escuela o en casa me siento como si hubiera fracasado completamente",
    "Si fallo en parte es tan malo como fracasar completamente",
    "Para mi familia solo son buenos los resultados excelentes",
    "Soy muy bueno/a concentrando mis esfuerzos para alcanzar una meta",
    "Incluso cuando hago algo muy cuidadosamente a menudo siento que no lo he hecho del todo bien",
    "Odio no ser el/la mejor en todo lo que hago",
    "Me propongo metas excesivamente altas",
    "Mis padres han esperado grandes cosas de mí",
    "La gente probablemente tendrá peor opinión de mí si cometo un error",
    "Pienso que nunca llegaré a satisfacer las expectativas de mis padres",
    "Si no hago las cosas tan bien como el resto de personas quiere decir que soy inferior a ellas",
    "Otras personas parecen conformarse con menos que yo",
    "Si no lo hago bien siempre la gente no me respetará",
    "Mis padres siempre han tenido más expectativas sobre mi futuro que yo",
    "Trato de ser una persona ordenada",
    "En general tengo dudas acerca de lo que hago",
    "La limpieza tiene mucha importancia para mí",
    "Espero hacer las cosas de cada día mejor que la mayoría de la gente",
    "Soy una persona organizada",
    "Tiendo a atrasarme en mi trabajo porque repito las cosas una y otra vez",
    "Me lleva mucho tiempo hacer las cosas correctamente",
    "Cuantos menos errores cometa más personas me querrán",
    "Siento que nunca cumpliré las expectativas de mis padres"
]

labels2 = ["En total desacuerdo", "En desacuerdo", 
           "Neutro", "En acuerdo", "Completamente de acuerdo"
           ]

if __name__=="__main__":
    
    for lista, labels in  zip([ survey_questions, perfectionism_questions], 
                              [labels1, labels2]):
        
        print(generate_html(lista, 1, labels))
        print("\n--------------------------------")