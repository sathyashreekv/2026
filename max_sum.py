class Solution(object):
    def maxMatrixSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        total_sum=0
        neg=0
        mn_val=float('inf')

        for row in matrix:
            for val in row:
                total_sum+=abs(val)
                if val<0:
                    neg+=1
                mn_val=min(mn_val,abs(val))
        if neg%2==0:
            return total_sum
        else:
            return total_sum-(2*mn_val)