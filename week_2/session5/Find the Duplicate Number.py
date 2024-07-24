#Floyds cycle Detection algorithm
#Time : O(n)
#space : O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = nums[0]
        #part-1: find the meeting points of the two pointers [slow and fast]
        while True:
            #one step at a time
            slow = nums[slow]
            #two step at a time
            fast = nums[nums[fast]]
            #meeting point
            if slow == fast:
                break
        #part-2: find the starting point/entrance of cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return fast