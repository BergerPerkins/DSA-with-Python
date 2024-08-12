#########                   https://leetcode.com/problems/majority-element/description/             #############3

## Algorithm:  Boyer Moore Voting Algorithm
## Time : O(n)
## Space : O(1)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if candidate == num else -1)
        return candidate