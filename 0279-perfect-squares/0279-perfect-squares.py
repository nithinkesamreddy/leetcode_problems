class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr= [0] + [n] * n
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                arr[i] = min(arr[i], arr[i - j * j] + 1)
                j += 1
                
        return arr[n]
        