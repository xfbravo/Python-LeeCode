class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength=0
        if len(s)==0:
            return 0
        if len(s)==1:
            return 1
        for i in range(len(s)):
            subString=[]
            for j in range(i, len(s)):
                if s[j] not in subString:
                    subString.append(s[j])
                    if j-i+1>maxLength:
                        maxLength=j-i+1
                else:
                    if j-i> maxLength:
                        maxLength=j-i
                    break
            if maxLength>len(s)-i:
                break
        return maxLength
solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb")) # 3