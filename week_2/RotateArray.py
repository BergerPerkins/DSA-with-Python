class Solution:
    def reverse(self,nums,low,high):
        while low<high:
            nums[low],nums[high]=nums[high],nums[low]
            low=low+1
            high=high-1
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        self.reverse(nums,0,n-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,n-1)

#timecomplexity O(n)
#space complexity O(1)