import numpy as np
from math import sin, cos
from tabulate import tabulate

# --- УРАВНЕНИЕ 1 ---
# y' = 2 + sin(x) - 3y^2

def f1(x, y):
    return 2 + sin(x) - 3 * y**2

def euler_koshi(f, a, b, y0, eps):
    N = 2
    max_diff = float('inf')
    while max_diff > eps:
        h = (b - a) / N
        x_old = [a + i * h for i in range(N+1)]
        y_old = [y0]
        for i in range(N):
            k1 = f(x_old[i], y_old[i])
            y_mid = y_old[i] + (h / 2) * k1
            k2 = f(x_old[i] + h / 2, y_mid)
            y_old.append(y_old[i] + h * k2)

        N *= 2
        h_new = (b - a) / N
        x_new = [a + i * h_new for i in range(N+1)]
        y_new = [y0]
        for i in range(N):
            k1 = f(x_new[i], y_new[i])
            y_mid = y_new[i] + (h_new / 2) * k1
            k2 = f(x_new[i] + h_new / 2, y_mid)
            y_new.append(y_new[i] + h_new * k2)

        max_diff = max(abs(y_new[2*i] - y_old[i]) for i in range(len(y_old)))

    return x_new, y_old, y_new

def runge_kutta(f, a, b, y0, eps):
    N = 2
    max_diff = float('inf')
    while max_diff > eps:
        h = (b - a) / N
        x_old = [a + i*h for i in range(N+1)]
        y_old = [y0]
        for i in range(N):
            k1 = h * f(x_old[i], y_old[i])
            k2 = h * f(x_old[i]+h/2, y_old[i]+k1/2)
            k3 = h * f(x_old[i]+h/2, y_old[i]+k2/2)
            k4 = h * f(x_old[i]+h, y_old[i]+k3)
            y_old.append(y_old[i] + (k1 + 2*k2 + 2*k3 + k4)/6)

        N *= 2
        h_new = (b - a) / N
        x_new = [a + i*h_new for i in range(N+1)]
        y_new = [y0]
        for i in range(N):
            k1 = h_new * f(x_new[i], y_new[i])
            k2 = h_new * f(x_new[i]+h_new/2, y_new[i]+k1/2)
            k3 = h_new * f(x_new[i]+h_new/2, y_new[i]+k2/2)
            k4 = h_new * f(x_new[i]+h_new, y_new[i]+k3)
            y_new.append(y_new[i] + (k1 + 2*k2 + 2*k3 + k4)/6)

        max_diff = max(abs(y_new[2*i] - y_old[i]) for i in range(len(y_old)))

    return x_new, y_old, y_new

# --- УРАВНЕНИЕ 2 ---
# y'' = cos(x + y) + 3.5(x - y)

def f2_sys(x, y, g):
    dy = g
    dg = cos(x + y) + 3.5 * (x - y)
    return dy, dg

def euler_init(x, y, g, h):
    dy, dg = f2_sys(x, y, g)
    return y + h*dy, g + h*dg

def adams(f_sys, a, b, y0, g0, order, eps):
    N = 2 ** (order + 1)
    max_diff = float('inf')
    while max_diff > eps:
        h = (b - a) / N
        x_old = [a + i*h for i in range(N+1)]
        y_old = [y0]
        g_old = [g0]

        for i in range(order):
            y_next, g_next = euler_init(x_old[i], y_old[i], g_old[i], h)
            y_old.append(y_next)
            g_old.append(g_next)

        for i in range(order, N):
            f0 = f2_sys(x_old[i], y_old[i], g_old[i])
            f1_ = f2_sys(x_old[i-1], y_old[i-1], g_old[i-1])
            f2_ = f2_sys(x_old[i-2], y_old[i-2], g_old[i-2])
            if order == 3:
                y_next = y_old[i] + h*(23*f0[0] - 16*f1_[0] + 5*f2_[0])/12
                g_next = g_old[i] + h*(23*f0[1] - 16*f1_[1] + 5*f2_[1])/12
            else:
                f3_ = f2_sys(x_old[i-3], y_old[i-3], g_old[i-3])
                y_next = y_old[i] + h*(55*f0[0] - 59*f1_[0] + 37*f2_[0] - 9*f3_[0])/24
                g_next = g_old[i] + h*(55*f0[1] - 59*f1_[1] + 37*f2_[1] - 9*f3_[1])/24
            y_old.append(y_next)
            g_old.append(g_next)

        # Повтор с удвоением
        N2 = 2 * N
        h2 = (b - a) / N2
        x_new = [a + i*h2 for i in range(N2+1)]
        y_new = [y0]
        g_new = [g0]

        for i in range(order):
            y_next, g_next = euler_init(x_new[i], y_new[i], g_new[i], h2)
            y_new.append(y_next)
            g_new.append(g_next)

        for i in range(order, N2):
            f0 = f2_sys(x_new[i], y_new[i], g_new[i])
            f1_ = f2_sys(x_new[i-1], y_new[i-1], g_new[i-1])
            f2_ = f2_sys(x_new[i-2], y_new[i-2], g_new[i-2])
            if order == 3:
                y_next = y_new[i] + h2*(23*f0[0] - 16*f1_[0] + 5*f2_[0])/12
                g_next = g_new[i] + h2*(23*f0[1] - 16*f1_[1] + 5*f2_[1])/12
            else:
                f3_ = f2_sys(x_new[i-3], y_new[i-3], g_new[i-3])
                y_next = y_new[i] + h2*(55*f0[0] - 59*f1_[0] + 37*f2_[0] - 9*f3_[0])/24
                g_next = g_new[i] + h2*(55*f0[1] - 59*f1_[1] + 37*f2_[1] - 9*f3_[1])/24
            y_new.append(y_next)
            g_new.append(g_next)

        max_diff = max(abs(y_new[2*i] - y_old[i]) for i in range(len(y_old)))
        N = N2

    return x_new, y_old, y_new

# --- ЗАПУСК ---

a, b = 0, 0.5
eps = 0.001

# Уравнение 1
x1, y1_pre, y1_post = euler_koshi(f1, a, b, 0, eps)
x2, y2_pre, y2_post = runge_kutta(f1, a, b, 0, eps)

# Уравнение 2
x3, y3_pre, y3_post = adams(f2_sys, a, b, 1, 0, order=3, eps=eps)
x4, y4_pre, y4_post = adams(f2_sys, a, b, 1, 0, order=4, eps=eps)

# Функция для вывода точек с ограничением на количество
def print_table(title, x_full, y_pre, y_post, max_points=16):
    # находим индексы, где значения отличаются от нуля
    start_index = next(i for i, y in enumerate(y_pre) if y != 0)
    
    # ограничиваем количество точек до max_points
    n = min(max_points, len(y_pre) - start_index)  # количество точек, которое реально есть
    table = []
    
    for i in range(n):
        idx_pre = start_index + i
        idx_post = 2 * idx_pre
        if idx_post >= len(y_post):
            break
        x = x_full[idx_post]
        y_pre_val = y_pre[idx_pre]
        y_post_val = y_post[idx_post]
        diff = abs(y_post_val - y_pre_val)
        table.append([f"{x:.5f}", f"{y_pre_val:.6f}", f"{y_post_val:.6f}", f"{diff:.2e}"])
    
    print(f"\n{title}\n")
    print(tabulate(table, headers=["x", "Y (пред.)", "Y (посл.)", "Разность"], tablefmt="grid"))

print_table("Метод Эйлера-Коши", x1, y1_pre, y1_post)
print_table("Метод Рунге-Кутты 4 порядка", x2, y2_pre, y2_post)
print_table("Метод Адамса 3 порядка", x3, y3_pre, y3_post)
print_table("Метод Адамса 4 порядка", x4, y4_pre, y4_post)
