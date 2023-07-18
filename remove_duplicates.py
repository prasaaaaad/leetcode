class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0 # this keeps tracks of unique numbers
        for i in range(len(nums)):
            if nums[i] > nums[k]:
                k += 1
                nums[k], nums[i] = nums[i], nums[k]
        return k + 1
