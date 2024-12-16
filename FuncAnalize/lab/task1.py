import numpy as np


def iterative_method(C, d, x0, alpha, epsilon, max_iterations=250):
    x_prev = x0
    for n in range(1, max_iterations + 1):
        x_next = np.matmul(C, x_prev) + d

        p2 = np.linalg.norm(x_next - x_prev)
        print(f"Итерация {n}: x_next = {x_next}, p2 = {
              p2}, {(alpha / (1 - alpha)) * p2}")

        # Условие завершения
        if (alpha / (1 - alpha)) * p2 <= epsilon:
            print(f"Итерация завершена на шаге {n} с точностью {epsilon}")
            return x_next, n

        x_prev = x_next

    print("Достигнуто максимальное число итераций.")
    return x_prev, max_iterations


# source
A = np.array([
    [1, 2, 3, 4],
    [2, 3, 4, 1],
    [3, 4, 1, 2],
    [4, 1, 2, 3]
])
b = np.array([26, 34, 26, 26]).reshape(-1, 1)
C = np.eye(4) - np.matmul(A, A)/100
print("C=", np.eye(4) - np.matmul(A, A)/100)
d = np.matmul(A, b)/100
print("d=", np.matmul(A, b)/100)
x0 = np.array([1.0, 1.0, 2.0, 3.0]).reshape(-1, 1)
alpha = 0.96


epsilon = 1e-2
x, n = iterative_method(C, d, x0, alpha, epsilon)
# print(f"Решение: {x}, Итераций: {n}")
