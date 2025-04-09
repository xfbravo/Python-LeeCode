# class Solution:
#     def generateParenthesis(self, n: int) -> list[str]:
#         result = []
#         if n == 0:
#             return result
#         elif n == 1:
#             result.append("()")
#             return result
#         for item in self.generateParenthesis(n - 1):
#             if "(" + item + ")" not in result:
#                 result.append("(" + item + ")")
#             if item + "()" not in result:
#                 result.append(item + "()")
#             if "()" + item not in result:
#                 result.append("()" + item)
#         result.sort()
#         return result
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def backtrack(s,left,right):
            if len(s)==2*n:
                result.append(s)
                return
            if left<n:
                backtrack(s+'(',left+1,right)
            if right<left:
                backtrack(s+')',left,right+1)
        result = []
        backtrack("",0,0)
        return result


solution = Solution()
print(solution.generateParenthesis(4))
print("(())(())" in solution.generateParenthesis(4))  # True
