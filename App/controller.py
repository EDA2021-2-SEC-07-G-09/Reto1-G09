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

from typing import MutableMapping
import config as cf
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros
def inicatalog():
    catalog = model.museo()
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
    booksfile = cf.data_dir + 'Data/Artists-utf8-small.csv'
    input_file = csv.DictReader(open(booksfile, encoding='utf-8'))
    for artista in input_file:
        model.addArtista(museo, artista)


def cargarObras(museo):
    """
    Carga todos los tags del archivo y los agrega a la lista de tags
    """
    tagsfile = cf.data_dir + 'Data/Artworks-utf8-small.csv'
    input_file = csv.DictReader(open(tagsfile, encoding='utf-8'))
    for obra in input_file:
        model.addObra(museo, obra)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def darUltimosArtistas(museo):
    ultimos=model.darUltimossArtistas(museo)
    return ultimos
def darUltimasObras(museo):
    ultimos=model.darUltimossObras(museo)
    return ultimos

def numeroArtistas(museo):
    size= model.numeroArtistas(museo)
    return size
def numeroObras(museo):
    size= model.numeroObras(museo)
    return size



