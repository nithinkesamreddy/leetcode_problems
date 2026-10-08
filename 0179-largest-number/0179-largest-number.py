class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        num_str = sorted(map(str, nums), key=lambda x: x * 10, reverse=True)
        return "0" if num_str[0] == "0" else "".join(num_str)
        