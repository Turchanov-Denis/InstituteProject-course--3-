import numpy as np


def f(x):
    return np.sqrt(3) * x - np.cos(2 * x) / 2


def df(x):
    return np.sqrt(3) + np.sin(2 * x)


def newton_method(x0, tol=1e-7):
    x = x0
    iteration = 1
    while True:
        fx = f(x)
        dfx = df(x)
        x_new = x - fx / dfx
        err = abs(fx)
        order_of_error = np.log10(err)  # вычисляем порядок погрешности
        print(f"Метод Ньютона, Шаг {iteration}: x = {x_new:.7f}, погрешность = {err}, порядок погрешности = {order_of_error:.2f}")
        if abs(fx) < tol:
            return x_new
        x = x_new
        iteration += 1


def secant_method(x0, x1, tol=1e-7):
    iteration = 1
    while True:
        fx0, fx1 = f(x0), f(x1)
        x_new = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        err = abs(fx1)
        order_of_error = np.log10(err)  # вычисляем порядок погрешности
        print(f"Метод секущих, Шаг {iteration}: x = {x_new:.7f}, погрешность = {err}, порядок погрешности = {order_of_error:.2f}")
        if abs(fx1) < tol:
            return x_new
        x0, x1 = x1, x_new
        iteration += 1


def chord_method(a, b, tol=1e-7):
    iteration = 1
    while True:
        fa, fb = f(a), f(b)
        x_new = a - fa * (b - a) / (fb - fa)
        err = abs(f(x_new))
        order_of_error = np.log10(err)  # вычисляем порядок погрешности
        print(f"Метод хорд, Шаг {iteration}: x = {x_new:.7f}, погрешность = {err}, порядок погрешности = {order_of_error:.2f}")
        if abs(f(x_new)) < tol:
            return x_new
        if f(a) * f(x_new) < 0:
            b = x_new
        else:
            a = x_new
        iteration += 1


def steffensen_method(x0, tol=1e-7):
    iteration = 1
    while True:
        fx = f(x0)
        g = (f(x0 + fx) - fx) / fx
        x_new = x0 - fx / g
        err = abs(fx)
        order_of_error = np.log10(err)  # вычисляем порядок погрешности
        print(f"Метод Стеффенсена, Шаг {iteration}: x = {x_new:.7f}, погрешность = {err}, порядок погрешности = {order_of_error:.2f}")
        if abs(fx) < tol:
            return x_new
        x0 = x_new
        iteration += 1


def simple_iteration_method(x0, tau, tol=1e-7, max_iter=100):
    x = x0
    for k in range(max_iter):
        x_new = x - tau * f(x)
        err = abs(x_new - x)
        order_of_error = np.log10(err)  # вычисляем порядок погрешности
        print(f"Метод простых итераций, Шаг {k+1}: x = {x_new:.7f}, погрешность = {err}, порядок погрешности = {order_of_error:.2f}")
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x


def newton_difference_method(x0, h=0.025, tol=1e-7, max_iter=100):
    x = x0
    for k in range(max_iter):
        fx = f(x)
        fx_plus_fx = f(x + fx) 

        x_new = x - (fx**2) / (fx_plus_fx - fx)
        
        err = abs(x_new - x)
        order_of_error = np.log10(err)  # вычисляем порядок погрешности
        print(f"Метод разности Ньютона, Шаг {k+1}: x = {x_new:.7f}, погрешность = {err}, порядок погрешности = {order_of_error:.2f}")
        
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return x


# Начальные приближения
x_newton = newton_method(0.5)
x_secant = secant_method(0.4, 0.1)
x_chord = chord_method(0.5, 0.1)
x_steffensen = steffensen_method(0.1)
x_simple_iter = simple_iteration_method(0.1, 0.2)
x_solution = newton_difference_method(0.1)

# Вывод результатов
print(f"\nМетод Ньютона: {x_newton:.7f}")
print(f"Метод секущих: {x_secant:.7f}")
print(f"Метод хорд: {x_chord:.7f}")
print(f"Метод Стеффенсена: {x_steffensen:.7f}")
print(f"Метод простых итераций: {x_simple_iter:.7f}")
print(f"Метод разности Ньютона: {x_solution:.7f}")
