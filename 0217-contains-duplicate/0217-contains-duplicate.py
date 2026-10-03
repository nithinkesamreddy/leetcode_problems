class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        view=set()
        for x in nums:
            if x in view:
                return True
            view.add(x)
        return False