# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
from math import sqrt
def findFactorProduct(n):
    product = [1]
    for i in range(1,int(sqrt(n))+1):
        if n % i == 0:
            product.append() = product * i

def solveQ005(maxNum):
    product = 1
    for eachNum in range(1, maxNum):
        if product % eachNum != 0:
            product = product * eachNum
    return product


if __name__ == "__main__":
    print(solveQ005(20))
