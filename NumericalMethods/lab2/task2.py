import numpy as np

A = np.array([
    [3.55, 2.31, 6.43, 4.11],
    [6.32, -4.22, -5.13, 4.31],
    [1.99, 3.28, 4.27, -1.33],
    [3.61, 2.88, -2.94, -2.55]
], dtype=float)

b = np.array([-0.58, 12.7, -1.32, 12.45], dtype=float)

# Преобразование матрицы для диагонального преобладания
n = A.shape[0]
for i in range(n):
    max_row = np.argmax(np.abs(A[i:, i])) + i
    if i != max_row:
        A[[i, max_row]] = A[[max_row, i]]
        b[[i, max_row]] = b[[max_row, i]]

# Проверка условий сходимости: диагональное преобладание и достаточное условие сходимости
is_diagonally_dominant = True
for i in range(n):
    if abs(A[i, i]) < sum(abs(A[i, j]) for j in range(n) if j != i):
        is_diagonally_dominant = False
        break

# Проверка достаточного условия сходимости (норма матрицы B < 1)
B = np.zeros((n, n))
c = np.zeros(n)
for i in range(n):
    for j in range(n):
        if i != j:
            B[i, j] = -A[i, j] / A[i, i]
    c[i] = b[i] / A[i, i]

norm_B = np.linalg.norm(B, ord=np.inf)
is_convergent = norm_B < 1

print("Матрица удовлетворяет условию диагонального преобладания:", is_diagonally_dominant)
print("Норма матрицы B:", norm_B)
print("Достаточное условие сходимости выполнено:", is_convergent)

# Метод Зейделя
x = np.zeros(n)
epsilon = 1e-6
max_iter = 1000
iterations = 0

for _ in range(max_iter):
    x_new = np.copy(x)
    for i in range(n):
        sum1 = sum(A[i, j] * x_new[j] for j in range(i))
        sum2 = sum(A[i, j] * x[j] for j in range(i + 1, n))
        x_new[i] = (b[i] - sum1 - sum2) / A[i, i]
    
    if np.linalg.norm(x_new - x, ord=np.inf) < epsilon:
        break
    x = x_new
    iterations += 1

print("Решение:", x)
print("Количество итераций:", iterations)
print("Измененная матрица:")
print(A)