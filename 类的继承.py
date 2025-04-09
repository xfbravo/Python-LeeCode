#类的继承
class Person:
    ID='123456'
    def __init__(self,name,age):
        print('Person类的构造函数被调用了')
        self._name=name
        self._age=age
    def __del__(self):
        print(f"对象{self._name}被删除了")
    def __str__(self):
        return f'姓名：{self._name}, 年龄：{self._age}'

    def greet(self):
        print(f'你好，我是{self._name}，我{self._age}岁了')

class Student(Person):
    def greet(self):
        print(f'你好，我是{self._name}，我{self._age}岁了，我是一个学生')

class CStudent(Student):
    def greet(self):
        super().greet()
        print(f'而且我是一个计算机专业的大学生')

    def get_name(self):
        return self._name
p1=Person('张三', 30)
p2=Student('李四', 20)
p3=CStudent('王五', 25)
p1.greet()
p2.greet()
p3.greet()
