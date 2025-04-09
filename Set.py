# s={1,2,3}
# print(s)
# s.add("Hello")
# print(s)
# s.pop()
# print(s)
# if "Hello" in s:
#     s.remove("Hello")
# print(s)
# s.clear()
# print(s)
# s={1,2,3}
# s2={3,4,5}
# print(s | s2)
# print(s & s2)
# print(s - s2)
set1Num=input("Enter the number of elements in set1: ")
set1=set()
input_str=input("Enter the elements in set1: ")
input_lst=input_str.split()
for i in range(int(set1Num)):
    set1.add(int(input_lst[i]))
set2Num=input("Enter the number of elements in set2: ")
set2=set()
input_str=input("Enter the elements in set2: ")
input_lst=input_str.split()
for i in range(int(set2Num)):
    set1.add(int(input_lst[i]))
listSum=list(set1 | set2)
print(listSum)