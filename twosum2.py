#jordan

class Solution(object): 
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers) - 1

        while True:
            sum = numbers[start] + numbers[end]
            if sum == target:
                return [start + 1, end + 1]
            if sum > target:
                end -= 1
            else:
                start += 1

# raymond 
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        start = 0
        end = len(numbers)-1

        while(start < end):
            total = numbers[start] + numbers[end]
            if total > target:
                end -= 1
            elif total == target:
                return [start+1, end+1]
            else:
                start += 1
    
        # answer should be guaranteed
        return "something went wrong"