#Ejemplo de algoritmo de complejidad logaritmica
import time

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Función para medir el tiempo de ejecución
def measure_search_time(arr, target):
    start_time = time.perf_counter_ns()  # Tiempo inicial en nanosegundos
    index = binary_search(arr, target)
    end_time = time.perf_counter_ns()    # Tiempo final en nanosegundos
    elapsed_time = end_time - start_time
    return elapsed_time

# datos para las pruebas
sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

for size in sizes:
    print(f"Tamaño del arreglo: {size}, Tiempo de ejecución:")
    # Crear un array ordenado en orden inverso para el peor caso
    sorted_array = list(range(size, 0, -1))

    target = size + 1

    # tiempo de búsqueda
    elapsed_time = measure_search_time(sorted_array, target)

    # resultados
    print(f"{elapsed_time} nanosegundos")
