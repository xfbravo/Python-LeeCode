class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        sameStart=[]
        for j in range(len(strs[0])):
            i=1
            for i in range(1,len(strs)):
                if j>len(strs[i])-1 or strs[i][j]!=strs[i-1][j]:
                    return ''.join(sameStart)
            else: sameStart.append(strs[0][j])
        return ''.join(sameStart)
solution=Solution()
lst=['Flower','Flow','Fly']
print(solution.longestCommonPrefix(lst))