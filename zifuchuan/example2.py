class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        lmind=len(s)

        for i in "qwertyuiopasdfghjklzxcvbnm":
            lnum=s.find(i)
            rnum=s.rfind(i)

            if lnum==rnum and lnum!=-1 and rnum!=-1:
                lmind=min(lmind,lnum)

        if lmind == len(s):
            return -1
        else:
            return lmind

s=Solution()
result=s.firstUniqChar("leetcode")
print result