def priority(op):
    """返回运算符的优先级"""
    if op =='(':
        return 0
    elif op in ('+', '-'):
        return 1
    elif op in ('*', '/'):
        return 2
    elif op == '^':
        return 3
    elif op==')':
        return 4
    return 0
def infix_to_postfix(expression):
    """将中缀表达式转换为后缀表达式"""
    stack=[]
    postfix=[]
    i=0
    while i < len(expression):
        if expression[i].isdigit():
            num=[]
            while i<len(expression) and expression[i].isdigit():
                num.append(expression[i])
                i+=1
            postfix.append(''.join(num))
            continue
        elif expression[i]=='(':
            stack.append(expression[i])
        elif expression[i]==')':
            while stack and stack[-1]!='(':
                postfix.append(stack.pop())
            stack.pop()
        elif expression[i] in('+', '-', '*', '/'):
            while stack and priority(stack[-1])>=priority(expression[i]):
                postfix.append(stack.pop())
            stack.append(expression[i])
        elif expression[i]=='^':
            while stack and priority(stack[-1])>priority(expression[i]):
                postfix.append(stack.pop())
            stack.append(expression[i])
        else:
            print("Invalid character:", expression[i])
            return None
        i+=1
    while stack:
        postfix.append(stack.pop())
    return postfix

def calculate_postfix(postfix):
    """计算后缀表达式的值"""
    stack = []
    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        else:
            num2=stack.pop()
            num1=stack.pop()
            if char=='+':
                stack.append(num1+num2)
            elif char=='-':
                stack.append(num1-num2)
            elif char=='*':
                stack.append(num1*num2)
            elif char=='/':
                if num2==0:
                    print("除数不能为0")
                    return None
                stack.append(num1/num2)
            elif char=='^':
                stack.append(num1**num2)
            else:print("Invalid operator:", char)
    return stack.pop()

n=int(input("请输入表达式的个数："))
for i in range(n):
    expression=input("请输入表达式：")
    expression=expression.strip()
    lst = infix_to_postfix(expression)
    if lst:
        print("后缀表达式:", ''.join(lst))
        result = calculate_postfix(lst)
        if result is not None:
            print("结果:", result)
        else:
            print("计算失败")
    else:
        print("转换失败")
