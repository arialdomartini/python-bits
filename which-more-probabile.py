#!/usr/local/bin/python
from random import randint, seed

def random_dice():
    return randint(1, 6)

def report(tot, extracted):
    print "After {0} extraction, these are the number extracted".format(tot)
    print extracted
    print "There are the frequencies"
    sumt = 0.0 + sum(extracted)
    frequency = [ n/sumt for n in extracted]
    print frequency
    print

extracted = [0,0,0,0,0,0]

seed()
number_of_extractions = 1500000

for i in range(number_of_extractions):
    dice = random_dice()
    extracted[dice-1] = extracted[dice-1]+1

report(number_of_extractions, extracted)
