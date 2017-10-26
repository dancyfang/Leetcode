class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        m = 0
        for i,c in enumerate(s):
            r = 1
            while i+r < len(s) and s[i+r] not in s[i:i+r]:
                r += 1
            if r>m:
                m = r
        return m

a = Solution()
print a.lengthOfLongestSubstring('pwwkew')
