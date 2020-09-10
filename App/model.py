"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
import csv
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from time import process_time 
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def newCatalog():
    """ Inicializa el catálogo de peliculas
    Crea una lista vacia para guardar todas las peliculas
    Se crean indices (Maps) por los siguientes criterios:
    Retorna el catalogo inicializado.
    """
    catalog = {'original_title': None,
               'id': None,
               'date': None,
               'average_count': None,
               'vote_count': None,
               'language': None}

    catalog['original_title'] = lt.newList('SINGLE_LINKED', compareMoviesIds)

    catalog['id'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapMovieIds)
    catalog['date'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapYear)
    catalog['average_count'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compareMapAverage)
    catalog['vote_count'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compareMapVote)
    catalog['language'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareMapLanguage)

    return catalog

# ==============================
# Funciones de consulta
# ==============================


# ==============================
# Funciones de Comparacion
# ==============================
def compareMoviesIds(id1, id2):
    """
    Compara los nombres de las movies
    """
    if (id1[0] < id2[0]):
        return 0
    elif id1[0] > id2[0]:
        return 1
    else:
        return -1


def compareMapMovieIds(id, entry):
    """
    Compara dos ids de peliculas, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (int(id) == int(identry)):
        return 0
    elif (int(id) > int(identry)):
        return 1
    else:
        return -1

def compareMapYear(id, entry):
    """
    Compara dos fechas de peliculas, id es un identificador
    y entry una pareja llave-valor
    """
    yearentry = me.getKey(entry)
    if (int(id) == int(yearentry)):
        return 0
    elif (int(id) > int(yearentry)):
        return 1
    else:
        return -1
def compareMapAverage(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    aventry = me.getKey(entry)
    if (float(id) == float(aventry)):
        return 0
    elif (float(id) > float(aventry)):
        return 1
    else:
        return -1
def compareMapVote(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (float(id) == float(identry)):
        return 0
    elif (float(id) > float(identry)):
        return 1
    else:
        return -1
def compareMapLanguage(id, entry):
    """
    Compara dos ids de libros, id es un identificador
    y entry una pareja llave-valor
    """
    identry = me.getKey(entry)
    if (id[0] == identry[0]):
        return 0
    elif (id[0] > identry[0]):
        return 1
    else:
        return -1
