import time
from multiprocessing import shared_memory

if __name__ == "__main__":
    shm_a = shared_memory.SharedMemory(name="signal", create=True, size=10)
    signal = shm_a.buf
    signal[0] = 0
    for i in range(10):
        signal[0] +=1
        time.sleep(1)
        print(shm_a.buf[0])

