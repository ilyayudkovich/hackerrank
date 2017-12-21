import sys

string = input().strip()
try:
    print(int(string))
except:
    print('Bad String')
