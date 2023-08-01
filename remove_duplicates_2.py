class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left, right = 0, 0
        size = len(nums)
        while right < size:
            count = 1
            # incrtement the right till the end of the current streak
            while right + 1 < size and nums[right] == nums[right + 1]:
                right += 1
                count += 1
            # shift at the most two occurences of the current number to the left
            for i in range(min(2, count)):
                nums[left] = nums[right]
                left += 1
            # increment right by one for the next number
            right += 1
        return left
