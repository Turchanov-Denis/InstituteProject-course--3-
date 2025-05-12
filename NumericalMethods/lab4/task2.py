import numpy as np
import pandas as pd

# Задаем параметры
a, b = 0, 1  # Интервал
n = 5  # Количество узлов
h = (b - a) / (n - 1)  # Шаг сетки

# Функция f(x) = cos^3(4x)
def f(x):
    return np.cos(4*x)**3

# Первая и вторая точные производные
def df_exact(x):
    return -12 * np.cos(4*x)**2 * np.sin(4*x)

def d2f_exact(x):
    return -48 * np.cos(4*x) * np.sin(4*x) - 48 * np.cos(4*x)**3

# Узлы сетки
x_vals = np.linspace(a, b, n)

# Вычисляем значения функции
f_vals = f(x_vals)

# Численные производные
df_left = np.zeros(n)
df_right = np.zeros(n)
df_center = np.zeros(n)
d2f_center = np.zeros(n)

# Односторонние разности (первого порядка)
df_left[1:] = (f_vals[1:] - f_vals[:-1]) / h
df_right[:-1] = (f_vals[1:] - f_vals[:-1]) / h

# Центральные разности (первого порядка)
df_center[1:-1] = (f_vals[2:] - f_vals[:-2]) / (2 * h)

# Вторая производная (центральные разности)
d2f_center[1:-1] = (f_vals[2:] - 2*f_vals[1:-1] + f_vals[:-2]) / (h**2)

# Точные значения производных
df_exact_vals = df_exact(x_vals)
d2f_exact_vals = d2f_exact(x_vals)

# Погрешности
err_df_left = np.abs(df_left - df_exact_vals)
err_df_right = np.abs(df_right - df_exact_vals)
err_df_center = np.abs(df_center - df_exact_vals)
err_d2f_center = np.abs(d2f_center - d2f_exact_vals)

# Создание таблицы
df_table = pd.DataFrame({
    "x": np.round(x_vals, 4),
    "f(x)": np.round(f_vals, 4),
    "df_left": np.round(df_left, 4),
    "df_right": np.round(df_right, 4),
    "df_center": np.round(df_center, 4),
    "df_exact": np.round(df_exact_vals, 4),
    "err_df_left": np.round(err_df_left, 4),
    "err_df_right": np.round(err_df_right, 4),
    "err_df_center": np.round(err_df_center, 4),
    "d2f_center": np.round(d2f_center, 4),
    "d2f_exact": np.round(d2f_exact_vals, 4),
    "err_d2f_center": np.round(err_d2f_center, 4),
})

# Вывод таблицы
print(df_table)
