class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size    # k can be greater than the length
        # in-place reversal to minimize the space
        self.reverse(nums, 0, size - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, size - 1)
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
