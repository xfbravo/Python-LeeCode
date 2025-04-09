import time
import threading
def sing():
    print("singing")
    time.sleep(1)
    print("stop singing")
    time.sleep(1)

def dance():
    print("dancing")
    time.sleep(1)
    print("stop dancing")
    time.sleep(1)
t1=threading.Thread(target=sing)
t2=threading.Thread(target=dance)
t1.start()
t2.start()