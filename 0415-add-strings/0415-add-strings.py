class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = []
        carry = 0
        
        p1 = len(num1) - 1
        p2 = len(num2) - 1
        
        while p1 >= 0 or p2 >= 0 or carry:
            d1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            d2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0
            
            total = d1 + d2 + carry
            carry = total // 10
            res.append(str(total % 10))
            
            p1 -= 1
            p2 -= 1
            
        # Reverse the result list and join it into a single string
        return "".join(res[::-1])
