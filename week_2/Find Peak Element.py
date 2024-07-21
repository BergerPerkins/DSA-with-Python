
######    https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=top-interview-150    ####

#time complexity : O(log n)
#space complexity : O(1)
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n=len(nums)
        low, high = 0, n-1
        if n == 1:
            return 0
        #implementation of Binary serch
        while low <= high:
            mid = low + (high - low)//2
            if (mid == 0 and nums[mid] > nums[mid + 1]) or \
             (mid== n - 1 and nums[mid] > nums[mid - 1]) or \
             (nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]):
                return mid

            elif nums[mid] < nums[mid + 1]:
                #explore towards right side of array
                low = mid + 1
            else:
                high = mid - 1 

