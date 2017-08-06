"""
This RSA algorithm is written by taking
"Introduction to Algorithms - CLRS" as reference

Author: Ankit Goyal
"""
import random


def extendedEuclidean(num1, num2):
    """
    This is an extension of euclid's algorithm to find gcd of two numbers
    It solves for x, y in the following equation
    num1 * x + num2 * y = gcd(num1, num2)
    Refer wikipedia's page or section 31.2 in CLRS
    """
    if num2 == 0:
        return (num1, 1, 0)

    d, temp_x, temp_y = extendedEuclidean(num2, num1 % num2)

    # TODO: see python notebook for explanation
    x, y = temp_y, temp_x - int(num1 / num2) * temp_y

    return (d, x, y)


def isPrime(num):
    """
    Checking for the primality of the number
    """
    if num % 2 == 0 and num > 2:
        return False
    i = 3
    num_sqrt = num**0.5
    while i <= num_sqrt:
        if num % i == 0:
            return False
        i += 2
    return True


def multiplicativeInverse(a, b, n):
    """
    Generating multiplicative inverse of given numbers (a,b modulo n)
    Refer Section 31.4 CLRS
    """
    # TODO: Mathematical proof in python notebook
    d, x, y = extendedEuclidean(a, n)
    if b % d == 0:
        temp_x = (x * (b/d)) % n
        result = []
        for i in range(d):
            result.append((temp_x + i*(n/d)) % n)
        return result
    return []


def generateRandomPrime(bits):
    """
    Generate <bits> bit random prime number
    """
    num = random.getrandbits(bits)
    print "Try: {}".format(num)
    while(not isPrime(num)):
        num += 2
        print "Try: {}".format(num)

    return num


def RSA():
    p = generateRandomPrime(512)
    q = p
    while q == p:
        q = generateRandomPrime(512)
    n = p*q
    phi = (p-1) * (q-1)


if __name__ == "__main__":
    print generateRandomPrime(512)
