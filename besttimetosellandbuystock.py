# jordna  54 47

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        max_profit = 0
        prices_size = len(prices)
        
        if prices_size <= 1:
            return 0

        left = 0
        right = 1
        while(True):
            if right == prices_size:
                return max_profit

            if prices[right] < prices[left]:
                left = right
                right += 1
                continue

            if (prices[right] - prices[left]) > max_profit:
                max_profit = prices[right] - prices[left]
                
            right += 1

# raymond 50 11
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        left = right = prices[0]

        for i in range(1, len(prices)):
            right = prices[i]
            if right > left:
                max_profit = max(max_profit, right - left)
            else:
                left = prices[i]

        return max_profit