import threading
from asyncio import timeout
from time import sleep
from multiProcess import Queue
from queue import Empty as queueEmpty
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

lock=threading.Lock()

list1=[0]*10

def task1():
    for i in range(len(list1)):
        list1[i]=i
        sleep(0.2)

def task2():
    for i in range(len(list1)):
        print("----->",list1[i])
        sleep(0.2)

if __name__=="__main__":
    th1=threading.Thread(target=task1)
    th2=threading.Thread(target=task2)
    th2.start()
    th1.start()
    # th1.join()
    # th2.join()
    print("All tasks completed.")