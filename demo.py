'''
Created on 29/05/2013

@author: pperez
'''

import random as rand
from timeit import Timer

# Inicializamos el random con seed 100
rand.seed(100)

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
        elif resp == 'n':
            mostrar_l = False
        else:
            print "Ingreso algo extra–o, intente de nuevo!"
            continue
        break # Si el else no agarra el caso, quiere decir que ingreso 's' o 'n'
    
    for n in casos:
        l = [] # Lista vacia
        setup = 'from bstsort import bstsort; for i in range(%d): l.append(%d)' % (n, rand.randint(0, 1000)) # Llenamos con numeros aleatorios
        
        if mostrar_l:
            print "l = %s" % l
        stmt = 'bstsort(l)'
        timer = Timer(stmt, setup) # Seteamos el timer para el statement donde se hace sort
        res[n] = timer.timeit(1) # Medimos el tiempo y almacenamos el resultado
    
    for n in sorted(res):
        print "bstsort: N = %d; T = %s" % (n, res[n])
    
    # Aca faltaria el codigo para generar el grafico con matplotlib