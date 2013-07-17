#! /usr/bin/env python

## Program to find the prime numbers from 1 to n.

import math
from timeit import time

primeno = []

def prime(n):
    for i in xrange(2, n + 1):
        sq = math.sqrt(i)
        count = 0
        for j in primeno:
            if j > sq + 1:
                break
            if i % j == 0:
                count += 1
                break
        if count == 0:
            primeno.append(i)

start_time = time.time()
prime(10**5)  # You can specify any number
end_time = time.time()
total_time = end_time - start_time # Time in seconds
#print primeno # uncomment this line if you want to see the prime numbers.
print 'Total time:', total_time
