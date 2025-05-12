import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 0.5 * (10 * (1 - x)**9 + 13 * (1 - x)**12)

# Метод отклонения
samples = []
n = 1000
while len(samples) < n:
    x = np.random.uniform(0, 1)
    y = np.random.uniform(0, 11.5)  # M = 11.5
    if y <= f(x):
        samples.append(x)

samples = np.array(samples)

# Эмпирическое мат. ожидание
empirical_mean = np.mean(samples)
print("Эмпирическое мат. ожидание:", empirical_mean)
print("Теоретическое мат. ожидание:", 325/4004)
