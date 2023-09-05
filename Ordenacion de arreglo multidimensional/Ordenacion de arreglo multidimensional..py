def ordenar_fila(matriz, fila):
    # Verificar que la fila requerida sea válida
    if fila < 0 or fila >= len(matriz):
        return "Fila no válida"

    # Algoritmo de selección para ordenar la fila
    for i in range(len(matriz[fila])):
        min_index = i
        for j in range(i + 1, len(matriz[fila])):
            if matriz[fila][j] < matriz[fila][min_index]:
                min_index = j
        matriz[fila][i], matriz[fila][min_index] = matriz[fila][min_index], matriz[fila][i]


# Matriz de (3x3)
mi_matriz = [
    [3, 1, 2],
    [6, 4, 5],
    [9, 7, 8]
]

# Impresion de la matriz original
print("Matriz original:")
for fila in mi_matriz:
    print(fila)

# ingresar la fila a ordenar
try:
    fila_a_ordenar = int(input("Ingresa el número de fila que deseas ordenar (0, 1 o 2): "))
    if fila_a_ordenar < 0 or fila_a_ordenar >= len(mi_matriz):
        raise ValueError("Fila no válida")

    # Función para ordenar la fila
    ordenar_fila(mi_matriz, fila_a_ordenar)

    # Impresion de la matriz ordenada
    print("\nMatriz con la fila ordenada:")
    for fila in mi_matriz:
        print(fila)
except ValueError:
    print("Entrada no válida. Ingresa un número de fila válido.")