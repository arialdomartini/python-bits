#!/usr/local/bin/python
from random import randint

def random_dice():
    return randint(1, 6)

def sum_of_n_dices(n):
    return sum([ random_dice() for i in range(n)])

def average(n):
    return (6.0 + 1.0) / 2*n

def test_with_n_dices(n, m): 
    print "I'm rolling %s dices %s times: " % (n, m),
    sum = 0
    for i in range(m):
        sum = sum + sum_of_n_dices(n)

    obtained_average = (1.0*sum)/m
    theoretical_average = average(n)
    distance = abs(obtained_average-theoretical_average)
    print "sum=%s; average=%s; distance: %s" %(sum, obtained_average, distance)

print "I'll experiment with the fact that the greatest the number of rolls, the"
print "smaller is the error. Rolling a lot of dices, the average sum is closer"
print "to the average value. Errors compensate, rather than accumulate"

n=3
test_with_n_dices(n, 1)
test_with_n_dices(n, 3)
test_with_n_dices(n, 5)
test_with_n_dices(n, 10)
test_with_n_dices(n, 30)
test_with_n_dices(n, 50)
test_with_n_dices(n, 100)
test_with_n_dices(n, 1000)
test_with_n_dices(n, 5000)
test_with_n_dices(n, 10000)
test_with_n_dices(n, 100000)
test_with_n_dices(n, 200000)

