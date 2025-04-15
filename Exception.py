# def calculate(num1:float,num2:float,operator:str)->float:
#     try:
#         if operator == '+':
#             return num1 + num2
#         elif operator == '-':
#             return num1 - num2
#         elif operator == '*':
#             return num1 * num2
#         elif operator == '/':
#             return num1 / num2
#         else:
#             print("Invalid operator")
#         with open(r'../file/wyx.txt', 'r', encoding='utf-8') as f:
#             lines = f.readlines()
#             for line in lines:
#                 print(line.strip())
#         list1 = []
#         list1.pop()
#
#     except Exception as error:
#         print("An error occurred:", error)
#     finally:
#         print("Finished")
#
# res =calculate(2,3,'/')
# print(res)

def raise_exception():
    pwd=input("请输入六位数字密码: ")
    if len(pwd) != 6:
        raise ValueError("密码长度不正确")
    if not pwd.isdigit():
        raise TypeError("密码必须是数字")

try:
    raise_exception()
except ValueError as e:
    print("ValueError:", e)
except TypeError as e:
    print("TypeError:", e)
