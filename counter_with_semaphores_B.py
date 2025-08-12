# Problem 3 (B)
import threading

GREEN = "\033[92m"
RESET = "\033[0m"

counter = 10
R0_A = 0
R0_B = 0

s = threading.Semaphore(0)

def process_A():
    global R0_A
    R0_A = counter
    R0_A += 1
    s.acquire() # Wait

def process_B():
    global counter, R0_B
    R0_B = counter
    R0_B += 2
    counter = R0_B
    s.release() # Signal

if __name__ == "__main__":
    counter = 10
    tA = threading.Thread(target=process_A)
    tB = threading.Thread(target=process_B)

    tA.start()
    tB.start()

    tA.join()
    tB.join()

    print(GREEN + f"Final value of counter = {counter}" + RESET)