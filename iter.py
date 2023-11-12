# f(x) = ln(x) + x - 2 = 0
import math

def f(x):
    return 2 - math.log(x)

x = 2
eps = 0.001

i = 1
while True:
    print(f"Итерация {i}, x = {x}")
    x1 = f(x)
    print(f"x1 = {x1}, abs(x1-x) = {abs(x1-x)}\n")
    if abs(x1 - x) < eps:
        x = x1
        break
    x = x1
    i += 1