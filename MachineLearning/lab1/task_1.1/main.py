import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def linear_regression(x, y):
    n = len(x)

    # Вычисление коэффициентов a и b
    sum_x = np.sum(x)
    sum_y = np.sum(y)
    sum_xy = np.sum(x * y)
    sum_x2 = np.sum(x ** 2)

    a = (sum_x * sum_y / n - sum_xy) / (sum_x ** 2 / n - sum_x2)
    b = (sum_y - a * sum_x) / n

    return a, b


def plot_regression(x, y, a, b):
    fig, ax = plt.subplots()

    ax.scatter(x, y, color='blue', label='Исходные данные')
    ax.plot(x, a * x + b, color='red', label='Регрессионная прямая')

    # Квадраты ошибок
    for xi, yi in zip(x, y):
        y_pred = a * xi + b
        error = yi - y_pred

        rect_x = xi
        rect_y = min(yi, y_pred)
        width = abs(error)
        height = abs(error)

        rect = patches.Rectangle(
            (rect_x, rect_y), width, height,
            linewidth=1, edgecolor='green', facecolor='green', alpha=0.2, hatch='//'
        )
        ax.add_patch(rect)

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.legend()
    plt.show()


def main():
    file_path = input("Введите путь к CSV файлу: ")
    df = pd.read_csv(file_path)
    for i, column in enumerate(df.columns):
        print(f"{i}: {column}")
    x_index = int(input("Выберите столбец для X: "))
    y_index = int(input("Выберите столбец для Y: "))

    x = df.iloc[:, x_index]
    y = df.iloc[:, y_index]

    print("\nСтатистическая информация:")
    print(f"Количество данных: {len(df)}")
    print(f"Минимум по X: {x.min()}, по Y: {y.min()}")
    print(f"Максимум по X: {x.max()}, по Y: {y.max()}")
    print(f"Среднее по X: {x.mean()}, по Y: {y.mean()}")

    a, b = linear_regression(x, y)
    print(f"\nПараметры регрессионной прямой: a = {a}, b = {b}")

    plot_regression(x, y, a, b)


if __name__ == "__main__":
    main()
