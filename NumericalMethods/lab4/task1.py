from sympy import symbols, expand, N

x = symbols('x')

# Узлы интерполяции
x_nodes = [8.1, 8.5, 8.9, 9.2]
y_nodes = [0.9085, 0.9294, 0.9494, 0.9638]

# Функция для вычисления базисного полинома Лагранжа L_k(x)
def lagrange_basis(k, x, x_nodes):
    basis = 1
    x_k = x_nodes[k]
    for j in range(len(x_nodes)):
        if j != k:
            basis *= (x - x_nodes[j]) / (x_k - x_nodes[j])
    return expand(basis)

# Вычисление многочлена Лагранжа P3(x)
P3 = sum(y_nodes[k] * lagrange_basis(k, x, x_nodes) for k in range(len(x_nodes)))
P3 = expand(P3)
P3_rounded = N(P3, 6)
print("Многочлен Лагранжа P3(x):")
print(P3_rounded)
