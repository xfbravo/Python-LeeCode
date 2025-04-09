class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        s=str(x)
        s=list(s)
        s.reverse()
        s=''.join(s)
        return s==str(x)
solution=Solution()
print(solution.isPalindrome(121)) # True