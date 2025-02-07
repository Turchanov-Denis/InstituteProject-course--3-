import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(3) * x - np.cos(2 * x) / 2

n = 10
x_vals = np.arange(0, n * 0.5, 0.5)
f_vals = f(x_vals)

for x, fx in zip(x_vals, f_vals):
    print(f"x = {x:.1f}, f(x) = {fx:.7f}")

x_vals = np.linspace(0, 1, 1000)
f_vals = f(x_vals)

plt.plot(x_vals, f_vals, label='f(x)')
plt.axhline(0, color='black', linestyle='--')
plt.xticks(np.arange(0, 1, 0.5))
plt.grid()
plt.legend()
plt.show()
