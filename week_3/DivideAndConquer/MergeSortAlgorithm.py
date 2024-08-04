## Time complexity
## recurrence relation 
## T(n) = 2T(n/2) + n  = O(n log n)

## Space complexity --> O(n)

# function definitin of mergeprocedure
# complexity of combine-->> n
def mergeprocedure(arr, start, mid, end):
    ## create and initialize the left and right sorted sub array
    L = arr[start:mid+1]
    R = arr[mid+1:end+1]
    m = n = 0
    K = start

    while m < len(L) and n < len(R):
        if L[m] < R[n]:
            arr[K] = L[m]
            m += 1
        else:
            arr[K] = R[n]
            n += 1
        K += 1

    ## copying the remeining elements of left sub array
    while m < len(L):
        arr[K] = L[m]
        m += 1
        K += 1
    
    ## copying the remaining elements of right sub array
    while n < len(R):
        arr[K] = R[n]
        n += 1
        K += 1

# function definition of array
## approach : Divide and Conquer
def mergesort(arr, start, end):
    if start < end:
        # 1. Divide --> c
        mid = start + (end - start)//2
        # 2. Conquer --> 2T(n/2)
        # recursive call for the left subtree
        mergesort(arr, start, mid)
        # recursive call for the right subtree
        mergesort(arr, mid+1, end)
        # 3. combine --> n
        # combine the reults of both left and right subtree
        mergeprocedure(arr, start, mid, end)


#driver code
arr = [50,20,45,11,15,27,34]
start = 0
end = len(arr)-1
n=len(arr)
#functioncalling
mergesort(arr, start, end)

#print the elements in the array
for i in range(len(arr)):
    print(arr[i], end=" ")
