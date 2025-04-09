class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for elem in s:
            if elem in ['(','[','{']:
                stack.append(elem)
            elif elem in [')',']','}']:
                if len(stack)==0:
                    return False
                if elem==')' and stack[-1]=='(':
                    stack.pop()
                elif elem==']' and stack[-1]=='[':
                    stack.pop()
                elif elem=='}' and stack[-1]=='{':
                    stack.pop()
                else:
                    return False
        if len(stack)!=0:
            return False
        return True
solution=Solution()
print(solution.isValid("()[]{")) # True