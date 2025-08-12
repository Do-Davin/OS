# Problem 3 (C)
import threading

GREEN = "\033[92m"
RESET = "\033[0m"

counter = 10
mutex = threading.Semaphore(1)  

def process_A():
    global counter
    mutex.acquire()  
    R0_A = counter
    R0_A += 1
    counter = R0_A
    mutex.release()  

def process_B():
    global counter
    mutex.acquire()  
    R0_B = counter
    R0_B += 2
    counter = R0_B
    mutex.release()  

if __name__ == "__main__":
    counter = 10

    tA = threading.Thread(target=process_A)
    tB = threading.Thread(target=process_B)

    tA.start()
    tB.start()

    tA.join()
    tB.join()

    print(GREEN + f"Final value of counter = {counter}" + RESET)