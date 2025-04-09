dic=dict()
dic['a']=1
dic['b']=2
dic['c']=3
print(dic)
print(dic['a'])
for key,value in dic.items():
    print(key , value)
dic={
    'a':1,
    'b':2,
    'c':3,
    'assistant':{
        'name':'jack',
        'age':30,
        'address':'beijing'
    }
}
print(dic['assistant']['name'])