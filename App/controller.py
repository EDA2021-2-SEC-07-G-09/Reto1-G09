"""
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
    booksfile = cf.data_dir + 'Artists-utf8-10pct.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for artista in input_file:
        model.addArtista(museo, artista)


def cargarObras(museo):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = cf.data_dir + 'Artworks-utf8-10pct.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for obra in input_file:
        model.addObra(museo, obra)
# Funciones de ordenamiento

def sortArrayListInsertion(lista):
    ordenada= model.sortArrayListInsertion(lista)
    return ordenada

def sortArrayListShell(lista):
    ordenada= model.sortArrayListShell(lista)
    return ordenada

def sortArrayListMerge(lista):
    ordenada= model.sortArrayListMerge(lista)
    return ordenada

def sortArrayListQuick(lista):
    ordenada= model.sortArrayListQuick(lista)
    return ordenada

def fechasRango(lista, fechai, fechaf):
    listaf= model.fechasRango(lista,fechai,fechaf)
    return listaf

def sortArrayListArtistInsertion(lista):
    ordenada= model.sortArrayListArtistInsertion(lista)
    return ordenada

def sortArrayListArtistShell(lista):
    ordenada= model.sortArrayListArtistShell(lista)
    return ordenada

def sortArrayListArtistMerge(lista):
    ordenada= model.sortArrayListArtistMerge(lista)
    return ordenada

def sortArrayListArtistQuick(lista):
    ordenada= model.sortArrayListArtistQuick(lista)
    return ordenada

def fechasRangoArtist(lista, fechai, fechaf):
    listaf= model.fechasRangoArtista(lista,fechai,fechaf)
    return listaf
# Funciones de consulta sobre el catálogo

def darUltimosArtistas(museo):
    ultimos=model.darUltimosArtistas(museo)
    return ultimos
def darUltimasObras(museo):
    ultimos=model.darUltimasObras(museo)
    return ultimos
def darPrimerosArtistas(museo):
    ultimos=model.darPrimerosArtistas(museo)
    return ultimos
def darPrimerasObras(museo):
    ultimos=model.darPrimerasObras(museo)
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