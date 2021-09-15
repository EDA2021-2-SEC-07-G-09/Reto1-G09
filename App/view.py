﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
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
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
import time
from DISClib.ADT import list as lt
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Cargar información en el catálogo")
    print("2- Consultar la lista de artistas ordenada cronológicamente")
    print("3- Consultar la lista de las adquisiciones ordenada cronológicamente")
    print("4- Consultar las obras de un artista ordenadas por técnica")
    print("5- Consultar la lista de obras clasificadas por la nacionalidad de su creador")
    print("6- Consultar el costo de transportar las obras de un departamento")
    print("7- Consultar la nueva exposición propuesta según el area disponible")
    print("0- Salir")



def museoLinkedList():
    return controller.inicatalogLinkedList()
def museoArrayList():
    return controller.inicatalogArrayList()
def cargarDatos(museo):
    return controller.cargarDatos(museo)
def imprimirDatosObra(obras):
    for obra in obras['elements']:
        x={'Title':obra['Title'],
        'Date':obra['Date'],
        'Medium': obra['Medium'],
        'Dimensions': obra['Dimensions']}
        print(x)
def imprimirDatosArtista(artistas):
    for artista in artistas['elements']:
        x={'Nombre': artista['DisplayName'],
        'Año de nacimiento': artista['BeginDate'],
        'Año de fallecimiento': artista['EndDate'],
        'Nacionalidad': artista['Nationality'],
        'Genero': artista['Gender']}
        print(x)



"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        x= input('Diga que tipo de lista necesita entre ARRAY_LIST y LINKED_LIST')
        print("Cargando información de los archivos ....")
        if x== 'LINKED_LIST':
            museo= museoLinkedList()
            cargarDatos(museo)
        elif x== 'ARRAY_LIST':
            museo= museoArrayList()
            cargarDatos(museo)
        
        print('Informacion de artistas cargados' + str(lt.size(museo['artistas'])))
        print('Información de las obras cargadas'+ str(lt.size(museo['artistas'])) )
        print('Artistas cargados: ' + str(lt.size(museo['artistas'])))
        print('Obras cargados: ' + str(lt.size(museo['obras'])))
        print('Ultimas tres obras'+ str(controller.darUltimasObras(museo['obras'])))
        print('Ultimos tres artistas'+ str(controller.darUltimosArtistas(museo['artistas'])))

    elif int(inputs[0]) == 2:
        articulo= 'artistas'
        lista= museo[articulo]
        y= int(input('Indique el temaño de la muestra'))

        if int(y)<=lt.size(museo[articulo]):
            lista_cortada= controller.cortarLista(lista, y)
            x= input('Diga que tipo de ordenamiento iterativo desea, entre Insertion, Shell, Merge y Quick')
            fechai= input('Inserte el año inicial en el formato AAAA')
            fechaf= input('Inserte el año final en el formato AAAA')
            start_time = time.process_time()
        
            if x=='Insertion':
                museo= museoArrayList()
                z= controller.sortArrayListArtistInsertion(lista_cortada)
            elif x=='Shell':
                z= controller.sortArrayListArtistShell(lista_cortada)

            elif x== 'Merge':
                z= controller.sortArrayListArtistMerge(lista_cortada)

            elif x== 'Quick':
                z= controller.sortArrayListArtistQuick(lista_cortada)
            

            lista_final= controller.fechasRangoArtist(z[0], fechai, fechaf)
            stop_time = time.process_time()
            elapsed_time_mseg = (stop_time - start_time)*1000
            ultimas=controller.darUltimosArtistas(lista_final)
            primeras=controller.darPrimerosArtistas(lista_final)
            print(ultimas)
            print(primeras)

            print("Artistas nacidos en el rango de fechas:"+ str(lt.size(lista_final)))
            print('Primeros tres artistas:')
            imprimirDatosArtista(primeras)
            print('Ultimos tres artistas: ') 
            imprimirDatosArtista(ultimas)
            print('El ordenamiento tomo'+ elapsed_time_mseg+ 'tiempo en mseg')
        else: 
            print("El tamaño de la muestra pedido supera la cantidad de datos  cargados")


    elif int(inputs[0]) == 3:
        articulo= 'obras'
        lista= museo[articulo]
        y= int(input('Indique el temaño de la muestra'))

        if int(y)<=lt.size(museo['obras']):
            lista_cortada= controller.cortarLista(lista, y)
            x= input('Diga que tipo de ordenamiento iterativo desea, entre Insertion, Shell, Merge y Quick')
            fechai= input('Inserte la fecha inicial en el formato AAAA-MM-DD')
            fechaf= input('Inserte la fecha final en el formato AAAA-MM-DD')
            start_time = time.process_time()
        
            if x=='Insertion':
                museo= museoArrayList()
                z= controller.sortArrayListInsertion(lista_cortada)
            elif x=='Shell':
                z= controller.sortArrayListShell(lista_cortada)

            elif x== 'Merge':
                z= controller.sortArrayListMerge(lista_cortada)

            elif x== 'Quick':
                z= controller.sortArrayListQuick(lista_cortada)

            lista_final= controller.fechasRango(z[0], fechai, fechaf)
            stop_time = time.process_time()
            elapsed_time_mseg = (stop_time - start_time)*1000
            ultimas=controller.darUltimasObras(lista_final)
            primeras=controller.darPrimerasObras(lista_final)
            print(ultimas)
            print(primeras)

            print("Aquisiciones en el rango de fechas:"+ str(lt.size(lista_final)))
            print("Obras adquiridas por compra: " + str(controller.obrasPurchase(lista_final)))
            print('Primeras tres obras:')
            imprimirDatosArtista(primeras)
            print('Ultimas tres obras: ') 
            imprimirDatosArtista(ultimas)
            print('El ordenamiento tomo'+ elapsed_time_mseg+ 'tiempo en mseg')
            
        else: 
            print("El tamaño de la muestra pedido supera la cantidad de datos cargados")
    

    elif int(inputs[0]) == 4:
        print("Obras de un artista ordenadas por técnica:")

    elif int(inputs[0]) == 5:
        print("Obras clasificadas por la nacionalidad de su creado:")

    elif int(inputs[0]) == 6:
        print("Costo de transportar las obras de un departamento:")

    elif int(inputs[0]) == 7:
        print("Nueva exposición propuesta según el area disponible:" )

    elif int(inputs[0]) == 0:
        sys.exit(0)

