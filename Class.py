#%%
class Person:
    @classmethod
    def sleep(cls):
        print("人类需要睡觉")

    @staticmethod
    def eat():
        print("人类需要吃饭")
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"姓名: {self.name}, 年龄: {self.age}"
    def __del__(self):
        print(f"对象{self.name}被删除了")

    def greet(self):
        print(f"你好, 我是{self.name}, 我{self.age}岁了")
# 创建类的实例
person = Person("张三", 30)
person.greet()
print(person.name)
#%%
print(person)
Person.eat()
Person.sleep()
person.eat()
person.sleep()

# %%
if __name__ == "__main__":
    # 创建对象
    person1 = Person("Alice", 25)
    person2 = Person("Bob", 30)

    # 调用实例方法
    person1.greet()
    person2.greet()

    # 调用类方法和静态方法
    Person.sleep()
    Person.eat()

    # 删除对象
    del person1
    del person2