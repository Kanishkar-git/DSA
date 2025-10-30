class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        string="".join(map(str,nums))
        split=string.split("0")
        max_length=0
        for i in split:
            if len(i)>max_length:
                max_length=len(i)
        return max_length
        