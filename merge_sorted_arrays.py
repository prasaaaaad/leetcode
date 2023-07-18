class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last = m + n - 1
        p = m - 1
        q = n - 1

        while p >= 0 and q >= 0:
            if nums1[p] > nums2[q]:
                nums1[last] = nums1[p]
                p -= 1
            else:
                nums1[last] = nums2[q]
                q -= 1
            last -= 1
        # move the leftovers from list 2 to list 1
        while q >= 0:
            nums1[last] = nums2[q]
            q, last = q - 1, last - 1
