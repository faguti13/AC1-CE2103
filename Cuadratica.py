"""
Algoritmo de complejidad cuadratica O(n^2) Insertion Sort, cuadratica en el peor caso
"""
import time

def insertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

##########################################################################################################################################

# Pruebas con diferentes tamaños de datos
sizes = [10, 100, 1000, 10000, 100000]
for size in sizes:
    arr = list(range(size, 0, -1))  # Arreglo en orden inverso para peor caso de Insertion Sort
    start_time = time.time_ns()
    insertionSort(arr)
    end_time = time.time_ns()
    execution_time_ns = end_time - start_time
    print(f"Tamaño del arreglo: {size}, Tiempo de ejecución de Insertion Sort: {execution_time_ns} ns.")
