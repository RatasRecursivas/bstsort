'''
Created on 29/05/2013

@author: pperez
'''

from bstsort import bstsort
import random

random.seed(100)

l = [random.randint(0, 1000) for i in range(10)]
print l

bstsort(l)
print l