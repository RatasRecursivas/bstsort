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
        self.__l = {} # Lista interna
        
        # Si pasa un iterable, llenamos el arbol con el
        if iterable is not None:
            for item in iterable:
                self.add(item)
            
    
    def add(self, dato, nodo_idx=None):
        '''
        '''
        if nodo_idx is None:
            nodo_idx = 0 # Primer nodo
        l = self.__l
        nodo = l.get(nodo_idx, None)
        
        if nodo is None:
            l[nodo_idx] = dato
        else:
            if dato < nodo:
                nodo_idx = (2 * nodo_idx) + 1
            else:
                nodo_idx = (2 * nodo_idx) + 2
            self.add(dato, nodo_idx)
    
    def inorder(self, nodo_idx = None, elementos = None):
        '''
        '''
        
        if nodo_idx is None: # Primera ejecucion
            elementos = []
            nodo_idx = 0
        
        l = self.__l
        nodo = l.get(nodo_idx, None)
        hijo_izq = (2 * nodo_idx) + 1
        hijo_der = (2 * nodo_idx) + 2
        
        if l.get(hijo_izq, None) is not None:
            self.inorder(hijo_izq, elementos)
        
        elementos.append(nodo)
        
        if l.get(hijo_der, None) is not None:
            self.inorder(hijo_der, elementos)
        
        return elementos
    
    def plot(self):
        '''
        '''
        pass