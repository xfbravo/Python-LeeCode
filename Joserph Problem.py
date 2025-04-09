from os import remove
#约瑟夫问题
num=int(input('please enter the number of Person: '))
start=int(input('please enter the start position of your list: '))
gap=int(input('please enter the gap between two actions: '))
lst=[]
for i in range(num):
    lst.append(i+1)
index=start#当前位置
count=0#计数器
while count<num-1:#删除的人数应该比总人数少1
    temp=lst[index]#记录本次删除的人的位置
    lst.remove(temp)#删除本次删除的人
    #应该先删除（这样就可以更新len(lst))再更新index，不然可能会出现index超出范围的情况
    index=(index+gap-1)%(len(lst))#更新当前位置（本应该是index+gap，但是由于删除了一个人，所以要减1）
    print(temp,end=' ')#输出本次删除的人
    count+=1#计数器加1
print(lst[0])#输出最后一个人