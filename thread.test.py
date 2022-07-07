from telnetlib import BRK
import threading
from threading import Thread

import time

stop_thread = False

def function1():
    for i in range(100):
        print(f"Num = {i}")
        time.sleep(0.05)

def function2():

        

    for i in range(100):
        if stop_thread == True:
            break
        print(f"Num 2 : {i}")
        time.sleep(1)



t1 = Thread(target=function1)
t2 = Thread(target=function2)

t1.start()
t2.start()

t1.join()

stop_thread = True