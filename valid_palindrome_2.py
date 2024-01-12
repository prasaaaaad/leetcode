# leetcode 125


class Solution:
    def isPalindrome(self, str: str) -> bool:
        s = ""
        for c in str:
            if c.isalnum():
                s += c

        s = s.lower()
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
