import numpy as np

def iterative_method(C, d, x0, alpha, epsilon, max_iterations=250):
    x_prev = x0
    
    eigenvalues = 100
    
    for n in range(1, max_iterations + 1):
        x_next = np.matmul(C, x_prev) + d
        
        # Логирование
        p2 = np.linalg.norm(x_next - x_prev)
        print(f"Итерация {n}: x_next = {x_next}, p2 = {p2}, {(alpha / (1 - alpha)) * p2}")
        
        # Условие завершения
        if (alpha / (1 - alpha)) * p2 <= epsilon:
            print(f"Итерация завершена на шаге {n} с точностью {epsilon}")
            return x_next, n

        x_prev = x_next

    print("Достигнуто максимальное число итераций.")
    return x_prev, max_iterations

# Данные
C = np.array([
    [0.7, -0.24, -0.22, -0.24],
    [-0.24, 0.7, -0.24, -0.22],
    [-0.22, -0.24, 0.7, -0.24],
    [-0.24, -0.22, -0.24, 0.7]
])
d = np.array([2.76, 2.84, 2.92, 2.42])
x0 = np.array([0.0, 1.0, 2.0, 3.0])
alpha = 0.96

# Запуск
epsilon = 1e-2
x, n = iterative_method(C, d, x0, alpha, epsilon)
print(f"Решение: {x}, Итераций: {n}")
