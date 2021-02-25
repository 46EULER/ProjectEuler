# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def isNumPalindromic(n):
    numStr = str(n)
    for loopI in range(len(numStr) // 2):
        if numStr[loopI] != numStr[-1 - loopI]:
            return False
    return True


def solveQ004(maxNum):
    temResult = 1
    for i in range(1, maxNum):
        for j in range(1, maxNum):
            product = i * j
            if isNumPalindromic(product):
                if product >= temResult:
                    temResult = product
    return temResult


if __name__ == "__main__":
    print(solveQ004(999))
