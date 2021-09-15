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
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
import datetime as dt
import time
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def museoArrayList():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    

    museo= {'artistas': None,
            'obras': None}

    

    museo['artistas'] = lt.newList('ARRAY_LIST')
    museo['obras'] = lt.newList('ARRAY_LIST')                     
    return (museo)

def museoLinkedList():
    """
    Inicializa el catálogo de libros. Crea una lista vacia para guardar
    todos los libros, adicionalmente, crea una lista vacia para los autores,
    una lista vacia para los generos y una lista vacia para la asociación
    generos y libros. Retorna el catalogo inicializado.
    """
    

    museo= {'artistas': None,
            'obras': None}

    

    museo['artistas'] = lt.newList('LINKED_LIST')
    museo['obras'] = lt.newList('LINKED_LIST')                          
    return (museo)


# Funciones para agregar informacion al catalogo
def crearArtista(nombre, nacionalidad, genero, ano_nacimiento):
    artista = {'nombre': "",
               'nacionalidad': "",
               'genero': "",
               'ano_nacimiento': 0}
    artista['nombre']=nombre
    artista['nacionalidad'] = lt.newList('ARRAY_LIST')
    artista['nacionalidad']=nacionalidad
    artista['genero']=genero 
    artista['ano_nacimiento']=ano_nacimiento

    
    return artista

def crearObra(titulo, artistas, fecha_creacion, medio, fecha_adquisicion, dimensiones):

    obra= {'titulo': " ",
            'artistas': " ",
            'fecha_creacion': " ",
            'medio': " ",
            'fecha_adquisicion': " ",
            'dimensiones': " "}
    obra['titulo']=titulo
    obra['artistas'] = lt.newList('ARRAY_LIST')
    obra['artistas']=artistas
    obra['fecha_creacion']= fecha_creacion
    obra['medio']=medio
    obra['fecha_adquisicion']= fecha_adquisicion
    obra['dimensiones']= dimensiones
    return obra

def addArtista(museo, artista):
    # Se adiciona el libro a la lista de libros
    lt.addLast(museo['artistas'], artista)
    


def addObra(museo, obra):
    
    lt.addLast(museo['obras'], obra)
# Funciones para creacion de datos

# Funciones de consulta
def darUltimosArtistas(museo):
    b= lt.size(museo)
    listaUltimos= lt.subList(museo, (b-3),3)
    return listaUltimos

def darUltimasObras(museo):
    b= lt.size(museo)
    listaUltimos= lt.subList(museo, (b-3),3)
    return listaUltimos

def darPrimerosArtistas(museo):
    listaUltimos= lt.subList(museo, 0,3)
    return listaUltimos

def darPrimerasObras(museo):

    listaUltimos= lt.subList(museo, 0,3)
    return listaUltimos


def numeroArtistas(museo):
    size= lt.size(museo['artistas'])
    return size

def numeroObras(museo):
    size= lt.size(museo['obras'])
    return size
def obrasPurchase(obras):
    numero=0
    for obra in obras['elements']:
        if obra['CreditLine']== 'Purchase':
             numero +=1
    return numero
def cortarLista(lista, muestra):
    lista_cortada= lt.subList(lista, 0, muestra)
    return lista_cortada
    


# Funciones utilizadas para comparar elementos dentro de una lista
def cmpArtworkByDateAcquired(artwork1, artwork2):
    """Devuelve True si la DateAquired de artwork1 es menor que la de artwork2
    artwork: Información de la primera obra que incluye su"""
    a= artwork1['DateAcquired']
    b= artwork2['DateAcquired']
    try:
        if a !='' and b!='':
            x= dt.datetime.strptime(a, '%Y-%m-%d')
            y= dt.datetime.strptime(b, '%Y-%m-%d')
            if x<y:
                return True
        else: 
            return False
    except ValueError:
        return False
def cmpArtistByDateBirth(artista1, artista2):
    """Devuelve True si la DateAquired de artwork1 es menor que la de artwork2
    artwork: Información de la primera obra que incluye su"""
    a= artista1['BeginDate']
    b= artista2['BeginDate']
    x= int(a)
    y= int(b)
    if x<y:
        return True
    else: 
        return False

# Funciones de ordenamiento obras
def sortArrayListInsertion(lista):
    size = lt.size(lista) 
    pos1=1
    start_time = time.process_time()
    while pos1<= size:
        pos2=pos1
        while (pos2 >1) and cmpArtworkByDateAcquired(lt.getElement(lista, pos2),lt.getElement(lista, pos2-1)):
            lt.exchange (lista, pos2, pos2-1)
            pos2 -= 1
        pos1+=1
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000

    return lista, elapsed_time_mseg

def sortArrayListShell(lista):
    start_time = time.process_time()
    sa.sort(lista,cmpArtworkByDateAcquired)
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista, elapsed_time_mseg
 

def sortArrayListMerge(lista):
    start_time = time.process_time()
    size = lt.size(lista)
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lt.subList(lista, 1, mid)
        rightlist = lt.subList(lista, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        sortArrayListMerge(leftlist)
        sortArrayListMerge(rightlist)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = lt.size(leftlist)
        rightelements = lt.size(rightlist)

        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist, i)
            elemj = lt.getElement(rightlist, j)
            """compara y ordena los elementos"""
            if cmpArtworkByDateAcquired(elemj, elemi):  
                lt.changeInfo(lista, k, elemj)
                j += 1
            else:                           
                lt.changeInfo(lista, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lt.changeInfo(lista, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(lista, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
    stop_time = time.process_time()
    elapsed_time_mseg = (stop_time - start_time)*1000
    return lista, elapsed_time_mseg

def partition(lista, lo, hi):
    """
    Función que va dejando el pivot en su lugar, mientras mueve
    elementos menores a la izquierda del pivot y elementos mayores a
    la derecha del pivot
    """
    follower = leader = lo
    while leader < hi:
        if cmpArtworkByDateAcquired(
           lt.getElement(lista, leader), lt.getElement(lista, hi)):
            lt.exchange(lista, follower, leader)
            follower += 1
        leader += 1
    lt.exchange(lista, follower, hi)
    return follower


def quicksort(lista, lo, hi):
    """
    Se localiza el pivot, utilizando la funcion de particion.
    Luego se hace la recursión con los elementos a la izquierda del pivot
    y los elementos a la derecha del pivot
    """
    if (lo >= hi):
        return
    pivot = partition(lista, lo, hi)
    quicksort(lista, lo, pivot-1)
    quicksort(lista, pivot+1, hi)


def sortArrayListQuick(lista):
    quicksort(lista, 1, lt.size(lista))
    return lista

def fechasRango(lista, fechai, fechaf):
    
    listaf=lt.newList('ARRAY_LIST')
    a= dt.datetime.strptime(fechai, '%Y-%m-%d')
    b= dt.datetime.strptime(fechaf, '%Y-%m-%d')
    i=0
    while i in range(0, lt.size(lista)):

        try:
            obra = lt.getElement(lista,i)
            c= dt.datetime.strptime(obra['DateAcquired'], '%Y-%m-%d')
            if c<b and c>a:
                lt.addLast(listaf, obra)
        except ValueError:
             pass
    return listaf



 # Funciones de ordenamiento artistas   
 
def sortArrayListArtistInsertion(lista):
    size = lt.size(lista) 
    pos1=1
    while pos1<= size:
        pos2=pos1
        while (pos2 >1) and cmpArtistByDateBirth(lt.getElement(lista, pos2),lt.getElement(lista, pos2-1)):
            lt.exchange (lista, pos2, pos2-1)
            pos2 -= 1
        pos1+=1
    return lista

def sortArrayListArtistShell(lista):
    sa.sort(lista,cmpArtistByDateBirth)
    return lista
 

def sortArrayListArtistMerge(lista):
    size = lt.size(lista)
    if size > 1:
        mid = (size // 2)
        """se divide la lista original, en dos partes, izquierda y derecha,
        desde el punto mid."""
        leftlist = lt.subList(lista, 1, mid)
        rightlist = lt.subList(lista, mid+1, size - mid)

        """se hace el llamado recursivo con la lista izquierda y derecha"""
        sortArrayListArtistMerge(leftlist)
        sortArrayListArtistMerge(rightlist)

        """i recorre la lista izquierda, j la derecha y k la lista original"""
        i = j = k = 1

        leftelements = lt.size(leftlist)
        rightelements = lt.size(rightlist)

        while (i <= leftelements) and (j <= rightelements):
            elemi = lt.getElement(leftlist, i)
            elemj = lt.getElement(rightlist, j)
            """compara y ordena los elementos"""
            if cmpArtistByDateBirth(elemj, elemi):  
                lt.changeInfo(lista, k, elemj)
                j += 1
            else:                           
                lt.changeInfo(lista, k, elemi)
                i += 1
            k += 1

        """Agrega los elementos que no se comprararon y estan ordenados"""
        while i <= leftelements:
            lt.changeInfo(lista, k, lt.getElement(leftlist, i))
            i += 1
            k += 1

        while j <= rightelements:
            lt.changeInfo(lista, k, lt.getElement(rightlist, j))
            j += 1
            k += 1
    return lista

def partitionArtist(lista, lo, hi):
    """
    Función que va dejando el pivot en su lugar, mientras mueve
    elementos menores a la izquierda del pivot y elementos mayores a
    la derecha del pivot
    """
    follower = leader = lo
    while leader < hi:
        if cmpArtistByDateBirth(
           lt.getElement(lista, leader), lt.getElement(lista, hi)):
            lt.exchange(lista, follower, leader)
            follower += 1
        leader += 1
    lt.exchange(lista, follower, hi)
    return follower


def quicksortArtist(lista, lo, hi):
    """
    Se localiza el pivot, utilizando la funcion de particion.
    Luego se hace la recursión con los elementos a la izquierda del pivot
    y los elementos a la derecha del pivot
    """
    if (lo >= hi):
        return
    pivot = partitionArtist(lista, lo, hi)
    quicksortArtist(lista, lo, pivot-1)
    quicksortArtist(lista, pivot+1, hi)


def sortArrayListArtistQuick(lista):
    quicksortArtist(lista, 1, lt.size(lista))
    return lista

def fechasRangoArtista(lista, fechai, fechaf):
    
    listaf=lt.newList('ARRAY_LIST')
    a= int(fechai)
    b= int(fechaf)
    for artist in lista['elements']:
        x=artist['BeginDate']
        c= int(x)
        if c<b and c>a:
            lt.addLast(listaf, artist)
    return listaf



# Funciones para agregar informacion al catalogo




