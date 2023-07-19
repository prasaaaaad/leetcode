class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            # j will start after i beacuse we can't use same number twice
            for j in range(i+1, size):
                if nums[i] + nums[j] == target:
                    return [i, j]
