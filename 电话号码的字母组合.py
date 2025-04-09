class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []
        combinations=['']
        for i in range(len(digits)):
            combinations=Solution.addCombination(combinations,digits[i])
        return combinations
    @staticmethod
    def addCombination(lst:list[str],char:str):
        newlst=[]

        if char == '2':
            for item in lst:
                newlst.append(item + 'a')
                newlst.append(item + 'b')
                newlst.append(item + 'c')
        elif char == '3':
            for item in lst:
                newlst.append(item + 'd')
                newlst.append(item + 'e')
                newlst.append(item + 'f')
        elif char == '4':
            for item in lst:
                newlst.append(item + 'g')
                newlst.append(item + 'h')
                newlst.append(item + 'i')
        elif char == '5':
            for item in lst:
                newlst.append(item + 'j')
                newlst.append(item + 'k')
                newlst.append(item + 'l')
        elif char == '6':
            for item in lst:
                newlst.append(item + 'm')
                newlst.append(item + 'n')
                newlst.append(item + 'o')
        elif char == '7':
            for item in lst:
                newlst.append(item + 'p')
                newlst.append(item + 'q')
                newlst.append(item + 'r')
                newlst.append(item + 's')
        elif char == '8':
            for item in lst:
                newlst.append(item + 't')
                newlst.append(item + 'u')
                newlst.append(item + 'v')
        else:
            for item in lst:
                newlst.append(item + 'w')
                newlst.append(item + 'x')
                newlst.append(item + 'y')
                newlst.append(item + 'z')
        return newlst

solution = Solution()
print(solution.letterCombinations('23'))