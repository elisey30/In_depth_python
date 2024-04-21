# Задача № 1
# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):
    """Транспонирует данную матрицу."""
    return [list(row) for row in zip(*matrix)]


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = transpose_matrix(matrix)
print("Оригинальная матрица:")
for row in matrix:
    print(row)
print("\nТранспонированная матрица:")
for row in transposed:
    print(row)
