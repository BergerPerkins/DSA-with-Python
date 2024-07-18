
  ####    https://leetcode.com/problems/search-a-2d-matrix/?envType=study-plan-v2&envId=top-interview-150    ####

#time complexity : O(log(m*n))
#space complexity : O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m-> no of rows
        #n -> no of columns
        m= len(matrix)
        n= len(matrix[0])
        # implementation of binary search
        low, high = 0, m * n -1
        while low <= high:
            mid = low + (high - low)//2
            row_idx = mid//n
            col_idx = mid%n
            midElement = matrix[row_idx][col_idx]
            #implementation of binary search
            if target == midElement:
                return True
            #exploring target value towards left side of mid
            elif target < midElement:
                high = mid - 1
            
            #exploring target values towards right side of mid
            else:
                low = mid + 1
        return False