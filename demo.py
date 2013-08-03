#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 29/05/2013

@author: pperez
@author: srocha

Codigo de plot tomado flaitemente de https://github.com/cseager/timeit_plot larga vida al software libre :)
'''

import random
import sys
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
import timeit

# Inicializamos el random con seed 100
rand = random.Random(100)

# Ampliamos el limite de recursividad
sys.setrecursionlimit(999999999)

# Cantidad de repeticiones por cada n
reps = 1

def timer(stmt, setup = 'pass'):
    return timeit.Timer(stmt, setup=setup)

def substitute_titles(label, series):
    ordered_axes=["x", "y", "z"]
    try: 
        for i, v in enumerate(series): 
            label = label.replace("{"+str(v)+"}", ordered_axes[i])
    except: 
        label = label.replace("{"+str(series)+"}", ordered_axes[0])
    return label

def timeit_plot2D(data, xlabel='xlabel', title='title', **kwargs):
    """Plots the results from a defaultdict returned by timeit_compare.
    
    Each function will be plotted as a different series. 
    
    timeit_compare may test many conditions, and the order of the conditions
    in the results data can be understood from the string substitutions 
    noted in the keys of the defaultdict. By default series=0 means
    that the first series is plotted, but this can be changed to plot 
    any of the testing conditions available. 
    """
    series = kwargs.get('series', 0)
    style = kwargs.get('style', 'line')
    size = kwargs.get('size', 500)
    ylabel = kwargs.get('ylabel', 'time')
    cmap = kwargs.get('cmap', 'rainbow')
    lloc = kwargs.get('lloc', 2)
    dataT = {}
    # set color scheme
    c = iter(plt.get_cmap(cmap)(np.linspace(0, 1, len(data))))
    # transpose the data from [x, y, z]... into ([x...], [y...], [z...])
    for k, v in data.items():
        dataT[k] = zip(*v)
    fig, ax = plt.subplots()
    for k, v in dataT.items():
        if style == 'scatter':
            ax.scatter(v[series], v[-1], s=size, c=next(c), alpha=.75)
        elif style == 'bubble':
            x, y, z = v[series[0]], v[series[1]], v[-1]
            ax.scatter(x, y, s=[size*i for i in z], c=next(c), alpha=.5)
        else:
            # pdb.set_trace()
            ax.plot(v[series], v[-1], c=next(c), lw=2)
    # TODO: BUG: no way to set other parameters manually (README fig2)
    ax.legend([substitute_titles(k,series) for k in dataT.keys()], loc=lloc)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid(True)
    return fig


# Genera una lista aleatoria, el rango es 10 veces mayor a n para dispersar los datos
def muestra(n):
    return [rand.randint(0, 10 * n) for _ in range(n)]

if __name__ == '__main__':
    res = defaultdict(list) # Diccionario con los resultados en tiempo, despues lo pasamos a la funcion que hace el grafico
    count = 0

    while True:
        print "Ingrese los N a probar, separados por espacio"
        casos = raw_input()
        try:
            casos = [int(n) for n in casos.split()]
            break # No nos pillo la excepcion, estamos OK!
        except ValueError:
            print "Epa! Python se mareo tratando de convertir los N a enteros, seguros que eran enteros?"
            print "Hiciste triste a python :("
    
    while True:
        print "Desea mostrar las listas generadas? [s/N]"
        resp = raw_input().lower()
        
        if resp == 's': # Si queremos mostrar las listas
            mostrar_l = True
        elif resp == 'n' or resp == '': # Si ingreso no, o no ingreso nada, no le mostramos las listas
            mostrar_l = False
        else:
            print "Ingreso algo extranio, intente de nuevo!"
            continue
        break # Si el else no agarra el caso, quiere decir que ingreso 's' o 'n', avanzamos en el programa
    

    for n in casos:
        setup = 'from bstsort import bstsort; from __main__ import l' # Importamos la funcion
        l = muestra(n) # Generamos la lista aleatoria de numeros
        stmt = 'bstsort(l)'
        if mostrar_l: # Vemos si mostramos o no la lista
            print "l = %s" % l
        
        test = timer(stmt, setup)
        result = test.timeit(number = reps)
        count += result
        res[stmt].append([n, result])
        
        print "bstsort: N = %d; T = %s s" % (n, result)
        if mostrar_l: # Vemos si mostramos o no la lista
            print "l = %s" % l
        print
    print "Y solo perdimos {0:.2f} segundos de nuestras vidas ;-)".format(count)
    raw_input("Presione una tecla para continuar")

    timeit_plot2D(res, 'n', 'BSTSort')
    # plt.savefig('resultado.png')
    plt.show()
