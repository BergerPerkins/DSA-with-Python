#function definition
def LinearSearch(arr, n, target):
    for i in range(n):
        if arr[i]==target:
            return i
    return -1




#driver code
arr = [12,14,11,29,31,45,62]
target = 31
n=len(arr)
result = LinearSearch(arr, n, target)
print(result)

#time complexity: O(n)
#space complexity : O(1)