class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            # j will start after i beacuse we can't use same number twice
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]