class Solution:
    def romanToInt(self, s: str) -> int:
        roman = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 }
        size = len(s)
        number = 0
        for i in range(size):
            if i + 1 < size and roman[s[i]] < roman[s[i + 1]]:
                number -= roman[s[i]]
            else:
                number += roman[s[i]]
        return number