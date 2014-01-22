#!/usr/local/bin/python
from random import randint

def random_dice():
    return randint(1, 6)

def report(tot, extracted):
    print "After {0} extraction, these are the frequencies".format(tot)
    print extracted
    sumt = 0.0 + sum(extracted)
    frequency = [ n/sumt for n in extracted]
    print frequency
    print

extracted = [0,0,0,0,0,0]

i = 0
while True:
    i = i + 1
    dice = random_dice()
    extracted[dice-1] = extracted[dice-1]+1
    if i%1000000 == 0:
        report(i, extracted)
