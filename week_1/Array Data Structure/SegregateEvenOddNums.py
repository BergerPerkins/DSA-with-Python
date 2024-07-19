########################################     Segregate Even Odd Nums    ######################################

#approach 1 --> two pointer approach
def segre(arr):
  ans=[]
  for i in range(len(arr)):
    if arr[i]%2==0:
      ans.append(arr[i])
  for i in range(len(arr)):
    if arr[i]%2!=0:
      ans.append(arr[i])
  return ans



arr=[7,2,9,4,6,1,3,8,5]
result=segre(arr)
print(result)
#timecomplexity O(n)
#space complexity O(n)
##############################################

#approach 2 --> two pointer approach
def segre(arr):
  i=-1
  j=0
  n=len(arr)
  while j != n:
    if arr[j] %2 == 0:
      i=i+1
      arr[i],arr[j]=arr[j],arr[i]
    j=j+1
  return arr


arr=[7,2,9,4,6,1,3,8,5]
result=segre(arr)
print(result)
#timecomplexity O(n)
#space complexity O(1)
