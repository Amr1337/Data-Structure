import threading
import time

def calc_sqr(numbers):
    print("Calculate the square number: ")
    for n in numbers:
        time.sleep(0.2)
        print("Square number: ", n*n)

def calc_cube(numbers):
    print("Calculate the cubic number: ")
    for n in numbers:
        time.sleep(0.2)
        print("Cube: ",n*n*n)

arr = [2,4,5,7]
#print(calc_sqr(arr))
#print(calc_cube(arr))

t= time.time()

t1 = threading.Thread(target=calc_sqr, args=(arr,))
t2 = threading.Thread(target=calc_cube, args=(arr,))

t1.start()
t2.start()

t1.join()
t2.join()

print("it took to run this code: ", time.time()-t)
