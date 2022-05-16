import time
from multiprocessing import shared_memory

if __name__ == "__main__":
    shm_a = shared_memory.SharedMemory(name="signal")
    signal = shm_a.buf
    for i in range(1000000):
        print(signal[0])
        if signal[0] != 10:
            signal[0] = 10
        time.sleep(1)