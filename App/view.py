"""
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
        print('Ultimas tres obras'+ str(controller.darUltimasObras(museo)))
        print('Ultimos tres artistas'+ str(controller.darUltimosArtistas(museo)))

    elif int(inputs[0]) == 2:
        print("Artistas ordenados cronológicamente:")

    elif int(inputs[0]) == 3:
        print("Adquisiciones ordenadas cronológicamente:")

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

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = initCatalog()
        loadData(catalog)
        print('Libros cargados: ' + str(lt.size(catalog['books'])))
        print('Autores cargados: ' + str(lt.size(catalog['authors'])))
        print('Géneros cargados: ' + str(lt.size(catalog['tags'])))
        print('Asociación de Géneros a Libros cargados: ' +
              str(lt.size(catalog['book_tags'])))

    elif int(inputs[0]) == 2:
        number = input("Buscando los TOP ?: ")
        books = controller.getBestBooks(catalog, int(number))
        printBestBooks(books)

    elif int(inputs[0]) == 3:
        authorname = input("Nombre del autor a buscar: ")
        author = controller.getBooksByAuthor(catalog, authorname)
        printAuthorData(author)

    elif int(inputs[0]) == 4:
        label = input("Etiqueta a buscar: ")
        book_count = controller.countBooksByTag(catalog, label)
        print('Se encontraron: ', book_count, ' Libros')

    else:
        sys.exit(0)
sys.exit(0)