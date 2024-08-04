## function definition of partition
def partition(arr, p, q):
    pivot = arr[p]
    i = p
    for j in range(i+1, q+1):
        if arr[j] <= pivot:
            i = i+1
            ## swap arr[i] with arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    ## final swap between arr[i] and pivot
    arr[i], arr[p] = arr[p], arr[i]
    return i


# Function definition of quicksort
def quicksort(arr, p, q):
    if p < q:
        ## 1. Divide
        mid = partition(arr, p, q)
        ## 2. Conquer
        ## recursively call left sub tree
        quicksort(arr, p, mid-1)
        ## recursively call right sub tree
        quicksort(arr, mid+1, q)
    return arr










## Driver code
arr = [50, 20, 45, 11, 15, 27, 34]
p = 0
q = len(arr) - 1
#function calling
result = quicksort(arr, p, q)
print(result)