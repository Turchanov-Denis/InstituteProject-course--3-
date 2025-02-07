import numpy as np

def gauss_method(A):
    n = len(A)
    
    for i in range(n):
        max_row = np.argmax(abs(A[i:, i])) + i
        A[[i, max_row]] = A[[max_row, i]]
        A[i] = A[i] / A[i, i]
        for j in range(i + 1, n):
            A[j] -= A[j, i] * A[i]
    
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = A[i, -1] - np.sum(A[i, i + 1:n] * x[i + 1:n])
    
    return A, x

def calculate_error(x, x_true):
    return np.abs((x_true - x) / x_true)

A = np.array([
    [3.55, 2.31, 6.43, 4.11, -0.58],
    [6.32, -4.22, -5.13, 4.31, 12.45],
    [1.99, 3.28, 4.27, -1.33, -1.32],
    [3.61, 2.88, -2.94, -2.55, 12.7]
], dtype=float)

A_triangular, x = gauss_method(A)
x_true = np.array([1, 2, -2, 1])
delta = calculate_error(x, x_true)

print("Матрица в треугольном виде:")
np.set_printoptions(precision=6)
print(A_triangular)
print("Решение системы:")
np.set_printoptions(precision=20)
print(x)
print("Относительная погрешность (покомпонентно):", delta)