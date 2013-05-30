'''
Created on 29/05/2013

@author: pperez
'''

from bst import BST

def bstsort(l):
    arbol = BST(l)
    for i in range(len(l)): l.pop(i) # Vaciamos la lista
    
    for item in arbol.inorder():
        l.append(item)