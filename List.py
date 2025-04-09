import copy
from copy import deepcopy
import requests
# lst=[1,2,3,4,5]
# print(lst)
# print(f'type(lst)={type(lst)}')
# #切片
# print(lst[::2])
# lst2=lst[::-1]
# print(lst2)
# lst.append(6)
# print(lst)
# lst.insert(0,0)
# print(lst)
# lst.pop(len(lst)-1)
# print(lst)
# lst.remove(4)
# print(lst)
# lst.extend([1,2,3])
# print(lst)
# lst.sort()
# print(lst)
# lst=['熊峰','吴怡欣','徐帆','李亮奇','程正阳','熊鑫']
# temp=[]
#
# for item in lst:
#     if item.startswith('熊'):
#         temp.append(item)
# for item in temp:
#     lst.remove(item)
# del temp
# print(lst)


#求循环节
# numerator = int(input("Enter the numerator: "))
# denominator = int(input("Enter the denominator: "))
# precision = int(input("Enter the precision: "))
# integerPart = numerator//denominator#整数部分
# if numerator>denominator:
#     numerator%=denominator#分子更新为小于分母的值
# decimal=list()#小数部分
# indexLoopStart=-1#循环节开始的位置
# while True:
#     if numerator*10//denominator not in decimal:#如果这个数不在小数部分中
#         decimal.append(numerator*10//denominator)#添加到小数部分
#     else:#如果这个数在小数部分中
#         indexLoopStart=decimal.index(numerator*10//denominator)#记录循环节开始的位置
#         break
#     numerator=numerator*10%denominator#更新分子
#     if numerator==0:#如果分子为0，说明可以整除，没有循环节，直接退出，indexLoopStart还是为-1
#         break
# print(integerPart,end='.')#输出整数部分,一定要输出
# #如果存在循环节
# loop=list()
# if indexLoopStart!=-1:
#     for i in range(indexLoopStart):
#         print(decimal[i],end='')#输出循环节之前的部分
#     loop=decimal[indexLoopStart:]
#     precision-=len(decimal[:indexLoopStart])
#     index=0
#     while precision>0:#如果还有精度，那么继续输出循环节
#         print(loop[index],end='')
#         index=(index+1)%len(loop)
#         precision-=1
# else:#如果不存在循环节，直接输出小数部分
#     for i in range(len(decimal)):
#         print(decimal[i],end='')
# print()
# print(f'ring={len(loop)}')
# for i in range(len(loop)):
#     print(loop[i],end='')

#list的拷贝
lst1=[1,2,3,[1,2,3],4,5]
lst2=lst1#引用
lst3=lst1.copy()#拷贝
lst4=deepcopy(lst1)#深拷贝
print(lst1,id(lst1))
print(lst2,id(lst2))
print(lst3,id(lst3))
print(lst4,id(lst4))
print(id(lst1[3]))
print(id(lst2[3]))
print(id(lst3[3]))
print(id(lst4[3]))