class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low,high=0,len(numbers)-1
        while low<high:
            summation=numbers[low]+numbers[high]
            if summation == target:
                return [low+1,high+1]
            elif summation > target:
                high-=1
            else:
                low +=1
        return [-1,-1]
    
#timecomplexity O(n)
#space complexity O(1)