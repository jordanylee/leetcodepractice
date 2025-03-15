# raymond t84 m88
class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        start = 1
        end = max(piles)

        while(start < end):
            # print("start: {}, end: {}".format(start, end))
            mid = (start + end) // 2
            # print(mid)

            hours_spent = 0
            for pile in piles:
                hours_spent += (pile + mid - 1) // mid
            # print(hours_spent)

            # binary search condition
            if hours_spent > h:
                start = mid + 1
            else:
                end = mid

        return start
    
