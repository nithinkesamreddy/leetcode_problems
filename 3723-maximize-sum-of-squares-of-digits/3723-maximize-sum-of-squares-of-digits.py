class Solution(object):
    def maxSumOfSquares(self, num, sum):
        """
        :type num: int
        :type sum: int
        :rtype: str
        """
        ans=[]
        for i in range (num):
            a=min(9,sum)
            ans.append(str(a))
            sum-=a
        if sum>0:
                return ""
        return "".join(ans)
        