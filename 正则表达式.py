import re

# class Solution:
#     def myAtoi(self, s: str) -> int:
#         s=s.strip()
#         r=re.match(r'^\s*([+-]?\d+)', s)
#         result= int(r.group(1)) if r else 0
#         if result>2**31-1:
#             return 2**31-1
#         elif result<-2**31:
#             return -2**31
#         else:
#             return result
# solution=Solution()
# print(solution.myAtoi("+1002"))
# res=re.match(r"^\s*([+-]?\d+)","  123456")
# print(res.group(1))
res =re.match(r"<(\w+)><(\w+)>(.*)?</\2></\1>","<html><body>login</body></html>")
print(res.group())

res=re.match(r"www\.(.*)?\.com","www.baidu.com")
print(res.group())

res=re.match(r"\d+@(qq|163|123|gmail)\.com","2102356261@qq.com")
print(res.group())

res=re.findall(r"\d+","123abc456def789")
print(res)

res=re.sub(r"wyx","吴怡欣","wyx, I love you")
print(res)

