n = int(input())

values = map(int, input().split())

total_sum = sum(values)

print("%.1f" % total_sum / n)

def calculateMedian(arr):
    arr = sorted(arr)
    if n % 2 is 1:
        return arr[ n // 2]
    else:
        return (arr[n // 2]  + arr[(n // 2) -1]) / 2 

print("%.1f" % calculateMedian(values))

values = sorted(values)

from collections import Counter
print(Counter(values).most_common()[0][0])

