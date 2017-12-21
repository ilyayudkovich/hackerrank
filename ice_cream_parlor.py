#!/bin/python

def solve(arr, money):
    # Complete this function

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                continue
            if arr[i] + arr[j] == money:
                print(i, j)
                return



if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        # the total amount of money to spend
        money = int(input().strip())
        # number of flavors
        n = int(input().strip())
        # the costs of ice cream
        arr = list(map(int, input().split(' ')))
        solve(arr, money)
