import numpy as np
import matplotlib.pyplot as plt

# Интервал t и начальное приближение
num_points = 500
iterations = 10
t_values = np.linspace(-1, 1, num_points)
x = np.ones_like(t_values)  # Начальное приближение x0 = 1

# Рекуррентная формула
results = [x]
for i in range(iterations):
    x_new = np.cos(6 * t_values) + (t_values**2 + 1) / (2 + np.abs(x))
    results.append(x_new)
    x = x_new
    # Вывод данных в консоль
    print(f'Итерация {i + 1}:')
    print(x_new)

# Построение графиков
plt.figure(figsize=(10, 6))
for i in range(iterations):
    plt.plot(t_values, results[i], label=f'Итерация {i}')

plt.title('Графики первых 10 итераций рекуррентной формулы')
plt.xlabel('t')
plt.ylabel('x(t)')
plt.legend(loc='upper left', fontsize='small')
plt.grid()
plt.show()
