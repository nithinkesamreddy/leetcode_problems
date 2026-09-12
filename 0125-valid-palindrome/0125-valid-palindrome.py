class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a= "".join(char.lower() for char in s if char.isalnum())
        return a==a[::-1]

           
        