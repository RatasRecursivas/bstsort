'''
Created on 29/05/2013

@author: pperez
'''

from bst import BST

def bstsort(l):
    arbol = BST()
    # Generamos nuestra estructura 
    # de datos auxiliar
    
    while l:
        # Vaciamos la lista en el arbol
        item = l.pop()
        arbol.add(item)
    
    l.extend(arbol.inorder())
    # Ingresamos a la lista los 
    # elementos con el recorrido EnOrden
