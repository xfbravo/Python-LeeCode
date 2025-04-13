def printList(param: list)->None:
    print(f'param:{param}')


def fun1(param:list)->None:
    print("fun1 running")
    param.pop()
    printList(param)
def fun2(param:list)->None:
    print("fun2 running")
    param.append('c')
    printList(param)
def fun3(param:list)->None:
    print("fun3 running")
    printList(param)
lst=['a','b']
fun1(lst)
fun2(lst)
fun3(lst)