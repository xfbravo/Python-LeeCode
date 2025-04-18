# import threading
# from asyncio import timeout
# from time import sleep
# from multiProcess import Queue
# from queue import Empty as queueEmpty
# count=0
# def task1():
#     global count
#     for i in range(1000000):
#         count+=1
# def task2():
#     global count
#     for i in range(1000000):
#         count+=1
#
# th1=threading.Thread(target=task1)
# th2=threading.Thread(target=task2)
# th1.start()
# th2.start()
# th1.join()
# th2.join()
# print(count)

# lst=['movie1','movie2','movie3','movie4','movie5']
# downloaded_lst=Queue(5)
# def download_movie(movie_lst):
#     for movie in movie_lst:
#         print(f"Downloading {movie}...")
#         sleep(0.5) # Simulate a download delay
#         downloaded_lst.put(movie)
#         print(f"{movie} downloaded.")
#
# def get_movie(downloaded_lst):
#     while True:
#         try:
#             movie=downloaded_lst.get(timeout=2)
#             print(f"Getting {movie}...")
#             sleep(0.5) # Simulate a get delay
#             print(f"{movie} got.")
#         except:
#             print("All movies got.")
#             break
#
#
# download=threading.Thread(target=download_movie,args=(lst,))
# get=threading.Thread(target=get_movie,args=(downloaded_lst,))
# download.start()
# get.start()
# download.join()
# get.join()
# print("All movies downloaded and got.")

# lock=threading.Lock()
#
# list1=[0]*10
#
# def task1():
#     for i in range(len(list1)):
#         list1[i]=i
#         sleep(0.2)
#
# def task2():
#     for i in range(len(list1)):
#         print("----->",list1[i])
#         sleep(0.2)
#
# if __name__=="__main__":
#     th1=threading.Thread(target=task1)
#     th2=threading.Thread(target=task2)
#     th2.start()
#     th1.start()
#     # th1.join()
#     # th2.join()
#     print("All tasks completed.")

from threading import Thread,Lock
import time
# lock1=Lock()
# lock2=Lock()
#
# class MyThread1(Thread):
#     def run(self):
#         if lock1.acquire():
#             print(self.name+"获得了lock1")
#             time.sleep(0.1)
#             if lock2.acquire(timeout=2):
#                 print(self.name+"又获得了lock2")
#                 time.sleep(0.1)
#                 lock2.release()
#             lock1.release()
#
# class MyThread2(Thread):
#     def run(self):
#         if lock2.acquire():
#             print(self.name+"获得了lock2")
#             time.sleep(0.1)
#             if lock1.acquire(timeout=2):
#                 print(self.name+"又获得了lock1")
#                 time.sleep(0.1)
#                 lock2.release()
#             lock1.release()
#
# if __name__ == '__main__':
#     th1 = MyThread1()
#     th2 = MyThread2()
#     th1.start()
#     th2.start()

# import threading
# import time
# import greenlet
# import gevent
# from gevent import monkey
#
# monkey.patch_all()
#
# def a():
#     for i in range(5):
#         print("A",i)
#         time.sleep(0.1)
# def b():
#     for i in range(5):
#         print("B",i)
#         time.sleep(0.1)
#
# def c():
#     for i in range(5):
#         print("C", i)
#         time.sleep(0.1)
#
# if __name__ == '__main__':
#     g1=gevent.spawn(a)
#     g2=gevent.spawn(b)
#     g3=gevent.spawn(c)
#     g1.join()
#     g2.join()
#     g3.join()
import gevent
from gevent import monkey
import requests
monkey.patch_all()

def download(url):
    response=requests.get(url)
    content=response.text
    print("下载了{}的数据，长度为{}".format(url,len(content)))

if __name__ == '__main__':
    urls=['http://www.baidu.com','http://www.163.com']
    g=[]
    for i, url in enumerate(urls):
        g.append(gevent.spawn(download,url))
    gevent.joinall(g)
