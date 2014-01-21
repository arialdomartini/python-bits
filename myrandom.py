#!/usr/local/bin/python
from random import random


somme = []
tot = 100
q = 100000
for p in range(tot):
    i = 0.0
    for n in range(q): 
        rnd = random()
        if rnd < 0.5:
            i=i-1
        else:
            i=i+1
    somme.append(i)
print somme
print sum(s for s in somme) / tot

