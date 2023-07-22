class Solution:
    def isPalindrome(self, s: str) -> bool:
        phrase = []
        for letter in s:
            if letter.isalnum():
                phrase.append(letter.lower())

        left, right = 0, len(phrase) - 1
        while left < right:
            if phrase[left] != phrase[right]:
                return False
            left += 1
            right -= 1
        return True
