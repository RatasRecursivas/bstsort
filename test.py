'''
Created on 28/06/2013

@author: pperez
'''

from bst import BST
from random import Random

r = Random(100)

l = r.sample(xrange(10000), 100)
print l

a = BST(l)

for i in a.inorder():
    print i