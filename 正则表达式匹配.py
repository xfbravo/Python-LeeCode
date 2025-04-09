import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        res=re.match(p,s)
        if not res:
            return False
        else:
            if res.group()==s:
                return True
            else:
                return False
solution=Solution()
print(solution.isMatch("ab",".*"))