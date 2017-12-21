
if __name__ == '__main__':
    n, m = input().split(' ')
    n, m = [int(n), int(m)]

    # create an array of all 0s
    arr = [0] * n
    max_val = -1
    for a0 in range(m):
        a, b, k = input().split(' ')
        a, b, k = [int(a), int(b), int(k)]
        for i in range(a- 1, b):
            arr[i] += k
            max_val = max(max_val, arr[i])

    print(max_val)

