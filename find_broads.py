# f(x) = ln(x) + x - 2 = 0
import math


def f(x):
    return math.log(x) + x - 2

x = []
# идти с шагом 1 и искать точку пересечения
for i in range(1, 100):
    if f(i) * f(i + 1) < 0:
        x.append((i, i + 1))

print(f"Точки пересечения: {x}")