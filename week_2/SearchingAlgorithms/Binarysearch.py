def BinarySearch(arr,  target):
    start=0
    end=len(arr)-1
    while start <= end:
        mid = start+(end-start)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1




#driver code
arr = [12,14,17,29,31,45,62]
target = 17
n=len(arr)
result = BinarySearch(arr,  target)
print(result)

#time complexity: O(log n)
#space complexity : O(1)