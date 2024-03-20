#Ejemplo de algoritmo de complejidad exponencial
import time

def exhaustive_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# Función para medir el tiempo de ejecución
def measure_search_time(arr, target, search_algorithm):
    start_time = time.perf_counter_ns()
    index = search_algorithm(arr, target)
    end_time = time.perf_counter_ns()
    elapsed_time = end_time - start_time
    return elapsed_time

# pruebas
sizes = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

for size in sizes:
    print(f"Tamaño del arreglo: {size}, Tiempo de ejecución (Búsqueda Exhaustiva):")
    # array ordenado en orden inverso para el peor caso
    sorted_array = list(range(size, 0, -1))

    target = size + 1

    # tiempo de búsqueda
    elapsed_time = measure_search_time(sorted_array, target, exhaustive_search)

    # resultados
    print(f"{elapsed_time} nanosegundos")
