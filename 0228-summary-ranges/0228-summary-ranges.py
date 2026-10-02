class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :type rtype: List[str]
        """
        if not nums:
            return []
        
        ranges = []
        start = nums[0]
        
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                if start == nums[i]:
                    ranges.append(str(start))
                else:
                    # Replaced f-string with .format() for Python 2 compatibility
                    ranges.append("{}->{}".format(start, nums[i]))
                
                if i < len(nums) - 1:
                    start = nums[i + 1]
                    
        return ranges
