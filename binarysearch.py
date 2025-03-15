#jrodan 100 63.81
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        return self.binarySearch(nums, target, 0, (len(nums) - 1))

    def binarySearch(self, nums, target, lower, upper):
        if lower > upper:
            return -1
        midpoint_index = ((upper + lower) // 2)
        midpointNum = nums[midpoint_index]
        if midpointNum == target:
            return midpoint_index
        if midpointNum > target:
            return self.binarySearch(nums, target, lower, (midpoint_index - 1))
        else:
            return self.binarySearch(nums, target, (midpoint_index + 1), upper)

# raymond t100 m63
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1

        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] == target:
                return mid
            else:
                end = mid - 1

        return -1