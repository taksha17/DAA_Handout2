# Author Name : Taksha Sachin Thosani
# UTA ID : 1002086312
# Github Link : https://github.com/taksha17/DAA_Handout2


import time
import matplotlib.pyplot as plt
import psutil

def txt6312_sys_info():
    cpu = psutil.cpu_freq()
    ram = psutil.virtual_memory()
    info = {
        'CPU MHz': f'{cpu.current:.2f}',
        'RAM GB': f'{ram.total / (1024**3):.2f}',
        'Available GB': f'{ram.available / (1024**3):.2f}'
    }
    return info

def txt6312_display_info():
    info = txt6312_sys_info()
    print("Sys Info:")
    for k, v in info.items():
        print(f"{k}: {v}")

def txt6312_sort_a(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >=0 and key < arr[j] :
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def txt6312_sort_b(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def txt6312_sort_c(arr):
    for i in range(len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def txt6312_bench(alg, sizes):
    times = []
    for s in sizes:
        arr = list(range(s, 0, -1))
        start = time.time()
        alg(arr)
        times.append(time.time() - start)
    return times

sizes = [5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000]
times_a = txt6312_bench(txt6312_sort_a, sizes)
times_b = txt6312_bench(txt6312_sort_b, sizes)
times_c = txt6312_bench(txt6312_sort_c, sizes)

txt6312_display_info()

plt.figure(figsize=(10, 6))
plt.plot(sizes, times_a, label='Sort A', marker='o')
plt.plot(sizes, times_b, label='Sort B', marker='o')
plt.plot(sizes, times_c, label='Sort C', marker='o')
plt.xlabel('Size')
plt.ylabel('Time (s)')
plt.title('Sorting Benchmarks')
plt.legend()
plt.grid(True)
plt.show()
