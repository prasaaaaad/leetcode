class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        size = len(nums)
        visited = []
        for i in range(size):
            current = nums[i]
            if current in visited:
                continue
            else:
                visited.append(current)
            count = 0
            for j in range(size):
                if nums[j] == current:
                    count += 1
            if count > (size // 2):
                return current