# bubble sort algorithm

def bubbleSort(arr):
    # also keeps track of total number of swaps
    num_steps = 0
    for i in range(len(arr)):
        # checks to see how many elements have been swapped this round
        steps = 0
        for j in range(len(arr) - 1):
            # if the elements are in the wrong order
            if arr[j] > arr[j+1]:
                # swap em
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
                # incremenet counters
                num_steps += 1
                steps += 1
        # if no swaps took place, stop.
        if not steps:
            break
    
    # return the arr
    return arr


# insertion sort algorithm

def insertionSort(arr):
    # iterate over whole array
    for i in range(1, len(arr)):
        # get the value that needs to be inserted
        val = arr[i]
        # keep track of its index
        pos = i

        # while the index is greater than 0 and the value in the list is greater than our value        
        while pos > 0 and arr[pos - 1] > val:
            # move back the value
            arr[pos] = arr[pos - 1]
            # decrease the position
            pos -= 1
        # update the value
        arr[pos] = val


# quick sort algorithm

def quickSort(arr):
    # if it's one element
    if len(arr) <= 1:
        # return it
        return arr
    # otherwise
    else:
        # select pivot as first element 
        pivot = arr[0]
        # select all elements less/equal than it
        less_than = [i for i in arr[1:] if i <= pivot]
        # select all elements greater than it
        greater_than = [i for i in arr[1:] if i > pivot]
        # return the quick sort of less_than, plus pivot, plus greater_than
        return quickSort(less_than) + pivot + quickSort(greater_than)

