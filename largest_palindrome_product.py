#!/bin/python3

def isPalindrome(val):
    return str(val) == str(val)[::-1]

v1 = 1000000
palindromes = [i for i in range(0, v1 + 1) if isPalindrome(i)]
palindromes.reverse()
val = None

for p in palindromes:
    for d in range(100, 1000):
        if p % d == 0  and len(str(p // d)) == 3:
            val = p
            break
    if val:
        break

print(val)
