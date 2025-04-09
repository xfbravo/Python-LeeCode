# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         #判断是否是回文字符串
#         return s == s[::-1]
#     def longestPalindrome(self, s: str) -> str:
#         lst=[]
#         length=len(lst)
#         if len(s) < 2:
#             return s
#         elif len(s)==2:
#             if s[0]==s[1]:
#                 return s
#             else:
#                 return s[0]
#         for i in range(len(s)):
#             if i+length>len(s):
#                 break
#             else:
#                 for j in range(i+length,len(s)):
#                     if s[j]!= s[i]:
#                         continue
#                     else:
#                         if self.isPalindrome(s[i:j+1]) and len(s[i:j+1])>len(lst):
#                             lst= s[i:j+1]
#                             length=len(lst)
#         return lst
class Solution:
    def expandAroundCenter(self,s:str,left:int,right:int):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        return left+1,right-1
    def longestPalindrome(self,s:str)->str:
        start,end=0,0
        for i in range(len(s)):
            left1,right1=self.expandAroundCenter(s,i,i)
            left2,right2=self.expandAroundCenter(s,i,i+1)
            if right1-left1>end-start:
                start,end=left1,right1
            if right2-left2>end-start:
                start,end=left2,right2
        return s[start:end+1]
solution = Solution()
print(solution.longestPalindrome("ccc")) # bab