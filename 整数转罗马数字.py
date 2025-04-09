class Solution:
    def intToRoman(self, num: int) -> str:
        result=''
        thou,hundred,tens,ones=(0,0,0,0)
        while num>0:
            if num>=1000:
                thou=num//1000
                num=num%1000
            if num>=100:
                hundred=num//100
                num=num%100
            if num>=10:
                tens=num//10
                num=num%10
            if num>=1:
                ones=num
                num=0
        if thou>0:
            result+='M'*thou
        if hundred>0:
            if hundred==9:
                result+='CM'
            elif hundred>=5:
                result+='D'+'C'*(hundred-5)
            elif hundred==4:
                result+='CD'
            else:
                result+='C'*hundred
        if tens>0:
            if tens==9:
                result+='XC'
            elif tens>=5:
                result+='L'+'X'*(tens-5)
            elif tens==4:
                result+='XL'
            else:
                result+='X'*tens
        if ones>0:
            if ones==9:
                result+='IX'
            elif ones>=5:
                result+='V'+'I'*(ones-5)
            elif ones==4:
                result+='IV'
            else:
                result+='I'*ones
        return result
solution=Solution()
print(solution.intToRoman(1994))