class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        # this loop will run till end of the first word in list
        for i in range(len(strs[0])):
            for word in strs:
                if i == len(word) or word[i] != strs[0][i]:
                    return prefix
            prefix += strs[0][i]
        return prefix
        