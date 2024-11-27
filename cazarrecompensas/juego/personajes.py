import random

personajes = {
        "Susan": {"pelo": "rubio", "Entradas": False, "ojos": "marron", "gafas": False, "sombrero": False, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Mujer"},
        "Claire": {"pelo": "pelirrojo", "Entradas": False, "ojos": "marron", "gafas": True, "sombrero": True, "barba": False, "bigote": False, "pendientes": True, "Sexo": "Mujer"},
        "David": {"pelo": "rubio", "Entradas": False, "ojos": "marron", "gafas": False, "sombrero": False, "barba": True, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Anne": {"pelo": "castaño", "Entradas": False, "ojos": "marron", "gafas": False, "sombrero": False, "barba": False, "bigote": False, "pendientes": True, "Sexo": "Mujer"},
        "Robert": {"pelo": "castaño", "Entradas": False, "ojos": "azul", "gafas": False, "sombrero": False, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Anita": {"pelo": "rubio", "Entradas": False, "ojos": "azul", "gafas": False, "sombrero": False, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Joe": {"pelo": "rubio", "Entradas": False, "ojos": "marrión", "gafas": True, "sombrero": False, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "George": {"pelo": "rubio", "Entradas": False, "ojos": "marron", "gafas": False, "sombrero": True, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Bill": {"pelo": "rubio", "Entradas": True, "ojos": "marron", "gafas": False, "sombrero": False, "barba": True, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Alfred": {"pelo": "rubio", "Entradas": False, "ojos": "azul", "gafas": False, "sombrero": False, "barba": False, "bigote": True, "pendientes": False, "Sexo": "Hombre"},
        "Max": {"pelo": "castaño", "Entradas": False, "ojos": "marron", "gafas": False, "sombrero": False, "barba": False, "bigote": True, "pendientes": False, "Sexo": "Hombre"},
        "Tom": {"pelo": "castaño", "Entradas": True, "ojos": "azul", "gafas": True, "sombrero": False, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Alex": {"pelo": "castaño", "Entradas": False, "ojos": "marron", "gafas": False, "sombrero": False, "barba": False, "bigote": True, "pendientes": False, "Sexo": "Hombre"},
        "Sam": {"pelo": "rubio", "Entradas": True, "ojos": "marron", "gafas": True, "sombrero": False, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Richard": {"pelo": "castaño", "Entradas": True, "ojos": "marron", "gafas": False, "sombrero": False, "barba": True, "bigote": True, "pendientes": False, "Sexo": "Hombre"},
        "Paul": {"pelo": "rubio", "Entradas": False, "ojos": "marron", "gafas": True, "sombrero": False, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Maria": {"pelo": "castaño", "Entradas": False, "ojos": "marron", "gafas": False, "sombrero": True, "barba": False, "bigote": False, "pendientes": True, "Sexo": "Mujer"},
        "Frans": {"pelo": "pelirrojo", "Entradas": False, "ojos": "marron", "gafas": False, "sombrero": False, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Herman": {"pelo": "pelirrojo", "Entradas": True, "ojos": "marron", "gafas": False, "sombrero": False, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Bernard": {"pelo": "castaño", "Entradas": False, "ojos": "marron", "gafas": False, "sombrero": True, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Philip": {"pelo": "castaño", "Entradas": False, "ojos": "marron", "gafas": False, "sombrero": False, "barba": True, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Eric": {"pelo": "rubio", "Entradas": False, "ojos": "marron", "gafas": False, "sombrero": True, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
        "Charles": {"pelo": "rubio", "Entradas": False, "ojos": "azul", "gafas": False, "sombrero": False, "barba": False, "bigote": True, "pendientes": False, "Sexo": "Hombre"},
        "Peter": {"pelo": "rubio", "Entradas": False, "ojos": "azul", "gafas": False, "sombrero": False, "barba": False, "bigote": False, "pendientes": False, "Sexo": "Hombre"},
    }

def personajes_aleatorios():
    
    return random.choice(list(personajes.keys()))

