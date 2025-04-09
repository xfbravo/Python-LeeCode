class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1 or numRows>=len(s):
            return s
        lst=[[] for _ in range(numRows)]
        goDown=True
        currentLine=0
        for i in range(len(s)):
            lst[currentLine].append(s[i])
            if currentLine==0:
                goDown=True
            elif currentLine==numRows-1:
                goDown=False
            if goDown:
                currentLine+=1
            else:
                currentLine-=1

        result=''
        for i in range(numRows):
            for elem in lst[i]:
                result+=elem
        return result

solution=Solution()
print(solution.convert("PAYPALISHIRING",3)) # PAHNAPLSIIGYIR