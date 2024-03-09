def gauss_elimination(matrix, n):
    for i in range(n):
        if matrix[i][i] == 0.0:
            return "Ошибка: Деление на ноль"
        
        for j in range(i+1, n):
            ratio = matrix[j][i]/matrix[i][i]
            
            for k in range(n+1):
                matrix[j][k] = matrix[j][k] - ratio * matrix[i][k]

    solutions = [0] * n
    solutions[n-1] = matrix[n-1][n] / matrix[n-1][n-1]

    for i in range(n-2,-1,-1):
        solutions[i] = matrix[i][n]

        for j in range(i+1,n):
            solutions[i] = solutions[i] - matrix[i][j]*solutions[j]

        solutions[i] = solutions[i] / matrix[i][i]

    return solutions

# Пример 5x5 матрицы и вектора результатов
matrix = [
    [2, 1, 1, 1, 1, 6],
    [1, 2, 1, 1, 1, 6],
    [1, 1, 2, 1, 1, 6],
    [1, 1, 1, 2, 1, 6],
    [1, 1, 1, 1, 2, 6]
]

# Применяем метод Гаусса
result = gauss_elimination(matrix, 5)
print("Решение:", result)
