name='  Sher l o ck Ho mes  '
print(id(name))
name='  Jack Sparrow  '
print(id(name))
print(name.upper())
print(name.strip())
print(name.replace(' ',''))
lst=name.split(' ')
print('_'.join(lst))
name=['张三','李四','王五']
print('_'.join(name))
for i in range(len(name)):
    itemName=name[i]
    if itemName.startswith('张'):
        newItemName=itemName.replace('张','熊')
        name[i]=newItemName
print(name)
name.pop(2)
print(name)
name.append('老六')
print(name)
name.insert(1,'老七')
print(name)
name.extend(['老八','老九'])
print(name)
age=input("请输入你的年龄：")
while True:
    if(age.isdigit()):
        age=int(age)
        if age<18:
            print("你还未成年")
        else :
            print("你已经成年")
        break
    else:
        age=input("请输入有效数字：")
        continue