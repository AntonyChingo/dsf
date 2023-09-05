def buscar_valor(matriz, valor):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[0])):
            if matriz[fila][columna] == valor:
                return f"El valor {valor} se encontró en la posición ({fila}, {columna})."
    return f"El valor {valor} no se encontró en la matriz."

# Matriz de (3x3)
mi_matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Ingresar el valor a buscar
valor_a_buscar = int(input("Ingresa el valor que deseas buscar: "))

# Funcion para buscar el valor
resultado = buscar_valor(mi_matriz, valor_a_buscar)

# Resultado
print(resultado)