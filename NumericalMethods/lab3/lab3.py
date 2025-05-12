import numpy as np
import scipy.integrate as spi
import pandas as pd

def f(x):
    return 1 / (x * (1 + x**2))

a, b = 2, 3
true_value, _ = spi.quad(f, a, b)

# Функции для численного интегрирования
def left_rectangles(f, a, b, n):
    x = np.linspace(a, b, n, endpoint=False)
    h = (b - a) / n
    return h * np.sum(f(x))

def right_rectangles(f, a, b, n):
    x = np.linspace(a + (b - a) / n, b, n, endpoint=True)
    h = (b - a) / n
    return h * np.sum(f(x))

def middle_rectangles(f, a, b, n):
    x = np.linspace(a + (b - a) / (2 * n), b - (b - a) / (2 * n), n)
    h = (b - a) / n
    return h * np.sum(f(x))

def trapezoidal(f, a, b, n):
    x = np.linspace(a, b, n)
    y = f(x)
    h = (b - a) / (n - 1)
    return h * (np.sum(y) - 0.5 * (y[0] + y[-1]))

def simpson(f, a, b, n):
    if n % 2 == 1:
        n += 1  # Simpson's rule requires even n
    x = np.linspace(a, b, n)
    y = f(x)
    h = (b - a) / (n - 1)
    return (h / 3) * (y[0] + 4 * np.sum(y[1:-1:2]) + 2 * np.sum(y[2:-2:2]) + y[-1])

methods = {
    "Левых прямоугольников": (left_rectangles, 2048),
    "Правых прямоугольников": (right_rectangles, 2048),
    "Средних прямоугольников": (middle_rectangles, 512),
    "Трапеций": (trapezoidal, 1024),
    "Симпсона": (simpson, 512)
}

data = []
for name, (method, n) in methods.items():
    value = method(f, a, b, n)
    error = abs((true_value - value) / true_value) * 100
    step = (b - a) / n
    data.append([name, round(value, 4), round(step, 6), n, round(error, 6)])

df = pd.DataFrame(data, columns=["Метод", "Значение интеграла", "Величина последнего шага", "Кол-во точек разбиения", "Относительная погрешность (%)"])
print(df)

