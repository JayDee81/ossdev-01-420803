import sys
import math


def eratosthenes(start, end):
    """Return prime numbers between start and end"""
    # check if input is valid
    if start < 0 or end < 0:
        raise Exception('Both input numbers have to be >= 0')

    # swap start and end if needed
    if start > end:
        start, end = end, start

    arr = []

    # initialize array
    for i in range(0, end):
        if i < max(start, 2):
            arr.append(False)
        else:
            arr.append(True)

    # Eratosthenes sieve
    for i in range(2, math.ceil(math.sqrt(end))):
        if arr[i] is True:
            for j in range(i**2, end, i):
                arr[j] = False

    # extract primes
    ret = []
    for i in range(start, end):
        if arr[i]:
            ret.append(i)

    return ret
