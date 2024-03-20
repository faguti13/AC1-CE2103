"""
Algoritmo de complejidad lineal O(n) Counting Sort
"""
import time

def countingSort(arr):
    max_element = max(arr)
    count = [0] * (max_element + 1)
    sorted_arr = [0] * len(arr)

    for num in arr:
        count[num] += 1

    for i in range(1, max_element + 1):
        count[i] += count[i - 1]

    for num in reversed(arr):
        sorted_arr[count[num] - 1] = num
        count[num] -= 1

    return sorted_arr

##########################################################################################################################################

# Pruebas con diferentes tamaños de datos
sizes = [10, 100, 1000, 10000, 100000]
for size in sizes:
    arr = list(range(size, 0, -1))  # Arreglo en orden inverso para peor caso de Counting Sort
    start_time = time.time_ns()
    sorted_arr = countingSort(arr)
    end_time = time.time_ns()
    execution_time_ns = end_time - start_time
    print(f"Tamaño del arreglo: {size}, Tiempo de ejecución de Counting Sort: {execution_time_ns} ns.")
