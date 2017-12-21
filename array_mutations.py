n, m = map(int, input().split(' '))

arr = input().split(' ')

for i in range(m):
    op, start, end = map(int, input().split(' '))
    elements = []
    for i in range(start - 1, end):
        elements.append(arr[start - 1])
        del arr[start - 1]
    if op is 1:
        arr = elements.extend(arr) 
    if op is 2:
        arr = arr.extend(elements)


print(arr[::n])
