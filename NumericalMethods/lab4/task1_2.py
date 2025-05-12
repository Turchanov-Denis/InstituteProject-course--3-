import numpy as np
import sympy as sp
from scipy.interpolate import lagrange

def lagrange_interpolation(x_vals, y_vals, x_interp):
    x = sp.Symbol('x')
    n = len(x_vals)
    
    # Вычисление базисных полиномов L_k(x)
    L_k = []
    for i in range(n):
        numerator = 1
        denominator = 1
        for j in range(n):
            if i != j:
                numerator *= (x - x_vals[j])
                denominator *= (x_vals[i] - x_vals[j])
        L_k.append(numerator / denominator)
    
    # Построение многочлена Лагранжа
    P_n = sum(y_vals[i] * L_k[i] for i in range(n))
    P_n = sp.simplify(P_n)
    
    # Вычисление значения в x_interp
    y_interp = P_n.subs(x, x_interp)
    
    return P_n, y_interp

# Исходные данные
x_vals = np.array([8.1, 8.5, 8.9, 9.3])
y_vals = np.log10(x_vals)  # Так как y = log10(x)
x_interp = 9.1

# Вычисление многочлена Лагранжа и значения в x_interp
P_n, y_interp = lagrange_interpolation(x_vals, y_vals, x_interp)

# Аналитическое значение log10(9.1)
y_actual = np.log10(x_interp)

# Абсолютная погрешность
error = abs(y_actual - float(y_interp))

# Вывод результатов
print(f'Интерполяционный многочлен Лагранжа: {P_n}')
print(f'Значение P_n(9.1): {y_interp}')
print(f'Аналитическое значение log10(9.1): {y_actual}')
print(f'Абсолютная погрешность: {error}')
