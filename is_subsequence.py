class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        k = 0
        s_size, t_size = len(s), len(t)
        for i in range(t_size):
            if k < s_size and s[k] == t[i]:
                k += 1
        return True if k == len(s) else False
