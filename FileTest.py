# with open("../files/xf.txt",'r',encoding='utf-8') as f:
#     for line in f:
#         print(line.strip())
with open("../files/xf.txt", 'r', encoding='utf-8') as f1, \
     open("../files/wyx.txt", 'a', encoding='utf-8') as f2:
     for line in f1:
         f2.write(line.strip())
         f2.write("\n")


