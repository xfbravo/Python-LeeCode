# Function to calculate the result of a mathematical expression
# def Calculate(num1,op,num2):
#     if op == '+':return num1+num2
#     if op == '-':return num1-num2
#     if op == '*':return num1*num2
#     if op == '/':return num1/num2
#     if op == '//':return num1//num2
#     if op == '%':return num1%num2
#     if op == '**':return num1**num2
# expression=input("Enter the expression: ")
# lst=expression.split()
# num1=int(lst[0])
# op=lst[1]
# num2=int(lst[2])
# tpl=Calculate(num1,op,num2)
# print("The result is:",tpl)
# 递归函数 fibonacci
# def Fibonacci(n):
#     if n==1:return 1
#     if n==2:return 1
#     return Fibonacci(n-1)+Fibonacci(n-2)
# n=int(input("Enter the index of Fibonacci: "))
# print(Fibonacci(n))
# def func(n):
#     def func2():
#         return n#返回func中n的值
#     return func2#返回一个函数,实际上是返回了func2的内存地址
#
# print(func(5)())
# a=10
# def func():
#     global a#声明a为全局变量
#     a+=1
# func()
# print(a)
# a=5
# def func1():
#     a=10
#     def func2():
#         def func3():
#             nonlocal a
#             a=50
#         func3()#在func2中调用func3
#     func2()#在func1中调用func2
#     print(a)#输出func1中的a=10
# func1()
# print(a)#输出global a=5
#lambda表达式
# def func(x):
#     return x**2
# print(func(5))
#
# lst=[item**2 for item in range(10) if item%2==0]
# print(lst)
# lst=[(lambda x:x**2)(item) for item in range(10) if item%2==0]
# print(lst)
# lst1=['a','b','c','d','e']
# lst2=[item.upper() for item in lst1]
# print(lst1)
# print(lst2)
# lst=[1,2,3,4,5]
# lst1=[(lambda i: i**2-i)(i) for i in lst]
# print(lst1)

# lst=[3,6,1,7,5,9,8,4,2]
# lst.sort()
# print(lst)
# lst1=sorted(lst)
# print(lst1)
# lst2=sorted(lst,reverse=True)
# print(lst2)

lst=['xf','wyx','jack','bob','sherlock']
def func(x):
    return len(x)
lst1=sorted(lst,key=func)
print(lst1)
lst2=sorted(lst,key=lambda x:len(x))
print(lst2)
lst3=filter(lambda x:x.startswith('x') ,lst)
print(lst3)
print(list(lst3))
lst4=[item.upper() for item in lst2]
print(lst4)
lst5=map(lambda s: s.upper() ,lst2)
print(lst5)
print(list(lst5))
