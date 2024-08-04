## https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
# time complexity = O(m+n)
# space complexity = O(1)

class Solution:
    def merge(self, nums1, m, nums2, n):
        k = m+n-1
        i=m-1
        j=n-1
        while i >= 0 and j >= 0:
            if nums1[i] <= nums2[j]:
                nums1[k] = nums2[j]
                j-=1
            else:
                nums1[k] = nums1[i]
                i -= 1
            k -= 1
        while j >= 0:
            nums1[k]=nums2[j]
            j-=1
            k-=1