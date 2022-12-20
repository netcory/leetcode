class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = len(nums)
        for idx, number in enumerate(nums):
            if number == val:
                nums[idx] = 10000
                k -= 1
        nums.sort()
        return(k)