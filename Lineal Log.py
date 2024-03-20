"""
Algoritmo de complejidad lineal logaritmica O(nlogn) Lineal Sort
"""
import time

def mergeSort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

##########################################################################################################################################

# Pruebas con diferentes tamaños de datos
sizes = [10, 100, 1000, 10000, 100000]
for size in sizes:
    arr = list(range(size, 0, -1))  # Arreglo en orden inverso para peor caso de Merge Sort
    start_time = time.time_ns()
    mergeSort(arr)
    end_time = time.time_ns()
    execution_time_ns = end_time - start_time
    print(f"Tamaño del arreglo: {size}, Tiempo de ejecución de Merge Sort: {execution_time_ns} ns.")
