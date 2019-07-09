import time
import threading

class myThread(threading.Thread):
    def cal_square(numbers):
        print("Claculating square number")
    for n in numbers:
        threadLock.acquire()
        time.sleep(0.2)
        print('square:\n',n*n )
        threadLock.release()

    def cal_cube(numbers):
        print("Calculate cube of number")
    for n in numbers:
        threadLock.acquire()
        time.sleep(0.2)
        print('cube:\n',n*n*n)
        threadLock.release()
        
arr = [2,3,8,9]

t = time.time()

threadLock=threading.Lock()

t1= threading.Thread(target=cal_square,  args=(arr,))
t2= threading.Thread(target=cal_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in ",time.time()-t)
