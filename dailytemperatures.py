#jordan  63.77 75.69

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        days_to_wait = [0] * len(temperatures)
        stack = list()

        for index, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][1]:
                orig_index = stack[-1][0]
                days_to_wait[orig_index] = index - orig_index 
                del stack[-1]
                
            stack.append((index, temperature))
        
        return days_to_wait
    
# raymond t43 m23
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                index = stack[-1][0]
                res[index] = i - index
                del stack[-1]
            stack.append((i, temperatures[i]))

        return res