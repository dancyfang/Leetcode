class Solution(object):
    def utils(self, s, i):
        """
        :type s: str
        :rtype: str
        """
        r = ""
        while i < len(s) and s[i] != ']':
        	if not s[i].isdigit():
        		r += s[i]
        		i += 1
        	else:
        		n = 0
        		while s[i].isdigit():
        			n = 10 * n + int(s[i])
        			i += 1
        		i += 1
        		rsub, i = self.utils(s, i)
        		r += rsub * n
        return r,i+1

    def decodeString(self, s):
    	r,i = self.utils(s, 0)
    	return r

s = Solution().decodeString('100[leetcode]')
print(s)        