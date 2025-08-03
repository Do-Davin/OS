import threading
import time
import random
from collections import deque
import logging

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler("producer_consumer.log"),
        logging.StreamHandler()
    ]
)

# Shared buffer
buffer = deque(maxlen=100)

# Semaphores
space = threading.Semaphore(50)  # 50 pairs allowed
s = threading.Semaphore(0)       # Number of available pairs
lock = threading.Semaphore(1)    # Mutex

# Producer thread
def producer():
    while True:
        # Generate correct or wrong pair
        if random.random() < 0.1:
            p1 = random.randint(1, 100)
            p2 = p1  # Wrong pair (duplicate)
            is_valid = False
        else:
            p1 = random.randint(1, 100)
            p2 = random.randint(101, 200)
            is_valid = True

        logging.info(f"[Producer] Trying to produce: ({p1}, {p2})")

        space.acquire()
        lock.acquire()

        if len(buffer) + 2 <= 100:
            buffer.append(p1)
            buffer.append(p2)
            if is_valid:
                logging.info(f"[Producer] ✅ Valid pair produced and added: ({p1}, {p2})")
            else:
                logging.warning(f"[Producer] ❌ Wrong pair added: ({p1}, {p2})")
        else:
            logging.error("[Producer] ❌ Buffer full! Skipping this pair.")

        lock.release()
        s.release()

        time.sleep(random.uniform(0.1, 0.5))

# Consumer thread
def consumer():
    while True:
        s.acquire()
        lock.acquire()

        try:
            p1 = buffer.popleft()
            p2 = buffer.popleft()
            logging.info(f"[Consumer] 📦 Consumed pair: ({p1}, {p2})")
        except IndexError:
            logging.error("[Consumer] ❗️ Buffer underflow or sync issue!")

        lock.release()
        space.release()

        time.sleep(random.uniform(0.5, 1.0))

# Start threads
producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()