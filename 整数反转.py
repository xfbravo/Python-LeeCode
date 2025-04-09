class Solution:
    def reverse(self, x: int) -> int:
        flag=1
        if x>0:
            s=str(x)
            flag=1
        elif x<0:
            s=str(-x)
            flag=-1
        else:
            return 0
        s=list(s)
        s.reverse()
        s=''.join(s)
        s=int(s)
        s*=flag
        if s>2**31-1 or s<-2**31:
            return 0
        return s
solution=Solution()
print(solution.reverse(120)) # 321