class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #l=len(num)
        num=sorted(set(nums),reverse=True)
        if len(num)>=3:
            return num[2]
        return num[0]
        
        