#!/usr/bin/env python
# -*- coding: utf-8 -*- 

'''
Created on 29/05/2013

@author: pperez
'''

import random
from time import time
from bstsort import bstsort
import sys

# Inicializamos el random con seed 100
rand = random.Random(100)

# Ampliamos el limite de recursividad
sys.setrecursionlimit(999999999)

# Genera una lista aleatoria, el rango es 10 veces mayor a n para dispersar los datos
def muestra(n):
    l = []
    lim = 5 * n
    l = [rand.randint(-lim, lim) for _ in range(n)]
    return l

if __name__ == '__main__':
    res = {} # Diccionario con los resultados en tiempo
    
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
        l = muestra(n) # Generamos la lista aleatoria de numeros
        if mostrar_l: # Vemos si mostramos o no la lista
            print "l = %s" % l
        
        t_inicio = time() # En sus marcas ... Listos ... Fuera
        bstsort(l) # Pongele
        t_fin = time() # Listo listo listo
        tiempo_ejecucion = (t_fin - t_inicio) * 1000.0 # Calculamos el timer que tardo el sorting (en ms)
        res[n] = tiempo_ejecucion # Medimos el tiempo y almacenamos el resultado
        
        print "bstsort: N = %d; T = %s ms" % (n, res[n])
        if mostrar_l: # Vemos si mostramos o no la lista
            print "l = %s" % l
        print
    # Aca faltaria el codigo para generar el grafico con matplotlib
