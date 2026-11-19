class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Sliding window problem
        charSet = set()
        l=0
        result = 0

        for i in range(len(s)):
            while (s[i] in charSet):
                charSet.remove(s[l])
                l+=1
            charSet.add(s[i])
            result = max(result, i-l+1)
        return result