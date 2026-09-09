class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums)!=0:
            for j in range(len(nums)-1):
                for i in range(len(nums)-1):
                    if nums[i]>=nums[i+1]:
                        temp=nums[i]
                        nums[i]=nums[i+1]
                        nums[i+1]=temp
            return nums
        return []



