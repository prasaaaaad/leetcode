class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        size = len(s)
        i, length = size - 1, 0
        while s[i] == ' ':
            i -= 1
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1
        return length