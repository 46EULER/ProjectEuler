# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
from math import sqrt
N = 600851475143
def findPart(x):
    i = 2
    while i <= x:
        if x % i == 0:
            return i
        i += 1
def makeallFactors(n):
    loopFunc = True
    result = []
    while loopFunc:
        a = findPart(n)
        if a != n:
            result.append(a)
            n = n / a
        else:
            result.append(a)
            loopFunc = False
    return result

def maxList(thisList):
    if thisList ==[] :
        return "empty"
    maxElement = thisList[0]
    for eachElement in thisList:
        if eachElement > maxElement:
            maxElement = eachElement
    return maxElement

if __name__ == "__main__":
    print(maxList(makeallFactors(600851475143)))