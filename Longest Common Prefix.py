class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = strs[0]
        for str in strs:
            while not str.startswith(output):
                output = output[:-1]
        return output
