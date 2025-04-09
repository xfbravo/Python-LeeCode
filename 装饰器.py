# lst=[]
# # Decorators
# #开挂日志
# def superPower(game):
#     def getPower():
#         lst.append(f'玩{game()}时开启了外挂')
#         lst.append(f"正在玩{game()}")
#         lst.append(f"玩{game()}后关闭了外挂")
#     return getPower
#
# @superPower
# def play_lol():
#     return "英雄联盟"
# @superPower
# def play_blackMithWuKong():
#     return "黑神话悟空"
# play_lol()
# play_blackMithWuKong()
# play_blackMithWuKong()
# play_lol()
#
# for item in lst:
#     print(item)
#通过装饰器完善开挂玩游戏系统，玩每个游戏前都开一个挂，并且记录打游戏的顺序
# lst=[]
# count=0
# UserName="2102356261"
# Password="dengni0425"
# def wrapper(game):
#     def inner(*args,**kwargs):
#         print("玩游戏前先开一个小挂")
#         ret=game(*args,**kwargs)
#         print("玩游戏后把挂关掉")
#         return ret
#     return inner
#
# @wrapper
# def play_LOL(username,passward,hero):
#     print("玩LOL咯")
#     print(f"这次我要玩{hero}")
# @wrapper
# def play_DNF(username,passward):
#     print("玩DNF咯")
#
# while True:
#     game = input("1. 玩LOL\n2. 玩DNF\n!.  不玩了\n请输入你要玩的游戏:")
#     if game=="1":
#         print("请输入你的LOL账号")
#         while True:
#             username=input()
#             if username==UserName:
#                 break
#             else:
#                 print("账号错误,请重新输入")
#         print("请输入你的LOL密码")
#         while True:
#             password=input()
#             if password==Password:
#                 break
#             else:
#                 print("密码错误,请重新输入")
#         hero=input("请输入你要玩的LOL英雄:")
#         play_LOL(username,password,hero=hero)
#         count+=1
#         lst.append(f'{count}. 玩LOL,选择了{hero}')
#     elif game=="2":
#         print("请输入你的DNF账号")
#         while True:
#             username = input()
#             if username == UserName:
#                 break
#             else:
#                 print("账号错误,请重新输入")
#         print("请输入你的DNF密码")
#         while True:
#             password = input()
#             if password == Password:
#                 break
#             else:
#                 print("密码错误,请重新输入")
#         play_DNF(username,password)
#         count+=1
#         lst.append(f'{count}. 玩DNF')
#     elif game=="!":
#         print("不想玩了，退出...")
#         break
#     else: print("输入错误,没有这个游戏,请重新输入")
#
# print("今天的游戏日志:")
# if len(lst)>0:
#     for item in lst:
#         print(item)
# else:
#     print("今天没有玩游戏")


#TODO通过装饰器进一步完善开挂玩游戏系统，玩每个游戏前都开一个挂，并且记录打游戏的顺序
lstGamePlayed=[]
count=0
verified=False
UserName="2102356261"
PassWord="dengni0425"

def login_verify(game):
    def wrapper(*args,**kwargs):
        global verified

        if not verified:#如果没有登录
            print("请输入用户名")
            while True:
                username=input()
                if username==UserName:
                    break
                else:
                    print("账号错误,请重新输入")
            print("请输入密码")
            while True:
                password=input()
                if password==PassWord:
                    verified=True
                    break
                else:
                    print("密码错误,请重新输入")
            print("登录成功")
        ret = game(*args,**kwargs)
        return ret
    return wrapper

def update_game_log(game):
    def wrapper(*args,**kwargs):
        ret = game(*args,**kwargs)
        global count
        count+=1
        lstGamePlayed.append(f'{count}. 玩{ret} {kwargs["hero"] if "hero" in kwargs else ""}')
        return ret
    return wrapper

@login_verify
@update_game_log
def play_LOL(**hero):
    print("玩LOL咯")
    return "LOL"

@login_verify
@update_game_log
def play_DNF():
    print("玩DNF咯")
    return "DNF"

while True:
    game=input("1.  LOL\n2.  DNF\n0.  退出\n请输入你要玩什么游戏:")

    if game=="1":
        hero = input("请输入你想玩的LOL英雄，登录成功后就可以畅玩了：")
        kwargs = {"hero": hero}
        play_LOL(**kwargs)
    elif game=="2":
        play_DNF()
    elif game=="0":
        print("不玩游戏了，退出...")
        break
    else:
        print("输入错误,没有这个游戏,请重新输入")

print("今天的游戏日志:")
if len(lstGamePlayed)>0:
    for item in lstGamePlayed:
        print(item)
else:
    print("今天没有玩游戏")

#TODO函数的参数

#
# def func1(a,b,c=0,d=0):
#     print(f'a={a},b={b},c={c},d={d}')
# func1(9,9,3,4)
# def func2(*information,**kwargs):
#     for item in information:
#         print(item)
#     for k,v in kwargs.items():
#         print(f'{k}={v}')
# information=('2102356261','dengni0425')
# func2(*information)
# kwargs={'name':'jack','age':30}
# func2(**kwargs)