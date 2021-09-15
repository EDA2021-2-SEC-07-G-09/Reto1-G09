﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.If not, see <http://www.gnu.org/licenses/>.
 """

from io import DEFAULT_BUFFER_SIZE
from typing import MutableMapping
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def inicatalogArrayList():
    catalog = model.museoArrayList()
    return catalog

def inicatalogLinkedList():
    catalog = model.museoLinkedList()
    return catalog

def cargarDatos(museo):
    cargarArtistas(museo)
    cargarObras(museo)



# Funciones para la carga de datos
def cargarArtistas(museo):
    """
    Carga los libros del archivo.  Por cada libro se toman sus autores y por
    cada uno de ellos, se crea en la lista de autores, a dicho autor y una
    referencia al libro que se esta procesando.
    """
    booksfile = cf.data_dir + 'Artists-utf8-small.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for artista in input_file:
        model.addArtista(museo, artista)


def cargarObras(museo):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = cf.data_dir + 'Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for obra in input_file:
        model.addObra(museo, obra)
# Funciones de ordenamiento

def sortArrayListInsertion(lista, cmp):
    ordenada= model.sortArrayListInsertion(lista, cmp)
    return ordenada

def sortArrayListShell(lista, cmp):
    ordenada= model.sortArrayListShell(lista, cmp)
    return ordenada

def sortArrayListMerge(lista, cmp):
    ordenada= model.sortArrayListMerge(lista, cmp)
    return ordenada

def sortArrayListQuick(lista, cmp):
    ordenada= model.sortArrayListQuick(lista, cmp)
    return ordenada
def cmpArtworkByDateAcquired(artwork1, artwork2):
    """Devuelve True si la DateAquired de artwork1 es menor que la de artwork2
    artwork: Información de la primera obra que incluye su"""
    resultado= model.cmpArtworkByDateAcquired(artwork1, artwork2)
    return resultado
def fechasRango(lista, fechai, fechaf):
    listaf= model.fechasRango(lista,fechai,fechaf)
    return listaf

# Funciones de consulta sobre el catálogo

def darUltimosArtistas(museo):
    ultimos=model.darUltimosArtistas(museo)
    return ultimos
def darUltimasObras(museo):
    ultimos=model.darUltimasObras(museo)
    return ultimos
def darPrimerossArtistas(museo):
    ultimos=model.darUltimosArtistas(museo)
    return ultimos
def darPrimerasObras(museo):
    ultimos=model.darUltimasObras(museo)
    return ultimos
def numeroArtistas(museo):
    size= model.numeroArtistas(museo)
    return size
def numeroObras(museo):
    size= model.numeroObras(museo)
    return size
def obrasPurchase(lista):
    obras= model.obrasPurchase(lista)
    return obras
def cortarLista(lista, muestra):
    lista_nueva= model.cortarLista(lista,muestra)
    return lista_nueva