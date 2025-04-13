<<<<<<< HEAD
# with open("../files/wyx.txt", 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip())
#
# with open("../files/xf.txt", 'a', encoding='utf-8') as f:
#     f.write("hello world\n")
# with open("../files/乡村教师.txt",'r',encoding='utf-8') as file:
#     lines = file.readlines()
#     for line in lines:
#         print(line.strip())t
# try:
#     with open("../files/test.png",'rb') as file1,open("../files/test2.png",'wb') as file2:
#             while True:
#                 data=file1.read(1024)
#                 file2.write(data)
#                 if not data:
#                     break
# except FileNotFoundError:
#     print("File not found")
# except IOError:
#     print("IO Error")
# except Exception as e:
#     print("An error occurred:", str(e))
import json

my_dict={
    'name':'熊峰',
    'age':20,
    'school':'BIT',
    'hobby':['basketball','coding','reading'],
    'games':[
        {'name':'LOL','time':100},
        {'name':'DOTA','time':200},
        {'name':'CSGO','time':300}
    ]
}
print (my_dict)
p=json.dumps(my_dict)
print(json.loads(p))
# with open("../files/JSONTest.json",'w') as file:
#     json.dump(my_dict,file)
# with open("../files/JSONTest.json",'r') as file:
#     my_dict=json.load(file)
#     print(type(my_dict))
#     print(my_dict)
=======
with open("../files/wyx.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())

with open("../files/xf.txt", 'a', encoding='utf-8') as f:
    f.write("hello world\n")
>>>>>>> 8f3e4131dc0866e63fd0c6ee4252c99e81e9e116
