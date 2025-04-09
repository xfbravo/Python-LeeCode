import re
class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        r=re.match(r'^\s*([+-]?\d+)', s)
        result= int(r.group(1)) if r else 0
        if result>2**31-1:
            return 2**31-1
        elif result<-2**31:
            return -2**31
        else:
            return result
solution=Solution()
print(solution.myAtoi("+1002"))