class Solution(object):
    def intersect(self, nums1, nums2):
        if len(nums1) < len(nums2):
            smaller_list = nums1
            larger_list = nums2
        else:
            smaller_list = nums2
            larger_list = nums1
            
        result = []
        
        for num in smaller_list:
            if num in larger_list:
                result.append(num)
                larger_list.remove(num)
                
        return result
