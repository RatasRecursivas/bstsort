'''
Created on 29/05/2013

@author: pperez
'''

from bst import BST

def bstsort(l):
    arbol = BST(l)
    
    for (idx, item) in enumerate(arbol.inorder()):
        l[idx] = item
