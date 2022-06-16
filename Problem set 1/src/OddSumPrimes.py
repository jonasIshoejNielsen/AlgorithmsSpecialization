from sys import stdin, argv
import sys
import sympy.ntheory as nt
import math
from FFT import fft, ifft, multiply2Polynomials, roundLst


def parse_start():
    n=0
    for (line_number, line) in enumerate(stdin):
        if line_number==0:
            n = int(line)
            break
    return n

def getPrimes(n):
    return list(nt.primerange(0, n))

def primesToCoefficient(primes, n):
    res = [0]*(n+1)
    for prime in primes:
        res[prime]=1
    return res

def getHowManyFor(n):
    primes=getPrimes(n)
    coeff=primesToCoefficient(primes,n)    
    coeff_squared=multiply2Polynomials(coeff, coeff)
    coeff_cubed=multiply2Polynomials(coeff, coeff_squared)
    return round(coeff_cubed[n].real)

def getHowManyCaching(n, coeff_cubed):
    primes=getPrimes(max)
    coeff=primesToCoefficient(primes,max)    
    coeff_squared=multiply2Polynomials(coeff, coeff)
    coeff_cubed=multiply2Polynomials(coeff, coeff_squared)
    for n in range(7,max,2):
        print(n,"\t",getHowManyCaching(n, round(coeff_cubed[n].real)))


def main():
    max = 100000     #any more and it begins taking minutes
    getHowManyCaching(max)


main()