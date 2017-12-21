#!/bin/python3


def sliceAbbr(piece, b):
    for c in range(len(b)):
        if piece[c] == b[c] or piece[c].upper() == b[c]:
            if c is len(b) - 1:
                return True
            continue
        else:
            break
    return False

def noUppers(string):
    for i in string:
       if i == i.upper():
           return False
    return True

def removal(a, b):
    for c in a:
        if not c in b and not c == c.upper() and not c.upper() in b:
            a = a.replace(c, '')
    return a

def abbreviation(a, b):
    sl = len(b)
    a = removal(a, b) 
    print(a)
    if sl > len(a):
        return 'NO'

    for i in range(0, len(a) - sl + 1):
        piece = a[i:i + sl]
        if sliceAbbr(piece, b):
           return 'YES' 
    return 'NO'

a = 'daBdcD'
b = 'ABC'

print(abbreviation(a, b))
                 


