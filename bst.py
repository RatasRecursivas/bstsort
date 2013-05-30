'''
Created on 29/05/2013

@author: pperez
'''

class BST(object):
    '''
    Implementaci?n _lisiada_ de un bst
    '''


    def __init__(self, iterable = None):
        '''
        Constructor
        '''
        self.raiz = {}  #NULL
        
        # Si pasa un iterable, llenamos el arbol con el
        if iterable is not None:
            for item in iterable:
                self.add(item)
            
    
    def add(self, dato, nodo=None):
        '''
        '''
        if nodo is None:
            nodo = self.raiz
        
        if nodo == {}:
            nodo['izq'] = {}
            nodo['der'] = {}
            nodo['key'] = dato
        else:
            if dato < nodo['key']:
                self.add(dato, nodo['izq'])
            else:
                self.add(dato, nodo['der'])
    
    def inorder(self, nodo = None, elementos = None):
        '''
        '''
        
        if nodo is None: # Primera ejecucion
            elementos = []
            nodo = self.raiz
        
        if nodo['izq'] != {}:
            self.inorder(nodo['izq'], elementos)
        
        elementos.append(nodo['key'])
        
        if nodo['der'] != {}:
            self.inorder(nodo['der'], elementos)
        
        return elementos
            
    def mostrar(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo != {}:
            self.mostrar(nodo['izq'])
            print nodo['key']
            #print "Dato:", nodo['key'], "Factor equilibrio", nodo['factor_equilibrio']
            self.mostrar(nodo['der'])
    
    def plot(self):
        '''
        '''
        pass
