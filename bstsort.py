'''
Created on 29/05/2013

@author: pperez
'''

from bst import BST

def bstsort(l):
    arbol = BST()
    
    while l:
        item = l.pop()
        arbol.add(item)
    
    l.extend(arbol.inorder())
