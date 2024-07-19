###############################################     REVERSAL OF ARRAY    ######################################

#approach 1 -->slicing indexing
#function definition
def reverse(arr):
  rev = arr[::-1]
  return rev

##driver code
arr=[2,1,7,9,12,4]
result=reverse(arr)
print(result)
#timecomplexity O(n)
#space complexity O(1)

###################################
#approach 2 -->negative indexing
#function definition
def reverse(arr):
  ans=[]
  for i in range(1,len(arr)+1):
    ans.append(arr[-i])
  return ans


##driver code
arr=[2,1,7,9,12,4]
result=reverse(arr)
print(result)
#timecomplexity O(n)
#space complexity O(n)

#####################################
#approach 3 --> two pointer approach
def reverse(arr):
  n=len(arr)
  i=0
  j=n-1
  while i<j:
    arr[i],arr[j] = arr[j],arr[i]
    i = i+1
    j = j-1
  return arr

##driver code
arr=[2,1,7,9,12,4]
result=reverse(arr)
print(result)
#timecomplexity O(n)
#space complexity O(1)

