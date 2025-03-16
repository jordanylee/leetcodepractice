# jordan 6 8 

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        return self.searc(piles, h)

    def finishesEating(self, piles, speed, guard_hours):
        sum_hours = 0
        for pile in piles:
            sum_hours += (ceil(float(pile) / float(speed)))
        return (sum_hours <= guard_hours)

    def searc(self, piles, guard_hours):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(1, max(piles), piles, guard_hours)

    def binarySearch(self, lower, upper, piles, guard_hours):
        print(lower, upper)
        
        midpoint = ((upper + lower) // 2)
        if lower == upper:
            return lower
        if self.finishesEating(piles, midpoint, guard_hours):
            return self.binarySearch(lower, midpoint, piles, guard_hours)
        else:
            return self.binarySearch((midpoint + 1), upper, piles, guard_hours)
        
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
    
