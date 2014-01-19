#!/usr/local/bin/python
from random import randint

def random_dice():
    return randint(1, 6)

def sum_of_n_dices(n):
    return sum([ random_dice() for i in range(n)])

def test_with_n_dices(n, m): 
    print "I'm rolling %s dices %s times: " % (n, m),
    sum = 0
    for i in range(m):
        sum = sum + sum_of_n_dices(n)

    print "sum=%s; average=%s" %(sum, (1.0*sum)/m)

print "I'll experiment with the fact that the greatest the number of rolls, the"
print "smaller is the error. Rolling a lot of dices, the average sum is closer"
print "to the average value. Errors compensate, rather than accumulate"

test_with_n_dices(2, 1)
test_with_n_dices(2, 3)
test_with_n_dices(2, 5)
test_with_n_dices(2, 10)
test_with_n_dices(2, 30)
test_with_n_dices(2, 50)
test_with_n_dices(2, 100)
test_with_n_dices(2, 1000)
test_with_n_dices(2, 5000)
test_with_n_dices(2, 10000)
test_with_n_dices(2, 100000)
test_with_n_dices(2, 200000)

