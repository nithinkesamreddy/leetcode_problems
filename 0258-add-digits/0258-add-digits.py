class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num>=10:
            sum=0
            for i in range(len(str(num))):
                a=num%10
                sum+=a
                num=num//10
            num=sum
        return num

        