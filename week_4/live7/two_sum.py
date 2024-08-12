############                  https://leetcode.com/problems/two-sum/   

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # created a dictionary
        num_dict = {}
        for idx,num in enumerate(nums):
            # complement of given target and num value
            comp = target - num
            if comp in num_dict:
                return[num_dict[comp], idx]
            num_dict[num] = idx