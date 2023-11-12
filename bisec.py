# f(x) = ln(x) + x - 2 = 0
import math

def f(x):
    return math.log(x) + x - 2


a = 1
b = 2
eps = 0.01

i = 1
while True:
    x = (a + b) / 2
    print(f"Итерация {i}")
    print(f"a = {a}, b = {b}, x = {x}\n")
    if abs(b - a) < eps:
        break
    if f(a) * f(x) < 0:
        b = x
    else:
        a = x
    i += 1