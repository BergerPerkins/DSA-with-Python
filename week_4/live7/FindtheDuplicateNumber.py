##############              https://leetcode.com/problems/find-the-duplicate-number/description/            ###############


##    Hashing   ##

## Time : O(n)+ O(n) +> O(n)
## space : O(n)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Create a empty hash table {key:value}
        # O(n) -> to create hash table
        count_dict = {}

        for num in nums:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        # Constraint (value > 1: duplicate number[return key])
        # O(n) -> to get tht key having count > 1
        for num, count in count_dict.items():
            if count > 1:
                return num

        # duplicates = [num for num, count in count_dict.items() if count > 1]
        # return duplicates[0]