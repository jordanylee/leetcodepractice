# jordan 27.66 55.32

class Solution(object):
    def averageValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sum = 0
        count = 0
        for num in nums:
            if (num & 1) == 0 and (num % 3) == 0:
                sum += num
                count += 1
        
        if sum == 0:
            return sum
        return (sum / count)