import os
from multiprocessing import Process, Pool,Queue
from time import sleep, time
from random import random


# def tast1(s):
#     while True:
#         print("This is Task 1  ",os.getpid(),"--------->",os.getppid())
#         sleep(s)
#
# def tast2(s):
#     while True:
#         print("This is Task 2  ",os.getpid(),"--------->",os.getppid())
#         sleep(s)
#
# if __name__ == '__main__':
#     print(os.getpid())
#     p1 = Process(target=tast1,name="tast1",args=(1,))
#     p2 = Process(target=tast2,name="tast2",args=(2,))
#
#     p1.start()
#     print(p1.name)
#     p2.start()
#     print(p2.name)
#     p1.join()
#     p2.join()
#     print("-----------------------------")
#     print("Main process end")

#自定义进程
# class MyProcess(Process):
#     def __init__(self,name):
#         super(MyProcess,self).__init__()
#         self.name=name
#
#     def run(self):
#         n=1
#         while True:
#             print(f"{n}------>Process name:",self.name,end='\n')
#             n+=1
#
# if __name__ == '__main__':
#     p1=MyProcess("小明")
#     p1.start()
#     p2=MyProcess("小红")
#     p2.start()

# def task(task_name):
#     print("start task: ",task_name)
#     start = time()
#     sleep(random())
#     end = time()
#     print("end task:",task_name, " cost time:",end-start," pid:",os.getpid())
#     # return 'end task:{}!, cost time:{}, pid:{}'.format(task_name, end-start, os.getpid())
#
# taskProcess=[]
# def callback_func(n):
#     taskProcess.append(n)
#
# if __name__ == '__main__':
#     pool=Pool(5)
#     tasks = ['task1', 'task2', 'task3', 'task4', 'task5','task6','task7','task8','task9','task10']
#     for task1 in tasks:
#         pool.apply(task, args=(task1,))
#     pool.close()
#     pool.join()
#     # for i in taskProcess:
#     #     print(i)
#     print("all tasks done")

#进程间通信---->Queue
# q=Queue(5)
# for i in range(5):
#     q.put(i)
# if not q.full():
#     q.put(5)
# else:
#     print("Queue is full")
# while not q.empty():
#     print(q.get())
#
# lst=[]
# lst.insert(len(lst),1)
# lst.insert(len(lst),2)
# print(lst)

#进程间通信
def download(q):
    images=['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg']
    for img in images:
        print("downloading",img)
        sleep(0.5)
        q.put(img)

def getfile(q):
    while not q.empty():
        img=q.get()
        print("get file:",img)

if __name__ == '__main__':
    q=Queue(5)
    p1=Process(target=download,args=(q,))
    p2=Process(target=getfile,args=(q,))
    p1.start()
    p1.join()
    p2.start()
    p2.join()
    print("all tasks done")