class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num=int("".join(map(str,digits)))
        num+=1
        b=[]
        while num>0:
            b.append(num%10)
            num=num//10
        b.reverse()
        return b

        